# -*- coding: utf-8 -*-
import builtins
import inspect
import math
import os
import sys

import numpy
import pytest

from main_package import *

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


def test_answer():
    assert len(methods_importer('abs', [math, builtins, numpy])) == 2


class TestPrepend:
    @pytest.mark.parametrize(
        'test_case,expected_result',
        [
            (len(methods_importer('abs', [math, builtins, numpy])), 2),
            (len(methods_importer('abs', [math])), 0),
            (len(methods_importer('abs', [numpy])), 1),
        ],
    )
    def test_multiple_mutable_structure(self, test_case, expected_result, our_great_fixture):
        print('Do stuff')
        assert test_case == expected_result + (our_great_fixture * 0)

    @pytest.fixture
    def our_great_fixture(self):
        print('Do smth before fixter is used (printed at failure only)')
        # yield
        print('Do smth after fixter is used (printed at failure only)')
        return 2

    def test_fixture(self, our_great_fixture):
        print('Do stuff')
        assert 2 == our_great_fixture

    @pytest.fixture(autouse=True)
    def auto_fixture(self):
        print('Do smth before fun (printed at failure only)')
        yield
        print('Do smth after fun (printed at failure only)')
