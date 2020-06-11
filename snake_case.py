# объявление функции
def convert_to_python_case(text):
    liste = []
    liste.extend(text)
    for i in range(1, len(liste)):
        if liste[i] != liste[i].lower():
            liste.insert(i, '_')
            liste[i + 1] = liste[i + 1].lower()
    snake = ''.join(liste)
    snake = snake.lower()
    return snake

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
