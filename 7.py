"""
Кирилл, Арина и Сергей играют в игру "Аngry Birds".
Их рекорды записываются в одну строку через пробел.
Напишите программу, которая определяет самый лучший результат.
Функцию max() не использовать
"""

scores = input("Введите рекорды игроков :\n")

scores_list = scores.split()
best_score = int(scores_list[0])

for score in scores_list:
    if int(score) > best_score:
        best_score = int(score)

print("Лучший результат: ", best_score)
