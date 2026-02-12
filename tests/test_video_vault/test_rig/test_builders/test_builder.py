"""module."""

from video_vault.rig.builders.builder import VideoVaultBuilder
from video_vault.src.db import migrations


class TestVideoVaultBuilder:
    """Test class."""

    def test_additional_resource_packages(self) -> None:
        """Test method."""
        assert VideoVaultBuilder.additional_resource_packages() == [migrations]
