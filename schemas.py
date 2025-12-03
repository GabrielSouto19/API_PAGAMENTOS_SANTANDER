from pydantic import BaseModel
from typing import List, Optional


class Calendario(BaseModel):
    expiracao: str   # o PIX aceita string ou número


class Devedor(BaseModel):
    cnpj: str
    nome: str


class Valor(BaseModel):
    original: str


class InfoAdicional(BaseModel):
    nome: str
    valor: str


class CriarCobranca(BaseModel):
    calendario: Calendario
    devedor: Devedor
    valor: Valor
    chave: str
    solicitacaoPagador: Optional[str] = None
    infoAdicionais: Optional[List[InfoAdicional]] = None
