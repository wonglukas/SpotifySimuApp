from app import app, users_collection, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SPOTIFY_AUTH_URL, SPOTIFY_TOKEN_URL
from urllib.parse import urlencode
import requests

@app.route("/auth")
def authenticate_spotify():
    auth_query_parameters = {
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": "user-read-private user-read-email user-top-read",
        "client_id": CLIENT_ID,
    }
    auth_url = f"{SPOTIFY_AUTH_URL}?{urlencode(auth_query_parameters)}"
    return redirect(auth_url)

@app.route("/auth/callback")
def spotify_callback():
    code = request.args.get("code")
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    response = requests.post(SPOTIFY_TOKEN_URL, data=token_data)
    token_info = response.json()

    # Store the access token in the database
    users_collection.insert_one({"access_token": token_info["access_token"]})

    return "Authentication successful. You can now close this window."
