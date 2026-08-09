"""Configs for pyrig.

All subclasses of ConfigFile in the configs package are automatically called.
"""

from collections.abc import Iterable
from types import ModuleType

from pyrig_executables.rig.configs.version_control.remote.workflows.release import (  # deptry: ignore[DEP004]  # noqa: E501
    ReleaseWorkflowConfigFile as BaseReleaseWorkflowConfigFile,
)
from winipyside.rig import resources

from video_vault.core.db import migrations


class ReleaseWorkflowConfigFile(
    BaseReleaseWorkflowConfigFile,
):
    """You can override methods from the base class to customize behavior."""

    def resource_modules(self) -> Iterable[ModuleType]:
        """Additional resources."""
        return (*super().resource_modules(), resources, migrations)
