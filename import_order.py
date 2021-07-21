# -*- coding: utf-8 -*-
import builtins
import importlib
import math
import sys  # noqa
from types import ModuleType
from typing import Callable, List, Optional, Union

import numpy


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    """
    Method has to check if any of `modules` contains
     `callable` object with name `method_name`
    and return list of such objects
    args:
        method_name - name of object (method) we wanna find
        modules - where to search. Given by str or Module object.
    return: list of modules, that contain this method_name
    """
    result = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError('Must be list of strings or ModuleType')

            met = getattr(mod, method_name, None)

            if met:
                result.append(mod)
                # return met

        except ImportError:
            continue

    return result


def search_import(
    method: str, modules: List[Union[str, ModuleType]]
) -> Optional[object]:
    """
    Method has to check if any of `modules` contains
    `callable` object with name `method_name`
    and return list of such objects
    args:
        method - name of object (method) we wanna find
        modules - where to search. Given by str or Module object.
    return: first found object (method)
    """
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                # get module by string name
                mod = importlib.import_module(module)
            else:
                raise TypeError('Must be list of strings or ModuleType')

            # get method from module by string name
            met = getattr(mod, method, None)

            if met:
                return met

        except ImportError:  # import_module can fail
            continue

    return None


# 1) MAIN TESTS-----------:

print(search_import('abs', [math, builtins, numpy]))
# => returns first abs form builtins

print(methods_importer('abs', [math, builtins, numpy]))
# => abs exist in builtins and in numpy

# 2) ADDITIONAL TESTS-----------:
# print(search_import('__import__', ['builtins']))
# <built-in function __import__>

# print(search_import('nothing', ['builtins']))
# None

# print(sys.meta_path)
# [
#   <class '_frozen_importlib.BuiltinImporter'>,
#   <class '_frozen_importlib.FrozenImporter'>,
#   <class '_frozen_importlib_external.PathFinder'>
# ]
