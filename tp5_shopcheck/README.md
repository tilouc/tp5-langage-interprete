# shopcheck

Outil CLI qui lit et valide les commandes du jour de TechShop (CSV), le catalogue fournisseur (JSON) et la configuration (YAML), puis produit `out/rapport.json` et `out/expeditions.csv`.

## Installation

Prérequis : [uv](https://docs.astral.sh/uv/).

```bash
cd tp5_shopcheck
uv sync
```

`uv sync` crée l'environnement virtuel `.venv` et installe les dépendances (`pydantic`, `pyyaml`) à partir de `uv.lock`.

## Lancement

Exécution par défaut (utilise `config.yaml`) :

```bash
uv run python -m shopcheck.main
```

Options :

| Option | Rôle |
| --- | --- |
| `-c`, `--config` | Fichier de configuration (défaut : `config.yaml`) |
| `-i`, `--input` | Remplace le fichier de commandes indiqué dans la configuration |
| `-k`, `--catalogue` | Remplace le catalogue indiqué dans la configuration |

Exemples avec les fichiers invalides :

```bash
uv run python -m shopcheck.main -c config_invalide.yaml
uv run python -m shopcheck.main -i data/commandes_invalide.csv
uv run python -m shopcheck.main -k data/catalogue_invalide.json
uv run python -m shopcheck.main -k data/catalogue_casse.json
```
