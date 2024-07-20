"""Tests for the package version."""

from validate_version_code import validate_version_code
from random_csv_generator.__version__ import __version__


def test_version():
    """Test the package version."""
    assert validate_version_code(__version__)
