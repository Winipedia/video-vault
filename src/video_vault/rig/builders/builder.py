"""Build script.

All subclasses of Builder in the builds package are automatically called.
"""

from collections.abc import Iterator
from itertools import chain
from types import ModuleType

from pyrig.rig.builders.base.executable import ExecutableBuilder

from video_vault import main
from video_vault.core.db import migrations
from video_vault.rig import resources


class VideoVaultBuilder(ExecutableBuilder):
    """Build class for video_vault."""

    def entry_point_module(self) -> ModuleType:
        """Get the entry point module."""
        return main

    def app_icon_png_location(self) -> tuple[str, ModuleType]:
        """Get the location of the app icon."""
        return "icon", resources

    def resource_packages(self) -> Iterator[ModuleType]:
        """Get the resource packages."""
        return chain(super().resource_packages(), (migrations,))
