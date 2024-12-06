import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')  # Use a strong secret key for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use SQLite for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Set environment variables for sensitive info
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Set environment variables for sensitive info
    UPLOAD_FOLDER = 'uploaded_files'
    ALLOWED_EXTENSIONS = {'pdf', 'xls', 'xlsx', 'csv'}
