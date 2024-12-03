from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./config/conf.env",
        extra="ignore"
    )


class DBConfig(Config):
    db_host: str
    db_port: str
    db_name: str
    db_username: str
    db_password: str
    db_table_name: str

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_table_name}"


# class DBConfig(Config):
#     db_name: str
#     table_name: str

#     @property
#     def database_url(self):
#         return f"sqlite+aiosqlite:///{self.db_name}"


db_config = DBConfig()
