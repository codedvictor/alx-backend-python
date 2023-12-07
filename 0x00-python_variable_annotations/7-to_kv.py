#!/usr/bin/env python3
"""
a type-annotated function to_kv
"""
from typing import Union, Tuple
from math import pow


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    """
    convert to str & int|float to tuple
    """
    return (k, pow(v, 2))
