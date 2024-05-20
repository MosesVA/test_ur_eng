import json


def questions_from_json(path_of_file):
    with open(path_of_file, encoding='utf-8') as questions_json:
        json_data = questions_json.read()
        python_data = json.loads(json_data)
    return python_data[0]


path_file = 'questions.json'

print(questions_from_json(path_file))
