from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
        )

config = Settings()