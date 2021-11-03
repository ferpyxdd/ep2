class Config(object):
    SECRET_KEY = 'd\x14$]*\xc8+\xfa\x1b\xf2/\x06\xbe2\xdf\xae\x02\xdfG\x83\xaeeY\xfc'

class ConfiguracionDesarrollo(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ilsigniore@localhost/tcpw2_4601365'
    SQLALCHEMY_TRACK_MODIFICATIONS = False