from fastapi import FastAPI, Response
from generate_token import generate_token
from pix import  consultar_cobranca,criar_cobranca
from schemas import CriarCobranca

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5000",  # Example frontend origin
    "http://127.0.0.1:5500/",  # Example frontend origin
    "https://your-frontend-domain.com",
]


from fastapi import FastAPI

app = FastAPI(title="Api PIX pagamentos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # Allow cookies and authorization headers
    allow_methods=["*"],     # Allow all HTTP methods
    allow_headers=["*"],     # Allow all headers
)



@app.get("/")
def read_root():
    return "Teste"

@app.get("/token")
def route_token():
    return generate_token()


# @app.post("/cobranca/{txid}")
# def route_cobranca(txid: str, body: CriarCobranca):
#     return criar_cobranca(txid, body.dict())



@app.get("/consulta/{txid}")
def get_cobranca(txid:str):
    print(txid)
    # return txid
    return consultar_cobranca(txid)


@app.post("/gerarCobranca/{txid}")
def generate_cobranca(txid:str,payload:CriarCobranca):
    
    return criar_cobranca(txid=txid,payload=payload)