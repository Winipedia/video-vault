"""Test module."""

from video_vault.rig.tools.coverage_tester import CoverageTester


class TestCoverageTester:
    """Test class."""

    def test_threshold(self) -> None:
        """Test method."""
        assert CoverageTester().threshold() == 50  # noqa: PLR2004
