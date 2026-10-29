"""Main window module.

This module contains the main window class for the VideoVault application.
"""

from typing import override

from winipyside.core.ui.pages.base.base import Base as BasePage
from winipyside.core.ui.windows.base.base import Base as BaseWindow

from video_vault.core.ui import pages
from video_vault.core.ui.pages.downloads import Downloads as DownloadsPage


class VideoVault(BaseWindow):
    """Main window for the VideoVault application."""

    @classmethod
    @override
    def get_all_page_classes(cls) -> list[type[BasePage]]:
        """Get all page classes."""
        return BasePage.get_subclasses(package=pages)

    @classmethod
    @override
    def get_start_page_cls(cls) -> type[DownloadsPage]:
        """Get the start page class."""
        return DownloadsPage

    @override
    def post_setup(self) -> None:
        """Setup the UI."""

    @override
    def pre_setup(self) -> None:
        """Setup the UI."""
        # set the play icon from winiutils.core
        play_icon = self.get_svg_icon("play_icon")
        self.setWindowIcon(play_icon)

    @override
    def setup(self) -> None:
        """Setup the UI."""
