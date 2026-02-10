"""Connexions base de données."""

import yaml
from pathlib import Path


def get_connection_string(env: str = "development") -> str:
    """Retourne la chaîne de connexion pour l'environnement."""
    config_path = Path(__file__).parents[2] / "config" / "database.yaml"

    with open(config_path) as f:
        config = yaml.safe_load(f)

    db = config[env]
    return f"postgresql://{db['user']}@{db['host']}:{db['port']}/{db['database']}"
