"""module."""

from video_vault.rig.tools.tools import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_dev_dependencies(self) -> None:
        """Test method."""
        result = Pyrigger.dev_dependencies()
        assert "yt-dlp-types" in result


class TestProjectTester:
    """Test class."""
