
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    organization_KEY = "==="
    OPENAI_KEY = '==='
    

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
