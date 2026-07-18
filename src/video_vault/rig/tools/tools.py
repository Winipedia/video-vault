"""Override pyrig tools."""

from winidjango.rig.tools.tools import ProjectTester as BaseProjectTester
from winipyside.rig.tools.project_tester import ProjectTester as BaseProjectTester2


class ProjectTester(BaseProjectTester, BaseProjectTester2):
    """ProjectTester class for video_vault."""

    def threshold(self) -> int:
        """Override the threshold method to set a custom coverage threshold."""
        return 50
