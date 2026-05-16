"""Coverage testing wrapper for the code coverage tool.

Wraps CoverageTester commands and information.
"""

from pyrig.rig.tools.coverage_tester import CoverageTester as BaseCoverageTester


class CoverageTester(BaseCoverageTester):
    """You can override methods from the base class to customize behavior."""

    def threshold(self) -> int:
        """Override the threshold method to set a custom coverage threshold."""
        return 50
