# Data Analyst Project Template

Structure de projet professionnelle pour data analysts.

> Fini les `analyse_finale_v3_VRAIFINAL.ipynb`

## Pourquoi cette structure ?

- **30 secondes** pour retrouver n'importe quelle analyse
- **Zéro copier-coller** entre notebooks
- **Prêt à industrialiser** quand on te le demande

## Structure

```
├── config/          # Connexions DB et paramètres centralisés
├── data/
│   ├── raw/         # Données brutes (jamais modifiées)
│   └── processed/   # Données nettoyées
├── notebooks/
│   ├── exploration/ # Analyses exploratoires
│   └── reporting/   # Rapports récurrents
├── sql/             # Requêtes versionnées et commentées
├── src/
│   ├── utils/       # Fonctions de nettoyage
│   └── viz/         # Fonctions de visualisation
├── tests/           # Tests unitaires
├── outputs/
│   ├── reports/     # Rapports générés
│   └── figures/     # Graphiques exportés
└── docs/            # Documentation
```

## Quick Start

```bash
# Cloner le repo
git clone https://github.com/gpenessot/data-analyst-template.git
cd data-analyst-template

# Installer les dépendances
pip install -e ".[dev]"

# Configurer les credentials
cp .env.example .env

# Lancer les tests
make test

# Ouvrir Jupyter
make run-notebook
```

## Commandes disponibles

| Commande | Description |
|----------|-------------|
| `make install` | Installer les dépendances |
| `make test` | Lancer les tests |
| `make lint` | Vérifier le code |
| `make format` | Formater le code |
| `make run-notebook` | Ouvrir Jupyter |

## Fichiers clés

| Fichier | Rôle |
|---------|------|
| `pyproject.toml` | Dépendances + config linting (standard moderne) |
| `Makefile` | Automatisation des tâches courantes |
| `.env.example` | Template pour les credentials |
| `.gitignore` | Exclut data, outputs, secrets |

---

## Aller plus loin

Ce template est un extrait de ce qu'on construit dans le **Productive Python Bootcamp** :

- 4 semaines pour passer de "je sais coder" à "je sais livrer"
- Stack moderne : uv, DuckDB, CI/CD, GitHub Actions
- Un projet déployé avec données réelles (25M+ lignes)

👉 [Découvrir le bootcamp](https://www.mes-formations-data.fr/formation/bootcamp)

---

## Licence

MIT - Utilise ce template comme tu veux.
