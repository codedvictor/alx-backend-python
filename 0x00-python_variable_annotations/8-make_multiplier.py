#!/usr/bin/env python3
"""
a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    convert to str & int|float to tuple
    """
    def multiplier_value(mv: float) -> float:
        return mv * multiplier
    return (multiplier_value)
