from pydantic import BaseModel, Field
from datetime import date

class Validador(BaseModel):
    organizador: int = Field(alias="Organizador")
    ano_mes: str = Field(alias="Ano_Mes")
    dia_da_semana: str = Field(alias="Dia_da_Semana")
    tipo_dia: str = Field(alias="Tipo_Dia")
    objetivo: str = Field(alias="Objetivo")
    date: date = Field(alias="Date")
    adset_name: str = Field(alias="AdSet_name")
    amount_spent: float = Field(alias="Amount_spent")
    link_clicks: int = Field(alias="Link_clicks")
    impressions: int = Field(alias="Impressions")
    conversions: int = Field(alias="Conversions")
    segmentacao: str = Field(alias="Segmentação")
    tipo_de_anuncio: str = Field(alias="Tipo_de_Anúncio")
    fase: str = Field(alias="Fase")

