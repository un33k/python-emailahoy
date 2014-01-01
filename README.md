Python Email Ahoy
====================

**A Python email utility that verifies existence of an email address**


[![build-status-image-fury]][fury]
[![build-status-image-pypi]][pypi]


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

License
====================

Protected by ([BSD](LICENSE.md))


[build-status-image-travis]: https://secure.travis-ci.org/un33k/python-emailahoy.png?branch=master
[travis]: http://travis-ci.org/tomchristie/python-emailahoy?branch=master

[build-status-image-fury]: https://badge.fury.io/py/python-emailahoy.png
[fury]: http://badge.fury.io/py/python-emailahoy

[build-status-image-pypi]: https://pypip.in/d/python-emailahoy/badge.png
[pypi]: https://crate.io/packages/python-emailahoy?version=latest

