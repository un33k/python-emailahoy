# -*- coding: utf-8 -*-

import sys 
import smtplib
import socket
import re
from utils import query_mx

# only allow the import of our public APIs (UU-SLUG = Uniqure & Unicode Slug)
__all__ = ['VerifyEmail', 'verify_email_address']


class VerifyEmail(object):
    """ Verify if email exists """

    EMAIL_RE = re.compile('([\w\-\.+]+@\w[\w\-]+\.+[\w\-]+)')
    default_response = (550, 'Unknown')
    
    # given a hostname, all mx records will be returned
    def get_mx_for_hostname(self, hostname):
        mx = []
        if self.is_hostname_valid(hostname):
            try:
                mx = query_mx(hostname)
            except:
                pass
        return mx
    
    # given a host name, returns True if valid, else False
    def is_hostname_valid(self, hostname):
        """ if hostname is valid """
        try:
            socket.gethostbyname(hostname)
        except:
            return False
        return True

    # given an email address, returns True if email matches a valid pattern
    def is_email_valid(self, email):
        """ if a given email maches the email pattern """
        return self.EMAIL_RE.search(email)

    # given an email, hostname is returned
    def get_hostname_from_email(self, email):
        try:
            hostname = email.strip().split('@')[1]
        except:
            hostname = None
        return hostname

    # given a hostname, a smtp server connection is returned or None
    def get_smtp_connection(self, hostname):
        """ returns server with valid connection if possible """
        resp = self.default_response
        connection_success = lambda x: x[0] == 220
        if self.is_hostname_valid(hostname):
            server = smtplib.SMTP()
            try:
                resp = server.connect(hostname)
            except:
                pass
            if connection_success(resp):
                return server
        return None
    
    # given a  response tuple, it returns True if status was success
    def was_found(self, resp):
        """ email WAS found """
        return resp[0] == 250

    # given a response tuple, it returns True if it can tell if email was not found
    def not_found(self, resp):
        """ email was NOT found """
        not_found_words = [
                "does not exist",
                "doesn't exist",
                "rejected", 
                "disabled",
                "discontinued",
                "unavailable",
                "unknown",
                "invalid",
                "doesn't handle",
        ]
        if resp[0] != 250 and any(a in resp[1].lower() for a in not_found_words):
            return True

    # given a response tuple, it returns true if it couldn't tell, if email found or not
    def could_not_verify_status(self, resp):
        """ email unverifiable """
        return not (self.was_found(resp) or self.not_found(resp))
    
    # returns a response tuple indicating the existance of an email address
    def verify_email_smtp(
        self,
        email,
        from_host='example.com',
        from_email='verify@example.com'
        ):
        """ if an email does exsit """
        
        cmd_success = lambda x: x[0] == 250
        found = False
        resp = self.default_response
        if self.is_email_valid(email):
            hostname = self.get_hostname_from_email(email)
            mx = self.get_mx_for_hostname(hostname)
            for m in mx:
                server = self.get_smtp_connection(m[1])
                if server:
                    try:
                        resp = server.docmd('HELO %s' % from_host)
                    except:
                        continue
                    if cmd_success(resp):
                        try:
                            resp = server.docmd('MAIL FROM: <%s>' % from_email)
                        except:
                            continue
                        if cmd_success(resp):
                            try:
                                resp = server.docmd('RCPT TO: <%s>' % email)
                            except:
                                continue
                            break
        return resp
            
# given an email it returns True if it can tell it exist or False
def  verify_email_address(email):
    e = VerifyEmail()
    status = e.verify_email_smtp(email)
    if e.was_found(status):
        return True
    return False

# if __name__ == "__main__":
#     # e = VerifyEmail()
#     # status = e.verify_email_smtp(sys.argv[1])
#     # if e.was_found(status):
#     #     print >> sys.stderr, "Found:", status
#     # elif e.not_found(status):
#     #     print >> sys.stderr, "Not Found:", status
#     # else:
#     #     print >> sys.stderr, "Unverifiable:", status
# 
#     if verify_email_address(sys.argv[1]):
#         print >> sys.stderr, "Found"
#     else:
#         print >> sys.stderr, "Not found"


