Python Email Ahoy
====================

**A Python email utility that verifies existence of an email address**

**Author:** Val Neekman [ info@neekware.com, @vneekman ]

Overview
========

A Python email utility that verifies existence of an email address.

How to install
==================

    1. easy_install python-emailahoy
    2. pip install python-emailahoy
    3. git clone http://github.com/un33k/python-emailahoy
        a. cd python-emailahoy
        b. run python setup.py
    4. wget https://github.com/un33k/python-emailahoy/zipball/master
        a. unzip the downloaded file
        b. cd into python-emailahoy-* directory
        c. run python setup.py

How to use
=================

``Use the class for more control & more granular return status``

    from emailahoy import VerifyEmail
    e = VerifyEmail()
    status = e.verify_email_smtp(
                        email='test@example.com',
                        from_host='mydomain.com',
                        from_email='verify@mydomain.com' 
                    )
    if e.was_found(status):
        print >> sys.stderr, "Found:", status
    elif e.not_found(status):
        print >> sys.stderr, "Not Found:", status
    else:
        print >> sys.stderr, "Unverifiable:", status

``Use the shorthand function for quick check``

    if verify_email_address('test@example.com'):
        print >> sys.stderr, "Found"
    else:
        print >> sys.stderr, "Don't care"

``Note:``
    1. Not all email servers will return the correct status
    2. Checking an invalid email address returns within 1 second
    3. Checking a valid email address returns within 4 seconds or more


Running the tests
=================

To run the tests against the current environment:

    python test.py

Changelog
=========

0.0.3
-----
* Added Travis CI support

0.2
-----
* Removed dependency on external packages (pydns)

0.1
-----

* Initial release


License
=======

Copyright (c) 2012, Val Neekman
Neekware Inc.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



