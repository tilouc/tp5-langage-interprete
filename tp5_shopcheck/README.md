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
