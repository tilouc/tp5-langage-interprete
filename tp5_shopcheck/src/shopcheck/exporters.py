import csv
import json
import os
from datetime import datetime

from shopcheck.models import Catalogue, Commande, Config


def calculer_rapport(commandes: list[Commande], catalogue: Catalogue, config: Config) -> dict:
    ht = sum(c.quantite * c.prix_unitaire for c in commandes if c.statut != "annulee")
    tva = ht * config.tva
    par_statut = {"payee": 0, "expediee": 0, "annulee": 0}
    for c in commandes:
        par_statut[c.statut] += 1
    return {
        "genere_le": datetime.now().isoformat(timespec="seconds"),
        "nb_commandes": len(commandes),
        "chiffre_affaires": {
            "ht": round(ht, 2),
            "tva": round(tva, 2),
            "ttc": round(ht + tva, 2),
        },
        "par_statut": par_statut,
        "alertes_stock": [
            {"ref": p.ref, "stock": p.stock}
            for p in catalogue.produits
            if p.stock < config.seuil_alerte_stock
        ],
    }


def exporter_rapport_json(rapport: dict, chemin: str) -> None:
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(rapport, f, indent=2, ensure_ascii=False)


def exporter_expeditions_csv(commandes: list[Commande], chemin: str) -> None:
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    colonnes = ["id_commande", "client_email", "ref", "quantite"]
    with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(
            c.model_dump(include=set(colonnes)) for c in commandes if c.statut == "payee"
        )
