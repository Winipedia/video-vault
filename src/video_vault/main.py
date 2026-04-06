"""Main entrypoint for the project."""

import logging
import sys

from PySide6.QtWidgets import QApplication

from video_vault.core.ui.stylesheet import STYLESHEET
from video_vault.core.ui.windows.main import VideoVault as VideoVaultWindow
from video_vault.rig.tools.tools import ProjectTester

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entrypoint for the project."""
    run()


def run() -> None:
    """Main function to run the application."""
    # if pytest is running exit with 0 before creating the window
    # to avoid segfaults in headless environments
    if ProjectTester.I.is_running_tests():
        return

    # Create QApplication - this manages the entire app
    app = QApplication(sys.argv)

    # set global style sheet
    app.setStyleSheet(STYLESHEET)

    # Create and show the main window
    window = VideoVaultWindow()

    window.showMaximized()
    # Start the event loop (keeps the app running)
    # This will block until the user closes the window
    logger.info("Starting event loop")
    app.exec()


if __name__ == "__main__":
    main()
