"""Test module."""

from winipyside.rig import resources as winipyside_resources

from video_vault.core.db import migrations
from video_vault.rig import resources as video_vault_resources
from video_vault.rig.configs.remote_version_control.workflows.release import (
    ReleaseWorkflowConfigFile,
)


class TestReleaseWorkflowConfigFile:
    """Test class."""

    def test_resource_modules(self) -> None:
        """Test method."""
        assert ReleaseWorkflowConfigFile.I.resource_modules() == (
            video_vault_resources,
            winipyside_resources,
            migrations,
        )
