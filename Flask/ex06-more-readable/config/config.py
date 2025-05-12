import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get absolute path of the database file
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'sql', 'app.db')

# Ensure the directory exists
os.makedirs(os.path.join(basedir, 'sql'), exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
