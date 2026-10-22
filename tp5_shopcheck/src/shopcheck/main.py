import argparse
import os

from shopcheck.exporters import calculer_rapport, exporter_expeditions_csv, exporter_rapport_json
from shopcheck.loaders import charger_catalogue, charger_config, lire_commandes, valider_commandes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", type=str, default="config.yaml")
    parser.add_argument("-i", "--input", type=str)
    parser.add_argument("-k", "--catalogue", type=str)
    args = parser.parse_args()

    config = charger_config(args.config)
    catalogue = charger_catalogue(args.catalogue or config.catalogue)
    commandes = valider_commandes(lire_commandes(args.input or config.commandes))
    rapport = calculer_rapport(commandes, catalogue, config)

    print(f"[OK] {len(commandes)} commandes validees")
    for alerte in rapport["alertes_stock"]:
        print(f"[ALERTE] stock bas : {alerte['ref']} ({alerte['stock']} en stock)")
    ca = rapport["chiffre_affaires"]
    print(f"Chiffre d'affaires : {ca['ht']:.2f} EUR HT / {ca['ttc']:.2f} EUR TTC")

    chemin_rapport = os.path.join(config.sortie, "rapport.json")
    chemin_expeditions = os.path.join(config.sortie, "expeditions.csv")
    exporter_rapport_json(rapport, chemin_rapport)
    exporter_expeditions_csv(commandes, chemin_expeditions)
    print(f"Rapport : {chemin_rapport}")
    print(f"Expeditions : {chemin_expeditions}")


if __name__ == "__main__":
    main()
