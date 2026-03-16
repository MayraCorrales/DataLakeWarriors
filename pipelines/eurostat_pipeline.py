import requests
import json

# Example Eurostat dataset
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/une_rt_m"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("eurostat_data.json", "w") as f:
        json.dump(data, f)

    print("Data downloaded successfully")

else:
    print("Error downloading data")
