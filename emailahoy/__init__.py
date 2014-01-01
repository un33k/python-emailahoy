# -*- coding: utf-8 -*-

__version__ = '0.0.6'

import re
import sys 
import socket
import popen2
import smtplib as _smtp

DEBUG = True

__all__ = ['VerifyEmail', 'verify_email_address', 'query_mx']

MX_RE = re.compile('mail\sexchanger\s=\s(\d+)\s(.*)\.')
EMAIL_RE = re.compile('([\w\-\.+]+@\w[\w\-]+\.+[\w\-]+)')
NOT_FOUND_KEYWORDS = [
    "does not exist",
    "doesn't exist",
    "doesn't have",
    "doesn't handle",
    "unknown user",
    "user unknown",
    "rejected", 
    "disabled",
    "discontinued",
    "unavailable",
    "unknown",
    "invalid",
    "typos",
    "unnecessary spaces",
]

UNVERIFIABLE_KEYWORDS = [
    "block",
    "block list",
    "spam",
    "spammer",
    "isp",
    "weren't sent",
    "not accepted",
]


def query_mx(host):
    """ Returns all MX records of a given domain name """

    mail_exchangers = []
    addr = {}
    fout, fin = popen2.popen2('which nslookup')
    cmd = fout.readline().strip()
    if cmd <> '':
        fout, fin = popen2.popen2('%s -query=mx %s' % (cmd, host))
        line = fout.readline()
        while line <> '':
            mx = MX_RE.search(line.lower())
            if mx:
                mail_exchangers.append((eval(mx.group(1)), mx.group(2)))
            line = fout.readline()

        if mail_exchangers:
            mail_exchangers.sort()
    return mail_exchangers


class VerifyEmail(object):
    """ Verify if email exists """

    EMAIL_FOUND = 1
    EMAIL_NOT_FOUND = 2 
    UNABLE_TO_VERIFY = 3


    def connect(self, hostname, timeout=10):
        """ Returns a server connection or None given a hostname """

        try:
            socket.gethostbyname(hostname)
            server = _smtp.SMTP(timeout=timeout)
            code, resp = server.connect(hostname)
            if code == 220:
                return server
        except:
            pass
        return None


    def unverifiable(self, resp):
        """ Return true if email is not verifiable """
        return any(a in resp.lower() for a in UNVERIFIABLE_KEYWORDS)


    def nonexistent(self, resp):
        """ Return true if email is not verifiable """
        return any(a in resp.lower() for a in NOT_FOUND_KEYWORDS)


    def verify(
        self,
        email,
        from_host='example.com',
        from_email='verify@example.com'
        ):
        """ verifies wether an email address does exsit """

        if not EMAIL_RE.search(email):
            return self.EMAIL_NOT_FOUND

        try:
            hostname = email.strip().split('@')[1]
            socket.gethostbyname(hostname)
            mail_exchangers = query_mx(hostname)
        except:
            return self.UNABLE_TO_VERIFY

        for mx in mail_exchangers:
            mx_name = mx[1]
            server = self.connect(mx_name)
            if not server:
                continue
            if DEBUG:
                server.set_debuglevel(1)
            code, resp = server.helo(mx_name)
            if code != 250:
                if not self.unverifiable(resp):
                    return self.UNABLE_TO_VERIFY
                continue
            code, resp = server.mail(from_email)
            if code != 250:
                if not self.unverifiable(resp):
                    return self.UNABLE_TO_VERIFY
                continue
            code, resp = server.rcpt(email)
            if code != 250:
                if self.nonexistent(resp):
                    return self.EMAIL_NOT_FOUND
                elif self.unverifiable(resp):
                    return self.UNABLE_TO_VERIFY
                else:
                    continue
            code, resp = server.data('Ahoy. Are you there?{0}.{0}'.format(_smtp.CRLF))
            if code != 250:
                if self.nonexistent(resp):
                    return self.EMAIL_NOT_FOUND
                elif self.unverifiable(resp):
                    return self.UNABLE_TO_VERIFY
            elif code == 250:
                return self.EMAIL_FOUND

        return self.UNABLE_TO_VERIFY


# given an email it returns True if it can tell it exist or False
def  verify_email_address(
                email, 
                from_host='example.com',
                from_email='verify@example.com'
                ):
    """ A quick email verification fuction """
    e = VerifyEmail()
    status = e.verify(email, from_host, from_email)
    print status
    if status == e.EMAIL_NOT_FOUND:
        return False
    return True

if __name__ == "__main__":
   # if verify_email_address('un33kvu@gmail.com', 'djanguru.djanguru.net', 'verify@djanguru.net'):
   # if verify_email_address('un33ksssddsdsd333vu@gmail.com', 'djanguru.net', 'verify@djanguru.net'):
   # if verify_email_address('un33kvu@yahoo.com', 'djanguru.net', 'verify@djanguru.net'):
   # if verify_email_address('un33ksssddsdsd333vu@yahoo.com', 'djanguru.net', 'verify@djanguru.net'):
   # if verify_email_address('un33ksssddsdsd333vu@cnn.com', 'djanguru.net', 'verify@djanguru.net'):
   # if verify_email_address('vman@outsourcefactor.com', 'djanguru.net', 'verify@djanguru.net'):
   if verify_email_address('asfsadfasfsdf@hotmail.com', 'djanguru.net', 'verify@djanguru.net'):
       print "found"
