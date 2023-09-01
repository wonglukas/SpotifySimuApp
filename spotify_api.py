from app import app, users_collection, listening_history_collection
import requests

@app.route("/api/listening-history", methods=["GET"])
def fetch_listening_history():
    user_access_token = users_collection.find_one()["access_token"]
    headers = {"Authorization": f"Bearer {user_access_token}"}

    response = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers=headers)
    history_data = response.json()

    tracks = [item["track"]["name"] for item in history_data["items"]]

    # Store the fetched tracks in the database
    listening_history_collection.insert_one({"tracks": tracks})

    return jsonify({"message": "Listening history fetched and stored."})
