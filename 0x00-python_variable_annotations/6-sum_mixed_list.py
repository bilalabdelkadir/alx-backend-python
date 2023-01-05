#!/usr/bin/env python3
""" Return sum of mixed string """

import math
import typing
from typing import Union


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """ sums mized intergers and floats"""
    return math.fsum(mxd_list)
