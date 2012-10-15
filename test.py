# -*- coding: utf-8 -*-

import unittest
from emailahoy import VerifyEmail
from emailahoy import query_mx
from emailahoy import verify_email_address
import sys
import logging

class TestEmailVerificationFunctions(unittest.TestCase):

    def setUp(self):
        """ Instantiate the class """
        self.e = VerifyEmail()
        self.log= logging.getLogger( "TestEmailVerificationFunctions" )
        

    def test_class_based_invalid_email(self):
        """ Test the existance of an invalid email address (class based)"""
        
        email = 'non-existing-email@gmail.com'
        self.log.debug("Testing classy invalid email address (%s)" % email)
        
        status = self.e.verify_email_smtp(
                            email=email,
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        
        self.log.debug(status)
        self.assertEquals(self.e.not_found(status), True)

    def test_class_based_valid_email(self):
        """ Test the existance of a valid email address (class based)"""
        
        email = 'info@neekware.com'
        self.log.debug("Testing classy valid email address (%s)" % email)
        status = self.e.verify_email_smtp(
                            email='info@neekware.com',
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        
        self.log.debug(status)
        self.assertEquals(self.e.was_found(status), True)

    def test_function_based_invalid_email(self):
        """ Test the existance of an invalid email address (function based)"""

        email = 'non-existing-email@gmail.com'
        self.log.debug("Testing invalid email address (%s)" % email)
        
        found = verify_email_address(
                            email=email,
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        
        # email doesn't exists
        self.assertEquals(found, False)
            

    def test_function_based_valid_email(self):
        """ Test the existance of a valid email address (function based)"""
        
        email = 'info@neekware.com'
        self.log.debug("Testing valid email address (%s)" % email)
        
        found = verify_email_address(
                            email=email,
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        # email exists
        self.assertEquals(found, True)
            

    def test_mx_query_invalid_domain(self):
        """ Query mx of an invalid domain name """
        
        domain = 'invalid_domain_address.com'
        self.log.debug("Testing MX Query for invalid domain (%s)" % domain)
        mx = query_mx(domain)
        self.assertEquals(len(mx), 0)


    def test_mx_query_valid_domain(self):
        """ Query mx of a valid domain name """
        
        domain = 'gmail.com'
        self.log.debug("Testing MX Query for valid domain (%s)" % domain)
        
        mx = query_mx('gmail.com')
        self.assertGreater(len(mx), 0)


if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestEmailVerificationFunctions" ).setLevel( logging.DEBUG )
    unittest.main()


