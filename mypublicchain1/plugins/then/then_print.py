
"""
ChainedPy Plugin: ".then_print()"

WHAT THIS FILE DOES:
    This file defines a ChainedPy plugin that adds a new .then_print() method to Chain objects.
"""

from __future__ import annotations
from typing import TypeVar

from chainedpy.register import then
from chainedpy.link import Link

_T = TypeVar("_T")  # Input type - what goes INTO your plugin


@then("print")  # Registers this function as a chain method named "print" (thus ".then_print()")
def then_print(
    prefix: str = "",
    suffix: str = "",
    end: str = "\n"
) -> Link[_T, _T]:  # Passthrough: input type = output type
    """
    Prints the input value to console and passes it through unchanged.

    This plugin allows you to debug and inspect values in the middle of a chain
    without interrupting the flow of data.

    Args:
        prefix: String to print before the value (default: "")
        suffix: String to print after the value (default: "")
        end: String appended after the last value (default: "\n")

    Returns:
        _T: The input value unchanged (passthrough)

    Example:
        input_data = "Hello World"
        result = await (
            Chain(input_data)
            .then_print(prefix="Debug:", suffix="[END]")
        )
        # Prints: Debug: Hello World [END]
        print(result)  # "Hello World"

    """
    class PrintLink(Link[_T, _T]):  # Implementation class
        """Link implementation for the print plugin."""
        name = "print"  # Plugin name

        async def __call__(self, input_value: _T) -> _T:
            """Print the input value and return it unchanged."""
            # Build the output string
            output_parts = []
            if prefix:
                output_parts.append(prefix)
            output_parts.append(str(input_value))
            if suffix:
                output_parts.append(suffix)

            # Print with the specified parameters
            print(" ".join(output_parts), end=end)

            # Return the input value unchanged (passthrough)
            return input_value
    return PrintLink()  # Return the implementation
