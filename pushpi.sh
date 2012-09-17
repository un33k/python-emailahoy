#!/bin/bash

python setup.py register
python setup.py bdist_egg upload --identity="val Neekman" --sign --quiet
python setup.py bdist_wininst --target-version=2.7 register upload --identity="Val Neekman" --sign --quiet
python setup.py sdist upload --identity="Val Neekman" --sign

