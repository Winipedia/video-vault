"""Configs for pyrig.

All subclasses of ConfigFile in the configs package are automatically called.
"""

from collections.abc import Iterable
from types import ModuleType

from pyrig_executables.rig.configs.remote_version_control.workflows.release import (
    ReleaseWorkflowConfigFile as ExecutablesReleaseWorkflowConfigFile,
)
from winipyside.rig import resources
from winipyside.rig.configs.configs import (
    ReleaseWorkflowConfigFile as WinipysideReleaseWorkflowConfigFile,
)

from video_vault.core.db import migrations


class ReleaseWorkflowConfigFile(
    WinipysideReleaseWorkflowConfigFile, ExecutablesReleaseWorkflowConfigFile
):
    """You can override methods from the base class to customize behavior."""

    def resource_modules(self) -> Iterable[ModuleType]:
        """Additional resources."""
        return (*super().resource_modules(), resources, migrations)
