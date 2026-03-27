"""Build script.

All subclasses of Builder in the builds package are automatically called.
"""

from collections.abc import Generator
from types import ModuleType

from pyrig.rig.builders.pyinstaller import PyInstallerBuilder
from pyrig.src.iterate import combine_generators

from video_vault import main
from video_vault.src.db import migrations


class VideoVaultBuilder(PyInstallerBuilder):
    """Build class for video_vault."""

    def entry_point_module(self) -> ModuleType:
        """Get the entry point module."""
        return main

    def resource_packages(self) -> Generator[ModuleType, None, None]:
        """Get the resource packages."""
        return combine_generators(super().resource_packages(), (migrations,))
