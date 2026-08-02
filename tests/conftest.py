"""Root conftest.

Importing ``video_vault`` runs ``setup_django()`` as a side effect, which
provisions a real Django SQLite database and reads/creates a secret key via
the OS keyring, both under the real user data directory. Under pytest-xdist
every worker is a separate process that imports ``video_vault`` on its own,
so without isolation all workers race on the exact same physical database
file and keyring storage directory (seen in CI as a keyring ``os.makedirs``
``FileExistsError`` and a "django_migrations table already exists" error).

Redirecting both to a private, per-worker temporary directory here runs
before any test module can trigger the import, so every worker gets its own
throwaway database and keyring store instead of sharing one.
"""

import tempfile
from pathlib import Path

import keyring
import platformdirs
from keyrings.alt.file import PlaintextKeyring


def pytest_configure() -> None:
    """Isolate video_vault's app data dir and keyring before it is imported."""
    test_data_dir = Path(tempfile.mkdtemp(prefix="video_vault_test_"))

    platformdirs.user_data_dir = lambda *_args, **_kwargs: str(test_data_dir)  # ty: ignore[invalid-assignment]

    isolated_keyring = PlaintextKeyring()
    isolated_keyring.file_path = str(test_data_dir / "keyring_pass.cfg")  # ty: ignore[invalid-assignment]
    keyring.set_keyring(isolated_keyring)
