import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='python-emailahoy',
    version='0.1',
    description = "A Python email utility that verifies existence of an email address",
    long_description = read('README'),
    author='Val Neekman',
    author_email='val@neekware.com',
    url='http://github.com/un33k/python-emailahoy',
    packages=['emailahoy'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Communications :: Email',
    ],
)
