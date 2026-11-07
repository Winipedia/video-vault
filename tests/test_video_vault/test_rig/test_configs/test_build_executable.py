"""Test module."""

from winipyside.rig import resources as winipyside_resources

from video_vault.core.db import migrations
from video_vault.rig import resources as video_vault_resources
from video_vault.rig.configs.build_executable import (
    BuildExecutableConfigFile,
)


class TestBuildExecutableConfigFile:
    """Test class."""

    def test_collect_all_modules(self) -> None:
        """Test method."""
        assert BuildExecutableConfigFile.I.collect_all_modules() == (migrations,)

    def test_collect_data_modules(self) -> None:
        """Test method."""
        assert BuildExecutableConfigFile.I.collect_data_modules() == (
            video_vault_resources,
            winipyside_resources,
        )
