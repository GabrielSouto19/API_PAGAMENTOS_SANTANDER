# API PAGAMENTOS SANTANDER

## Instruções 

### Clonar o repositório
Abra o seu editor de código em uma pasta separada para os próximos passos

Para clonar o repositório, abra seu terminal com ctrl + j e dê o comando:

`
git clone https://github.com/GabrielSouto19/API_PAGAMENTOS_SANTANDER
`

Ainda no terminal dê o comando:

`
cd API_PAGAMENTOS_SANTANDER
`
## Configurações de SETUP 

- Criar um ambiente virtual

No ambiente Windows
`
python -m venv .venv
`
- Ativação do ambiente virtual

`
.venv\Scripts\activate
` 

- Instalação de dependencias 

`
pip install requirements.txt
` 

### Configurações de Ambiente
- Renomear o .env.example para .env
- Substiuir para as suas credenciais de acesso reais 

### Rodar o projeto

No terminal, digite o comando

`
uvicorn main:app --reload
`
