import qrcode
import httpx
from io import BytesIO
from settings import settings
from schemas import CriarCobranca
from generate_token import generate_token
from fastapi.exceptions import HTTPException

def criar_cobranca(txid: str, payload: CriarCobranca) -> dict:
    token = generate_token()["access_token"]

    url = f"{settings.PIX_BASE_URL}/api/v1/cob/{txid}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with httpx.Client(
        cert=(settings.MTLS_CERT_FILE, settings.MTLS_KEY_FILE),
        verify=settings.MTLS_VERIFY,
        timeout=30
    ) as client:
        try:
            resp = client.put(url, headers=headers, json=payload.model_dump())
            resp.raise_for_status()
            print(resp.json())
            return resp.json()
        
        except(Exception) as e: 
            raise HTTPException( 409,f"Já existe uma cobrança com este TXID.{e}")
        
        



def consultar_cobranca(txid: str) -> dict:
    """
    Consulta individual de cobrança PIX (Swagger: /api/v1/cob/{txid})
    """
    token = generate_token()["access_token"]

    url = f"{settings.PIX_BASE_URL}/api/v1/cob/{txid}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with httpx.Client(
        cert=(settings.MTLS_CERT_FILE, settings.MTLS_KEY_FILE),
        verify=settings.MTLS_VERIFY,
        timeout=30
    ) as client:
        resp = client.get(url, headers=headers)
        resp.raise_for_status()
        print(resp.json()["status"])
        print(resp.json()["location"])

        return resp.json()




if __name__ == "__main__":
#     payload = {
#    "calendario": {
#    "expiracao": "85400"
#     },
    
#     "devedor": {
#     "cnpj": "19221229000184",
#     "nome": "Angela"
#     },
#     "valor": {
#     "original": "10.00"
#     },
#     "chave": "+5531998762834",
#     "solicitacaoPagador": "Cobrança dos serviços prestados.",
#     "infoAdicionais": [
#     {
#     "nome": "AAA",
#     "valor": "Valor9"
#     }
#     ]
#     }
    # passou
    # print(consultar_cobranca("EX29000000000000000000000000127")) 
    print(criar_cobranca(txid="EX29000000000000000000000000131",
                         payload={
  "calendario": { "expiracao": "85400" },
  "devedor": { "cnpj": "19221229000184", "nome": "Angela" },
  "valor": { "original": "10.00" },
  "chave": "+5531998762834",
  "solicitacaoPagador": "Cobrança dos serviços prestados.",
  "infoAdicionais": [
    { "nome": "AAA", "valor": "Valor9" }
  ]
}
))