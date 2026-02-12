"""Build script.

All subclasses of Builder in the builds package are automatically called.
"""

from types import ModuleType

from pyrig.rig.builders.pyinstaller import PyInstallerBuilder

from video_vault.src.db import migrations


class VideoVaultBuilder(PyInstallerBuilder):
    """Build class for video_vault."""

    @classmethod
    def additional_resource_packages(cls) -> list[ModuleType]:
        """Get additional resource packages."""
        return [migrations]
