import csv
import json

import yaml

from shopcheck.models import Catalogue, Commande, Config


def charger_config(chemin: str) -> Config:
    with open(chemin, encoding="utf-8") as f:
        donnees = yaml.safe_load(f)
    return Config.model_validate(donnees)


def charger_catalogue(chemin: str) -> Catalogue:
    with open(chemin, encoding="utf-8") as f:
        donnees = json.load(f)
    return Catalogue.model_validate(donnees)


def lire_commandes(chemin: str) -> list[dict]:
    with open(chemin, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def valider_commandes(lignes: list[dict]) -> list[Commande]:
    return [Commande.model_validate(ligne) for ligne in lignes]
