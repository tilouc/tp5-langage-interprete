import datetime
from typing import Literal

from pydantic import BaseModel, Field


class Commande(BaseModel):
    id_commande: int = Field(gt=0)
    date: datetime.date
    client_email: str
    ref: str
    quantite: int = Field(ge=1, le=100)
    prix_unitaire: float = Field(gt=0)
    statut: Literal["payee", "expediee", "annulee"]


class Dimensions(BaseModel):
    largeur_cm: float = Field(gt=0)
    hauteur_cm: float = Field(gt=0)


class Produit(BaseModel):
    ref: str
    nom: str
    prix: float = Field(gt=0)
    stock: int = Field(ge=0)
    categories: list[str] = []
    dimensions: Dimensions | None = None


class Catalogue(BaseModel):
    fournisseur: str
    mise_a_jour: datetime.date
    produits: list[Produit]


class Config(BaseModel):
    commandes: str
    catalogue: str
    sortie: str = "out"
    tva: float = Field(default=0.20, ge=0, le=1)
    seuil_alerte_stock: int = Field(default=5, ge=0)
