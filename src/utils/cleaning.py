"""Fonctions de nettoyage de données."""

import pandas as pd


def load_and_clean(filepath: str) -> pd.DataFrame:
    """Charge et nettoie un fichier CSV."""
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df


def handle_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Supprime les colonnes avec trop de valeurs manquantes."""
    return df.dropna(thresh=len(df) * threshold, axis=1)


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Supprime les doublons."""
    return df.drop_duplicates()
