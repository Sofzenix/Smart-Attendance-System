import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "smartface_super_secret_key")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_URI = os.path.join(BASE_DIR, "database", "smartface.db")
    
    # Mail Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME", "noreply@smartface.local")
