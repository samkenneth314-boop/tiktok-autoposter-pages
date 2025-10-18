from flask import Flask, redirect, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

CLIENT_KEY = os.getenv("TIKTOK_CLIENT_KEY")
CLIENT_SECRET = os.getenv("TIKTOK_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

@app.route("/")
def home():
    # Step 1: Redirect user to TikTok login
    auth_url = (
        "https://www.tiktok.com/auth/authorize/"
        f"?client_key={CLIENT_KEY}"
        "&response_type=code"
        "&scope=video.upload,video.publish"
        f"&redirect_uri={REDIRECT_URI}"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    # Step 2: TikTok redirects here with a "code"
    code = request.args.get("code")

    # Step 3: Exchange the code for an access token
    token_url = "https://open-api.tiktok.com/oauth/access_token/"
    data = {
        "client_key": CLIENT_KEY,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
    }
    res = requests.post(token_url, data=data)
    return res.json()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
