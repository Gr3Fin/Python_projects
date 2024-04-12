# --- Get questions from the Open Trivia Database ---

import requests


class QuizData:

    def __init__(self):
        parameters = {
            "amount": 1,
            "type": "boolean"}

        response = requests.get(url="https://opentdb.com/api.php", params=parameters)  # the API endpoint URL
        response.raise_for_status()

        self.question_data = response.json()["results"]
