from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    CLIENT_ID: str
    CLIENT_SECRET: str
    TOKEN_URL: str = "https://trust-pix.santander.com.br/oauth/token"

    MTLS_CERT_FILE: str = "client_cert.pem"
    MTLS_KEY_FILE: str = "client_key.pem"
    MTLS_VERIFY: bool  = False

    PIX_BASE_URL: str = "https://trust-pix.santander.com.br"

    class Config:
        env_file = ".env"


settings = Settings()
