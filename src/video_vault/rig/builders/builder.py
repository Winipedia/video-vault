"""Build script.

All subclasses of Builder in the builds package are automatically called.
"""

from collections.abc import Generator
from types import ModuleType

from pyrig.core.iterate import combine_generators
from pyrig.rig.builders.pyinstaller import PyInstallerBuilder

from video_vault import main
from video_vault.core.db import migrations
from video_vault.rig import resources


class VideoVaultBuilder(PyInstallerBuilder):
    """Build class for video_vault."""

    def entry_point_module(self) -> ModuleType:
        """Get the entry point module."""
        return main

    def app_icon_png_location(self) -> tuple[str, ModuleType]:
        """Get the location of the app icon."""
        return "icon", resources

    def resource_packages(self) -> Generator[ModuleType, None, None]:
        """Get the resource packages."""
        return combine_generators(super().resource_packages(), (migrations,))
