import html

import requests

response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()
data = response.json()

question_data_encoded = data['results']

for dictionary in question_data_encoded:
    del dictionary['incorrect_answers']

question_data = question_data_encoded

for i in range(len(question_data_encoded)):
    for key in question_data_encoded[i]:
        question_data[i][key] = html.unescape(question_data_encoded[i][key])

