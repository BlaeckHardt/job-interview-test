class Config:
    ENV = "dev"
    DEBUG = True
    JSON_SORT_KEYS = True
    RESTX_MASK_SWAGGER = False
    CACHE_TYPE = "simple"  
    CACHE_DEFAULT_TIMEOUT = 900

class DevelopmentConfig(Config):
    ENV = "dev"
    JSON_SORT_KEYS = False
    LOG_LEVEL = "DEBUG"

config_by_name = dict(dev = DevelopmentConfig)
