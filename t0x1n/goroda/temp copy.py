import random 
from goroda import cities # импортируем список городов из файла

# составляем список городов для игры
cities2 = list(cities) 
# перемешиваем чтоб не выдавать ответы по порядку
random.shuffle(cities2) 

# первый ход бота, рандомно выбирает город и удаляет его из спика городов для игры
bot_answer = cities2.pop()
# форматируем ответ бота - первая заглавная остальные строчные
bot_answer_f = f'{bot_answer.upper()[0]}{bot_answer.lower()[1:]}'
user_answer_f = f'"Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: '

print()
print(bot_answer_f)

user_answer = input(user_answer_f) 
user_answer_f = f'{user_answer.upper()[0]}{user_answer.lower()[1:]}'

def answer():
    print(f'"Верно!"\n"мне на -> "{user_answer.upper()[-1]}" <-"\n')
    cities2.remove(user_answer)
    for candidate in cities2:
        if candidate[0] == user_answer[-1]: 
            bot_answer = candidate 
            print(f'">>> Я отвечу: "{candidate}')
            cities2.remove(candidate)
            break
    else:
        game_over = True
        print(f'"Я больше не знаю городов на букву "{user_answer[-1]}\n"Сдаюсь, вы победили!"')

def check():
    if user_answer.lower()[0] != bot_answer[-1]:
        print(f"{bot_answer_f}'Ответ должен начинаться с буквы '{bot_answer.upper()[-1]}")
        user_answer_f 
#        continue
    elif user_answer not in  cities:
        print(f'"Такого города нет!"\n"Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: "\n')
    elif user_answer not in cities2:
        print(f'"Было! Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: "')
    else: 
        answer()


game_over = False
while not game_over:
    check()

