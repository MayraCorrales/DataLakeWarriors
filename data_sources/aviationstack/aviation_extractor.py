import requests
import json
from datetime import datetime

API_KEY = "48e8deb8700c52d5f3a9cfe39cfe3ced"

def fetch_aviation_data():
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 100
    }

    response = requests.get(url, params=params)
    data = response.json()

    filename = f"aviation_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Saved: {filename}")

    return filename


if __name__ == "__main__":
    fetch_aviation_data()