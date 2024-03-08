"""Submodule for C++ test helpers.

This submodule provides functions for:
- Calling C++ functions from within Python.
- Calling C functions from within Python.
"""


from amk_testhelpers.cpp.cpphelpers import (
    callC,
    callCPP,
    callCFunction,
    callCPPFunction
)

__all__ = ['callC', 'callCPP', 'callCFunction', 'callCPPFunction']