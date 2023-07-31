import random # Импортируем библиотеку "Рандом"
from goroda import cities

cities2 = cities # Это список доступных городов
random.shuffle(cities2) # Перемешиваем все города в списке cities2
#bot_answer = cities2.pop() # Бот случайным образом выбирает один из городов в списке доступных городов cities2.
# Функция "pop()" удаляет элемент по указанному индексу и возвращает его. Если индекс не указан, то удаляет и
# возвращает последний элемент. Метод генерирует исключения, если список пуст или указан индекс за пределами диапазона.
bot_answer = random.choice(cities)
print(bot_answer)

user_answer = input ('>>>>>>>>>> ИГРОК: ') # Это ответ игрока
user_answer_r = user_answer[-1]
user_answer_f = user_answer.lower()
user_answer_c = f'{user_answer.upper()[0]}{user_answer.lower()[1:]}'

print(user_answer_r)
print(user_answer_f)
print(user_answer_c)

#bot_answer_r = bot_answer[-1]
#bot_answer_f = bot_answer.lower

def word_in():
    if user_answer.lower()[0] != bot_answer [-1]: # функция "lower" переводит заглавные буквы в прописные. Плюс
        # создано Правило - если первая буква ответа игрока не равна последней букве ответа бота, то:
        print ('Неправильно. город должен начинаться с буквы "' + bot_answer [-1] + '"')
        print()
#        continue

    elif user_answer.lower not in  cities:
        print ('Такого города в России не существует! Попробуйте снова.')
        print()

    elif user_answer not in cities2:
        print ('Такой город уже называли.')
        print()

    else: # Иначе (то есть ели первая буква ответа игрока равна последней букве ответа бота, то:

        print ('Верно!')
        print ('Мне на букву "' + user_answer[-1] + '".')
        print()
        cities2.remove (user_answer) # Убираем ответ игрока из списка доступных городов

        for candidate in cities2: # Создаём переменную "candidate" для ответа бота. Цикл "for" - для переменной
            # "candidate", находящейся в списке доступных городов "cities2"
            if candidate.lower()[0] == user_answer[-1]:  # функция "lower" переводит заглавные буквы в прописные. Плюс
        # создано Правило - если первая буква ответа бота равна последней букве ответа игрока, то:
                bot_answer = candidate # Присваеваем ответу бота переменную "candidate"
                cities2.remove (candidate) # Убираем ответ бота из списка доступных городов "cities2"
                print ('>>>>>>>>>> БОТ: ' + candidate) # Вывод ответа бота
                print ('Вам на букву "' + candidate [-1] + '".')
                print()
                break
        else:
            game_over = True
            print ('Я больше не знаю городов на букву "' + user_answer[-1] + '". Сдаюсь, вы победили!')
