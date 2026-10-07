"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.tools.testing.project import ProjectTester as BaseProjectTester
from winipyside.core.ui.base.base import Base as BaseUI
from winipyside.core.ui.windows.base.base import Base as BaseWindow

from video_vault.core.ui.pages.add_downloads import AddDownloads
from video_vault.core.ui.pages.downloads import Downloads
from video_vault.core.ui.pages.player import Player
from video_vault.core.ui.windows.main import VideoVault
from video_vault.rig.tools.tools import ProjectTester

initial = None
dependencies = None
operations = None
_DJANGO_MIGRATION_CONTRACT = (
    dependencies,
    initial,
    operations,
)
_TOOLS = (ProjectTester,)
_TOOLS_OVERRIDES = (BaseProjectTester.threshold,)
_UI_CLASSES = (
    AddDownloads,
    Downloads,
    Player,
    VideoVault,
)
_UI_FRAMEWORK_CALLBACKS = (
    BaseUI.post_setup,
    BaseUI.pre_setup,
    BaseWindow.get_all_page_classes,
    BaseWindow.get_start_page_cls,
)
