import random # импортируем модуль для рандомайза
from list import cities # импортируем список городов России

cities2 = list(cities) # создаём список городов для игры
random.shuffle(cities2) # перемешиваем список для игры в рандомном порядке

bot_answer = cities2.pop() # первый ходит. Программа называет рандомный город и исключает его из списка игры
bot_answer_f = f'{bot_answer.upper()[0]}{bot_answer.lower()[1:]}' # Форматирует ответ бота чтобы город был с заглавной буквы
print()
print(bot_answer_f)
print(f'"Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: ') # запрашиваем у игрока город 

game_over = False # условие для цикла

while not game_over: # запускаем цикл
    user_answer = input() # ответ игрока 
    user_answer_f = f'{user_answer.upper()[0]}{user_answer.lower()[1:]}' # форматируем ответ игрока
    if user_answer.lower()[0] != bot_answer[-1]: # если первая буква ответа не равна последней загаданного слова
        print(f"'был назван город '{bot_answer_f}'\nОтвет должен начинаться с буквы '{bot_answer.upper()[-1]}") # поясняем что не прав
        continue # повторяем вопрос
    elif not user_answer in cities: # если ответа нет в списке горобов России
        print(f'"Такого города нет!"\n"Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: "\n')
    elif not user_answer in cities2: # если ответ уже был
        print(f'"Было! Тебе на -> "{bot_answer.upper()[-1]}" <-"\n" >> Ваш ответ: "')
    else: # если ответ удовлетврояет условия
        print(f'"Верно!"\n"мне на -> "{user_answer.upper()[-1]}" <-"\n')
        cities2.remove(user_answer) # удаляем ответ пользователя из списка городов для игры
        for candidate in cities2: # подбираем город ядл ответа 
            if candidate[0] == user_answer[-1]: 
                bot_answer = candidate 
                cities2.remove(candidate) # удаляем выбранный город из списка игры
                print(f'">>> Я отвечу: "{candidate.upper()[0]}{candidate.lower()[1:]}" Тебе на -> "{candidate.upper()[-1]}" <-"\n" >> Ваш ответ: ')
                break
        else: # если нет городов на нужную букву
            game_over = True # конец игры
            print(f'"Я больше не знаю городов на букву "{user_answer[-1]}\n"Сдаюсь, вы победили!"')
                
