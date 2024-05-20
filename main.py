from utils.utils import *

print("Добро пожаловать в приложение проверки знания английского языка!")

user_name = input('Введите Ваше имя: ')
user_level = input("Выберите уровень сложности (легкий, средний, тяжелый): ").lower().strip()

path_questions_file = 'questions.json'
words_easy, words_medium, words_hard, knowledge_level = questions_from_json(path_questions_file)

level_questions = get_user_level(user_level, words_easy, words_medium, words_hard)
user_answers = base_program(level_questions)
end_result = get_result(user_answers, knowledge_level)

print()
print(f'Ваш ранг: {end_result}')

save_result(user_answers, user_name)
