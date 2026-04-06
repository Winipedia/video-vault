"""test module."""

import os
import platform
import shutil
from contextlib import chdir
from pathlib import Path

import pytest
from pyrig.core.processes import run_subprocess
from pyrig.rig.tools.package_manager import PackageManager


def test_main() -> None:
    """Test func for main."""


@pytest.mark.skipif(
    platform.system() == "Windows",
    reason="Test fails on Windows due to windows paths in gitub ci",
)
def test_run(tmp_project_root_path: Path, tmp_source_root_path: Path) -> None:
    """Test func for main."""
    # copy the video_vault folder to a temp directory
    # run main.py from that directory

    # shutil video_vault_path to tmp_path
    shutil.copytree(
        PackageManager.I.source_root(), tmp_source_root_path, dirs_exist_ok=True
    )

    files = [
        "pyproject.toml",
        "uv.lock",
        "README.md",
        "LICENSE",
    ]

    for file in files:
        shutil.copy(file, tmp_project_root_path)

    env = os.environ.copy()
    with chdir(tmp_project_root_path):
        # install deps
        run_subprocess(["uv", "sync", "--no-dev"])

        # delete pyproject.toml and uv.lock and readme.md
        for file in files:
            Path(file).unlink()
        # python -m video_vault.main

        run_subprocess(["uv", "run", "-m", "video_vault.main"], env=env)
