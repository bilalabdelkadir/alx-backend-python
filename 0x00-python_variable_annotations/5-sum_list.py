#!/usr/bin/env python3
""" takes a list of inputs and returns as floats"""

import math
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ takes list inputs and returns the floats """
    return math.fsum(input_list)
