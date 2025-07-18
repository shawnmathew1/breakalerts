import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HIBP_API_KEY")
BASE_URL = "https://haveibeenpwned.com/api/v3"

HEADERS = {
    "hibp-api-key": API_KEY,
    "user-agent" : "BreakAlertsApp"
}

async def check_breaches(email : str):
    url = f"{BASE_URL}/breachedaccount/{email}?truncateResponse=false"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")



