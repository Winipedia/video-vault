"""Override pyrig tools."""

from pyrig.rig.tools.testing.project import (  # deptry: ignore[DEP004]
    ProjectTester as BaseProjectTester,
)


class ProjectTester(BaseProjectTester):
    """ProjectTester class for video_vault."""

    def threshold(self) -> int:
        """Override the threshold method to set a custom coverage threshold."""
        return 50
