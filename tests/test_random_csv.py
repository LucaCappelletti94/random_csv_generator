"""Tests for the random_csv function."""

from tqdm.auto import trange
from random_csv_generator import random_csv


def test_random_csv():
    """Test the random_csv function."""
    for _ in trange(10):
        random_csv()


def test_random_state_reproducibility():
    """Test that the random state is reproducible."""
    df1 = random_csv(random_state=42)
    df2 = random_csv(random_state=42)
    assert df1.equals(df2)
    df3 = random_csv(random_state=43)
    assert not df1.equals(df3)
    df4 = random_csv(random_state=42)
    assert df1.equals(df4)
    df5 = random_csv(random_state=43)
    assert df3.equals(df5)


def test_different_locale():
    """Test different parametrizations for the locale."""
    random_csv(localization="en_US.UTF-8")
    random_csv(localization="it_IT.UTF-8")
    random_csv(localization=None)
