"""module."""

from video_vault.rig.tools.tools import Pyrigger


class TestPyrigger:
    """Test class."""

    def test_get_dev_dependencies(self) -> None:
        """Test method."""
        result = Pyrigger.get_dev_dependencies()
        assert "yt-dlp-types" in result


class TestProjectTester:
    """Test class."""
