"""Database setup module.

This module contains the database settings.
In the init we setup django settings and create the db if not existent.
"""

import logging
import sys
from io import StringIO
from pathlib import Path

import django
from django.conf import settings
from platformdirs import user_data_dir
from winidjango.core.db.setup import migrate_safely

from video_vault.core import db
from video_vault.core.core.consts import APP_NAME, AUTHOR
from video_vault.core.core.security import get_app_key_as_str

logger = logging.getLogger(__name__)


def setup_django() -> None:
    """Setup the database."""
    if settings.configured:
        return

    # can be None in frozen apps and django needs it to be writable
    if sys.stdout is None:
        sys.stdout = StringIO()
    if sys.stderr is None:
        sys.stderr = StringIO()

    root_dir = Path(user_data_dir(APP_NAME, AUTHOR, ensure_exists=True))
    media_root = root_dir / "media"
    media_root.mkdir(parents=True, exist_ok=True)

    db_path = root_dir / "db" / "db.sqlite3"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": str(db_path),
            },
        },
        INSTALLED_APPS=[
            db.__name__,
        ],
        MEDIA_ROOT=media_root,
        MEDIA_URL="/media/",
        SECRET_KEY=get_app_key_as_str(),
    )

    django.setup()

    migrate_safely(db_path)

    logger.info("Django setup complete")
