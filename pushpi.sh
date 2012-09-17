#!/bin/bash

python setup.py register
# python setup.py bdist upload --identity="val Neekman" --sign
python setup.py sdist upload --identity="Val Neekman" --sign

