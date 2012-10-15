# -*- coding: utf-8 -*-

import unittest
from emailahoy import VerifyEmail
from emailahoy import query_mx
from emailahoy import verify_email_address

class TestEmailVerificationFunctions(unittest.TestCase):

    def setUp(self):
        """ Instantiate the class """
        self.e = VerifyEmail()

    def test_class_based_invalid_email(self):
        """ Test the existance of an invalid email address (class based)"""
        status = self.e.verify_email_smtp(
                            email='non-existing-email@gmail.com',
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        # email doesn't exist
        self.assertEquals(self.e.not_found(status), True)

    def test_class_based_valid_email(self):
        """ Test the existance of a valid email address (class based)"""
        status = self.e.verify_email_smtp(
                            email='info@neekware.com',
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        # email exists
        self.assertEquals(self.e.was_found(status), True)

    def test_function_based_invalid_email(self):
        """ Test the existance of an invalid email address (function based)"""

        found = verify_email_address(
                            email='non-existing-email@gmail.com',
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        # email doesn't exists
        self.assertEquals(found, False)
            

    def test_function_based_valid_email(self):
        """ Test the existance of a valid email address (function based)"""

        found = verify_email_address(
                            email='info@neekware.com',
                            from_host='neekware.com',
                            from_email='info@neekware.com'
                        )
        # email exists
        self.assertEquals(found, True)
            

    def test_mx_query_invalid_domain(self):
        """ Query mx of an invalid domain name """
        mx = query_mx('invalid_domain_address.com')
        self.assertEquals(len(mx), 0)


    def test_mx_query_valid_domain(self):
        """ Query mx of a valid domain name """

        mx = query_mx('gmail.com')
        self.assertGreater(len(mx), 0)


if __name__ == '__main__':
    unittest.main()


