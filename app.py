from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Read your TikTok keys
CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY")
CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Check that it worked
print("TikTok API keys loaded successfully!")
print("Client Key:", CLIENT_KEY)
print("Redirect URI:", REDIRECT_URI)
