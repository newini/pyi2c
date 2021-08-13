#!/bin/env python3
# -*- coding: utf-8 -*-
# tests/getBit.py
"""
Test getBit function
"""

from pyi2c import getBit

byte = 0x5a
print( bin(byte) )
print(
        getBit(byte, 7),
        getBit(byte, 6),
        getBit(byte, 5),
        getBit(byte, 4),
        getBit(byte, 3),
        getBit(byte, 2),
        getBit(byte, 1),
        getBit(byte, 0)
        )
