from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "an-farmview"
    items_per_user: int = 50
    fno_server: str
    fno_password: str
    snmp_community: str = ''
    snmp_ip: str = ''
    an_farmview_api_url: str = 'empty'

    class Config:
        env_file = ".env"


settings = Settings()