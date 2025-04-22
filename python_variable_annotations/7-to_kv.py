#!/usr/bin/env python3
"""you need me to do what...?"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Im anticipating this wont pass because of inexact output"""
    return (k, float(v ** 2))
