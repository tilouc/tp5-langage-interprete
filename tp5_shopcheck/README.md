# tp5_shopcheck

## installation

prérequis : [uv](https://docs.astral.sh/uv/).

```bash
cd tp5_shopcheck
uv sync
```

## lancement

```bash
uv run python -m shopcheck.main
```

options :

| option | rôle |
| --- | --- |
| `-c`, `--config` | fichier de configuration (défaut : `config.yaml`) |
| `-i`, `--input` | remplace le fichier de commandes indiqué dans la configuration |
| `-k`, `--catalogue` | remplace le catalogue indiqué dans la configuration |
