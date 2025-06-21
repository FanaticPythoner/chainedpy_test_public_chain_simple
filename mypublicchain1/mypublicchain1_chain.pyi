'''Typed stub file (auto-generated) DO NOT EDIT BY HAND.

This stub allows static analysers (Pyright, Pylance, MyPy) to see dynamically
registered then_* / as_* plugins and custom processors.

Regenerate with:
    chainedpy update-project-pyi --project-path "C:\\Users\\n0_0n\\Documents\\GitHub\\chainedpy_test_public_chain_simple\\mypublicchain1"
'''
# CHANGE: END
from __future__ import annotations
import types
from typing import Any, Awaitable, Callable, TypeVar, overload

from chainedpy.chain import Chain as _BaseChain

_T = TypeVar("_T")
_O = TypeVar("_O")

class Chain(_BaseChain[_T]):  # type: ignore[misc]
    """ChainedPy project: mypublicchain1
    
    This Chain class extends the base ChainedPy Chain with 1 additional plugin(s):
    
    Available then_* plugins:
        - .then_print(...)
    
    """

    def then_print(self, prefix: str = "", suffix: str = "", end: str = "\n") -> Chain[_T]: ...
