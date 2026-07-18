"""module."""

from video_vault.rig.tools.tools import ProjectTester


class TestProjectTester:
    """Test class."""

    def test_threshold(self) -> None:
        """Test method."""
        assert ProjectTester().threshold() == 50  # noqa: PLR2004
