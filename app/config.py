class Config:
    SECRET_KEY = 'supersecretkey'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    pro=ProductionConfig
)
