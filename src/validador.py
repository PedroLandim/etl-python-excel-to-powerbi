from pydantic import BaseModel, model_validator, Field
from typing import Literal
from datetime import date


class Campanha(BaseModel):
    organizador: int = Field(alias="Organizador")
    ano_mes: str = Field(alias="Ano_Mes")
    dia_da_semana: str = Field(alias="Dia_da_Semana")
    tipo_dia: str = Field(alias="Tipo_Dia")
    objetivo: str = Field(alias="Objetivo")
    data: date = Field(alias="Date")
    adset_name: str = Field(alias="AdSet_name")
    amount_spent: float = Field(positive=True, alias="Amount_spent")
    link_clicks: int | Literal[""] = Field(alias="Link_clicks")
    impressions: int = Field(alias="Impressions")
    conversions: int | Literal[""] = Field(alias="Conversions")
    segmentacao: str = Field(alias="Segmentação")
    tipo_de_anuncio: str = Field(alias="Tipo_de_Anúncio")
    fase: str = Field(alias="Fase")



    @model_validator(mode='after')
    def validador_regras_negocios(self):

        if self.amount_spent < 0:
            raise ValueError("Amount_spent não pode ser negativo")

        if self.link_clicks != "":
            if self.link_clicks > self.impressions:
                raise ValueError("Link_clicks não pode ser maior que Impressions")

        if self.conversions != "" and self.link_clicks != "":
            if self.conversions > self.link_clicks:
                raise ValueError("Conversions não pode ser maior que Link_clicks")
        return self



