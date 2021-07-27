# -*- coding: utf-8 -*-
# file helps to fix isort bug: puts it after packages isort
import inspect
import os
import sys

# sys.path.insert(0, '..') # not working with isort # pull request v2

currentdir = os.path.dirname(os.path.abspath(  # noqa
    inspect.getfile(inspect.currentframe())))  # noqa
parentdir = os.path.dirname(currentdir)  # noqa
sys.path.insert(0, parentdir)  # noqa
