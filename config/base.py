from pydantic import BaseSettings


class Settings(BaseSettings): 
    BROKER_HOST: str
    BROKER_PORT: int
    BROKER_USER: str
    BROKER_VHOST: str
    BROKER_PASS: str
    BROKER_QUEUE: str
    BROKER_ROUTE: str
    BROKER_EXCHANGE: str
    BROKER_QUEUE_INGEST: str
    BROKER_QUEUE_ROUTE_INGEST: str
    NUM_WORKER: int
    
    API_REQUEST: str

    ELASTIC_HOST: str
    ELASTIC_INDEX: str
    
    ELASTIC_KBN5_HOST: str
    ELASTIC_KBN5_INDEX: str

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str
    REDIS_PASS: str

    BROKER_QUEUE_NOT_FOUND: str
    BROKER_ROUTE_NOT_FOUND: str

    class Config: 
        env_file = '.env'

settings = Settings()
