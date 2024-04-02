# --- Get questions from the Open Trivia Database ---

import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)  # the API endpoint URL
response.raise_for_status()

question_data = response.json()["results"]


