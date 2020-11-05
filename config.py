import os

class Config:
    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:w1nj3k4@localhost/blogs'
    SECRET_KEY =os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   

    #  email configurations
  
    


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:w1nj3k4@localhost/blogs'
    


class TestConfig(Config):
    
    DEBUG = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:w1nj3k4@localhost/blogs'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
