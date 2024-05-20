import json
import time


def questions_from_json(path_of_file):
    with open(path_of_file, encoding='utf-8') as questions_json:
        json_data = questions_json.read()
        python_data = json.loads(json_data)
        easy = python_data[0]['questions'][0]
        medium = python_data[0]['questions'][1]
        hard = python_data[0]['questions'][2]
        knowledge = python_data[1]['levels']
    return easy, medium, hard, knowledge


def save_result(result, username):
    user = username + '_' + str(round(time.time()))
    with open('results\\result_' + user + '.json', 'w', encoding='utf-8') as user_result:
        json_data = json.dumps(result, ensure_ascii=False)
        user_result.write(json_data)


def get_result(answers, knowledge_level_dict):
    true_answers_list = [key for key, value in answers.items() if value]
    false_answers_list = [key for key, value in answers.items() if not value]
    result = knowledge_level_dict[str(len(true_answers_list))]

    print('Верные слова:')
    for word in true_answers_list:
        print(word)

    print()

    print('Неверные слова:')
    for word in false_answers_list:
        print(word)
    return result


def get_user_level(level, words_easy, words_medium, words_hard):
    if level == "средний":
        questions = words_medium
        print('Слова уровня Средний:\n')
    elif level == "тяжелый":
        questions = words_hard
        print('Слова уровня Тяжелый:\n')
    else:
        questions = words_easy
        print('Слова уровня Легкий:\n')
    return questions


def base_program(questions):
    answers = {}
    for word, translation in questions.items():
        print(
            f"Слово: {word}, {len(translation)} букв, первая буква '{translation[:1].upper()}'")
        answer = input("Ваш перевод: ").lower().strip()
        if answer in translation:
            print(f"Правильно! {word} - это {translation}")
            answers[word] = True
        else:
            print(f"Неправильно! {word} - это {translation}")
            answers[word] = False
        print("-----------")
    return answers
