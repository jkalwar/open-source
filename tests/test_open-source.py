"""Tests for `open-source` package."""

import pytest
import importlib
mod = importlib.import_module("open-source.open-source")


def test_convert(capsys):

    """Correct my_name argument prints"""

    mod.convert("Jill")

    captured = capsys.readouterr()

    assert "Jill" in captured.out