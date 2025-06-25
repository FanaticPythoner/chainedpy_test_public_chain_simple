'''Typed stub file (auto-generated) DO NOT EDIT BY HAND.

This stub allows static analysers (Pyright, Pylance, MyPy) to see dynamically
registered then_* / as_* plugins and custom processors.

Regenerate with:
    chainedpy update-project-pyi --project-path "C:/Users/n0_0n/Documents/GitHub/ChainedPy - Copy (2) - Copy/PROJECTS/mypublicchain1"
'''
# CHANGE: START - Enhanced imports for comprehensive type support
from __future__ import annotations
import types
from typing import Any, Awaitable, Callable, TypeVar, overload, Literal

from chainedpy.chain import Chain as _BaseChain

# CHANGE: START - Import all required types for chainedpy methods including Link and Wrapper
from chainedpy.chain import IAutoChained
from chainedpy.plugins.processors import Proc
from chainedpy.link import Link, Wrapper, Processor
# CHANGE: END
# CHANGE: END

# CHANGE: START - Dynamic TypeVar imports from chain hierarchy

from chainedpy.chain import _T  # _T

from chainedpy.chain import _I  # _I

from chainedpy.chain import _O  # _O

from chainedpy.chain import _E  # _E

from chainedpy.chain import _V  # _V

from chainedpy.chain import T_auto  # T_auto

from chainedpy.chain import T_val  # T_val

# CHANGE: END

# CHANGE: START - Enhanced template with clear chain hierarchy delimiters
class Chain(_BaseChain[_T]):  # type: ignore[misc]
    """Public test ChainedPy project named mypublichain1

    This Chain class extends the base ChainedPy Chain with 15 method(s) from the entire chain hierarchy.
    All methods from the entire chain hierarchy are included for proper type checking.

    """

    # ═══════════════════════════════════════════════════════════════════════════════════
    # BASE CHAINEDPY METHODS (always available)
    # ═══════════════════════════════════════════════════════════════════════════════════

    # from chainedpy
    def then_map(self, fn: Callable[[_T], _O | Awaitable[_O]]) -> 'Chain[_O]': ...

    # from chainedpy
    def then_if(self, *, condition: bool | Callable[[IAutoChained[_T]], bool | Awaitable[bool]], then: _O | Callable[[IAutoChained[_T]], _O | Awaitable[_O] | 'Chain[_O]'], otherwise: _O | Callable[[IAutoChained[_T]], _O | Awaitable[_O] | 'Chain[_O]']) -> 'Chain[_O]': ...

    # from chainedpy
    def then_filter(self, predicate: Callable[[IAutoChained[_T]], bool | Awaitable[bool]]) -> 'Chain[_T]': ...

    # from chainedpy
    def then_flat_map(self, fn: Callable[[IAutoChained[_T]], 'Chain[_O]']) -> 'Chain[_O]': ...

    # from chainedpy
    def then_switch(self, *, key: Callable[[IAutoChained[_T]], _I], cases: dict[_I, _O | Callable[[IAutoChained[_T]], _O | Awaitable[_O] | 'Chain[_O]']], default: _O | Callable[[IAutoChained[_T]], _O | Awaitable[_O] | 'Chain[_O]'] | None = None) -> 'Chain[_O]': ...

    # from chainedpy
    def then_foreach(self, *, transform: Callable[[IAutoChained[_E]], _V | Awaitable[_V] | 'Chain[_V]']) -> 'Chain[list[_V]]': ...

    # from chainedpy
    def then_parallel_foreach(self, *, transform: Callable[[IAutoChained[_E]], _V | Awaitable[_V] | 'Chain[_V]'], limit: int | None = None) -> 'Chain[list[_V]]': ...

    # from chainedpy
    def then_reduce(self, *, initial: _O, accumulator: Callable[[_O, IAutoChained[_E]], _O | Awaitable[_O]]) -> 'Chain[_O]': ...

    # from chainedpy
    def then_parallel(self, *chains: 'Chain[object]') -> 'Chain[list[object]]': ...

    # from chainedpy
    def then_process(self, proc: Literal[Proc.STRIP, Proc.UPPER, Proc.LOWER, Proc.B64_ENCODE, Proc.JSON_DUMPS], *, param: str | None = None) -> 'Chain[str]': ...





    # from chainedpy
    def as_retry(self, *, attempts: int = 3, delay: float = 1.0) -> 'Chain[_T]': ...

    # from chainedpy
    def as_timeout(self, seconds: float) -> 'Chain[_T]': ...

    # from chainedpy
    def as_log(self, label: str, *, level: int = 20) -> 'Chain[_T]': ...

    # from chainedpy
    def as_cache(self, *, ttl: float = 60.0) -> 'Chain[_T]': ...

    # from chainedpy
    def as_on_error(self, handler: Callable[[Exception], _T | Awaitable[_T]]) -> 'Chain[_T]': ...




# CHANGE: END
