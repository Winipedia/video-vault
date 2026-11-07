"""Configs for pyrig.

All subclasses of ConfigFile in the configs package are automatically called.
"""

from collections.abc import Iterable
from types import ModuleType
from typing import override

from pyrig_executables.rig.configs.build_executable import (  # deptry: ignore[DEP004]
    BuildExecutableConfigFile as BaseBuildExecutableConfigFile,
)
from winipyside.rig import resources

from video_vault.core.db import migrations


class BuildExecutableConfigFile(BaseBuildExecutableConfigFile):
    """You can override methods from the base class to customize behavior."""

    @override
    def collect_all_modules(self) -> Iterable[ModuleType]:
        """Additional resources."""
        return (*super().collect_all_modules(), migrations)

    @override
    def collect_data_modules(self) -> Iterable[ModuleType]:
        """Additional resources."""
        return (*super().collect_data_modules(), resources)
