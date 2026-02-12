"""Override pyrig tools."""

from winidjango.rig.tools.tools import ProjectTester as BaseProjectTester
from winidjango.rig.tools.tools import Pyrigger as BasePyrigger
from winipyside.rig.tools.project_tester import ProjectTester as BaseProjectTester2


class Pyrigger(BasePyrigger):
    """Pyrigger class for video_vault."""

    @classmethod
    def dev_dependencies(cls) -> list[str]:
        """Get the dev dependencies."""
        return [
            *super().dev_dependencies(),
            "yt-dlp-types",
        ]


class ProjectTester(BaseProjectTester, BaseProjectTester2):
    """ProjectTester class for video_vault."""
