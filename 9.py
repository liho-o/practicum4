"""
Напишите программу, которая задает пользователю вопросы, на которые
 он отвечает "да" или "нет". По результатам ответов на вопросы, программа должна
определить породу собаки. Разработайте программу по представленному ниже
дереву решений.
"""

if input('Собака короткошерстной породы?') == "да":
    if input('Рост собаки менее 50 см?') == "да":
        if input('У собаки короткий хвост?') == "да":
            print("английский бульдог")
        else:
            if input('У собаки длинные уши?') == "да":
                print("гончая")
            else:
                if input('У собаки короткое тело?') == "да":
                    print("мопс")
                else:
                    print("чихухуа")
    else:
        if input('Собака весит более 50 кг?') == "да":
            print("Датский дог")
        else:
            print("Фоксхаунд")
else:
    if input('Рост собаки менее 50 см?') == "да":
        if input('У собаки доброжелательный характер?') == "да":
            print("Кокер спаниэль")
        else:
            print("Ирландский сеттер")
    else:
        if input('У собаки рост менее 70 см?') == "да":
            if input('У собаки длинные уши?') == "да":
                print("Большой вандейский грифон")
            else:
                print("Колли")
        else:
            if input('Окрас рыжий с белыми отметинами?') == "да":
                print("Сенбернар")
            else:
                if input('Белоснежный окрас?') == "да":
                    print("Ирландский волкодав")
                else:
                    print("ньюфаундленд")
