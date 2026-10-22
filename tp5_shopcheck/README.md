# tp5_shopcheck

## Installation

Prérequis : [uv](https://docs.astral.sh/uv/).

```bash
cd tp5_shopcheck
uv sync
```

## Lancement

```bash
uv run python -m shopcheck.main
```

Options :

| Option | Rôle |
| --- | --- |
| `-c`, `--config` | Fichier de configuration (défaut : `config.yaml`) |
| `-i`, `--input` | Remplace le fichier de commandes indiqué dans la configuration |
| `-k`, `--catalogue` | Remplace le catalogue indiqué dans la configuration |

Exemples :

```bash
uv run python -m shopcheck.main -c config_invalide.yaml
uv run python -m shopcheck.main -i data/commandes_invalide.csv
uv run python -m shopcheck.main -k data/catalogue_invalide.json
uv run python -m shopcheck.main -k data/catalogue_casse.json
```
