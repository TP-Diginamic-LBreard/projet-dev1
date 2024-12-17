from datetime import date as Date
from typing import Optional
from pydantic import BaseModel

from src.models import Commande as CommandeModel


class PartialCommande(BaseModel):
    date: Optional[Date] = None
    client: Optional[int] = None
    timbre_client: Optional[float] = None
    timbre_commande: Optional[float] = None
    nombre_colis: Optional[int] = None
    cheque: Optional[float] = None
    conditionnement: Optional[int] = None
    # cdeComt = ???
    arg1: Optional[str] = None
    # barchive = ???
    arg2: Optional[int] = None
    # bstock = ???
    arg3: Optional[int] = None


    def merge_model(self, model: CommandeModel) -> CommandeModel:
        if self.date:
            model.datcde = self.date

        if self.client:
            model.codcli = self.client

        if self.timbre_client:
            model.timbrecli = self.timbre_client

        if self.timbre_commande:
            model.timbrecde = self.timbre_commande

        if self.nombre_colis:
            model.nbcolis = self.nombre_colis

        if self.cheque:
            model.cheqcli = self.cheque

        if self.conditionnement:
            model.idcondit = self.conditionnement

        if self.arg1:
            model.cdeComt = self.arg1

        if self.arg2:
            model.barchive = self.arg2

        if self.arg3:
            model.bstock = self.arg3

        return model


class Commande(PartialCommande):
    date: Date
    client: int
    timbre_client: float
    timbre_commande: float
    cheque: float

    @classmethod
    def from_model(cls, model: CommandeModel) -> 'Commande':
        return cls(
            date            = model.datcde if model.datcde else Date.fromtimestamp(0),
            client          = model.codcli,
            timbre_client   = model.timbrecli if model.timbrecli else 0,
            timbre_commande = model.timbrecde if model.timbrecde else 0,
            nombre_colis    = model.nbcolis,
            cheque          = model.cheqcli if model.cheqcli else 0,
            conditionnement = model.idcondit,
            arg1            = model.cdeComt,
            arg2            = model.barchive,
            arg3            = model.bstock,
        )


    def to_model(self) -> CommandeModel:
        return CommandeModel(
            datcde    = self.date,
            codcli    = self.client,
            timbrecli = self.timbre_client,
            timbrecde = self.timbre_commande,
            nbcolis   = self.nombre_colis,
            cheqcli   = self.cheque,
            idcondit  = self.conditionnement,
            cdeComt   = self.arg1,
            barchive  = self.arg2,
            bstock    = self.arg3
        )


class FullCommande(Commande):
    id: int

    @classmethod
    def from_model(cls, model: CommandeModel) -> 'FullCommande':
        return cls(
            id              = model.codcde,
            date            = model.datcde if model.datcde else Date.fromtimestamp(0),
            client          = model.codcli,
            timbre_client   = model.timbrecli if model.timbrecli else 0,
            timbre_commande = model.timbrecde if model.timbrecde else 0,
            nombre_colis    = model.nbcolis,
            cheque          = model.cheqcli if model.cheqcli else 0,
            conditionnement = model.idcondit,
            arg1            = model.cdeComt,
            arg2            = model.barchive,
            arg3            = model.bstock,
        )


    def to_model(self) -> CommandeModel:
        return CommandeModel(
            codcde    = self.id,
            datcde    = self.date,
            codcli    = self.client,
            timbrecli = self.timbre_client,
            timbrecde = self.timbre_commande,
            nbcolis   = self.nombre_colis,
            cheqcli   = self.cheque,
            idcondit  = self.conditionnement,
            cdeComt   = self.arg1,
            barchive  = self.arg2,
            bstock    = self.arg3
        )
