#!/usr/bin/env bash
set -o errexit -o nounset -o pipefail

uv \
  run \
  pyinstaller \
  --onefile \
  --name=video-vault-"${OSTYPE}" \
  --icon=src/video_vault/rig/resources/icon.png \
  --collect-all=video_vault.core.db.migrations \
  --collect-data=video_vault.rig.resources \
  --collect-data=winipyside.rig.resources \
  src/video_vault/main.py
