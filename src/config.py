import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Secrets
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    CLIENT_ID = os.environ.get('CLIENT_ID')

    # Redis
    REDIS_URL = os.environ.get('REDIS_URL')
    REDIS_SECRET = os.environ.get('REDIS_SECRET')
    SESSION_TYPE = 'redis'

    # Local URLs
    REDIRECT_URL = 'http://127.0.0.1:5000/authorize'

    # VATSIM URLs for Dev
    API_URL = 'https://auth-dev.vatsim.net/api/user'
    TOKEN_URL = 'https://auth-dev.vatsim.net/oauth/token'
    AUTH_URL = f'https://auth-dev.vatsim.net/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&response_type=code&scope=full_name+vatsim_details+email+country'

    # # VATSIM URLs for Prod
    # API_URL = 'https://auth.vatsim.net/api/user'
    # TOKEN_URL = 'https://auth.vatsim.net/oauth/token'
    # AUTH_URL = 'https://auth.vatsim.net/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&response_type=code&scope=full_name+vatsim_details+email+country'
