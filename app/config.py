import os

class Settings:
    DB_USERNAME : str = os.getenv("MYSQL_USER")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
    DB_HOST : str = os.getenv("MYSQL_HOST","db")
    DB_PORT : str = os.getenv("MYSQL_PORT",3306)
    DB_DATABASE : str = os.getenv("MYSQL_DATABASE")	
    DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    NEWS_CLIENT_ID : str = os.getenv("NEWS_CLIENT_ID")
    NEWS_CLIENT_PW : str = os.getenv("NEWS_CLIENT_PW")
    CONSTRUCTION_SERVICE_KEY : str = os.getenv("CONSTRUCTION_SERVICE_KEY")
    GEOCODING_SERVICE_KEY : str = os.getenv("GEOCODING_SERVICE_KEY")

settings = Settings()
