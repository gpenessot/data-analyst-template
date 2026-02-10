"""Tests pour les fonctions de nettoyage."""

import pandas as pd
import pytest
from src.utils.cleaning import handle_missing, remove_duplicates


def test_remove_duplicates():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [3, 3, 4]})
    result = remove_duplicates(df)
    assert len(result) == 2


def test_handle_missing():
    df = pd.DataFrame({"a": [1, None, None], "b": [1, 2, 3]})
    result = handle_missing(df, threshold=0.5)
    assert "a" not in result.columns
    assert "b" in result.columns
