"""module."""

from video_vault.rig.tools.tools import ProjectTester, Pyrigger


class TestPyrigger:
    """Test class."""

    def test_dev_dependencies(self) -> None:
        """Test method."""
        result = Pyrigger().dev_dependencies()
        assert "yt-dlp-types" in result


class TestProjectTester:
    """Test class."""

    def test_threshold(self) -> None:
        """Test method."""
        assert ProjectTester().threshold() == 50  # noqa: PLR2004
