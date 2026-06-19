# video-vault

<!-- security -->
[![DependencyAuditor](https://img.shields.io/badge/security-pip--audit-blue?logo=python)](https://github.com/pypa/pip-audit)
[![SecurityChecker](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
<!-- ci/cd -->
[![CI](https://img.shields.io/github/actions/workflow/status/Winipedia/video-vault/health_check.yml?label=CI&logo=github)](https://github.com/Winipedia/video-vault/actions/workflows/health_check.yml)
[![CD](https://img.shields.io/github/actions/workflow/status/Winipedia/video-vault/deploy.yml?label=CD&logo=github)](https://github.com/Winipedia/video-vault/actions/workflows/deploy.yml)
<!-- code-quality -->
[![DependencyChecker](https://img.shields.io/badge/dependencies-deptry-blue)](https://github.com/osprey-oss/deptry)
[![MarkdownLinter](https://img.shields.io/badge/markdown-rumdl-darkgreen)](https://github.com/rvben/rumdl)
[![PythonLinter](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![SpellChecker](https://img.shields.io/badge/spell--check-typos-blue)](https://github.com/crate-ci/typos)
[![TypeChecker](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![VersionControlHookManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)
<!-- testing -->
[![CoverageTester](https://img.shields.io/badge/coverage->=50%25-hsl(60,80%25,45%25)?logo=codecov&logoColor=white)](https://github.com/pytest-dev/pytest-cov)
[![ProjectTester](https://img.shields.io/badge/tested%20with-pytest-46a2f1.svg?logo=pytest)](https://pytest.org)
<!-- tooling -->
[![PackageManager](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Pyrigger](https://img.shields.io/badge/built%20with-pyrig-3776AB?logo=buildkite&logoColor=black)](https://github.com/Winipedia/pyrig)
[![RemoteVersionController](https://img.shields.io/github/stars/Winipedia/video-vault?style=social)](https://github.com/Winipedia/video-vault)
[![VersionController](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)
<!-- documentation -->
[![DocsBuilder](https://img.shields.io/badge/MkDocs-Documentation-326CE5?logo=mkdocs&logoColor=white)](https://www.mkdocs.org)
[![Documentation](https://img.shields.io/badge/Docs-GitHub%20Pages-black?style=for-the-badge&logo=github&logoColor=white)](https://Winipedia.github.io/video-vault)
<!-- project-info -->
[![ExecutableBuilder](https://img.shields.io/github/downloads/Winipedia/video-vault/total?logo=github&label=downloads)](https://github.com/Winipedia/video-vault/releases)
[![ProgrammingLanguage](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/github/license/Winipedia/video-vault)](https://github.com/Winipedia/video-vault/blob/main/LICENSE)

---

> An application to download any video

---

## Features

- **Download videos**
  from any platform (YouTube, Vimeo, etc.) using an embedded browser
- **Encrypted storage** with AES-GCM encryption for all downloaded videos
- **Built-in video player**
  with automatic position tracking and resume functionality
- **Cross-platform** support (Windows, macOS, Linux)
- **Dark theme** UI inspired by Netflix

## Installation

### Requirements

- Python 3.12 or 3.13
- [uv](https://github.com/astral-sh/uv) package manager

### Install

```bash
uv pip install video-vault
```

### Run

```bash
video-vault
```

## Quick Start

1. **Launch the application**
   - The Downloads page will open showing your video library
2. **Download a video**:
   - Click the "+" button in the top-right corner
   - Navigate to any video URL in the embedded browser
   - Click the download button (arrow icon)
   - Wait for the download and encryption to complete
3. **Play a video**:
   - Click on any video in your library
   - Select "Play" from the menu
   - The video will resume from where you left off

## Documentation

For more detailed information, see the [documentation](docs/index.md):

- [User Guide](docs/user-guide.md) - How to use the application
- [Development Guide](docs/development.md) - How to contribute and develop

## Security

All downloaded videos are encrypted using AES-GCM encryption.
Encryption keys are stored securely in your system's keyring:

- **macOS**: Keychain
- **Windows**: Credential Manager
- **Linux**: Secret Service

## Tech Stack

- **UI Framework**: PySide6 (Qt for Python)
- **Video Download**: yt-dlp
- **Video Processing**: FFmpeg (bundled via imageio-ffmpeg)
- **Database**: Django ORM with SQLite
- **Encryption**: AES-GCM via cryptography library

## License

See [LICENSE](LICENSE) file for details.
