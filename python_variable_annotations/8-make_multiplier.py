#!/usr/bin/env python3
"""Times and times again"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Target Function"""
    return lambda x: x * multiplier
