# ЛИНЕЙНЫЙ ПОИСК

names = ['Володя', 'Валера', 'Вася', 'Саша', 'Антон', 'Яков']

search_for = 'Антон'  # что ищем

def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # возвращаем индекс

    return None  # или None если не найдено

print('Искомый елемент', search_for, 'найден под индексом', linear_search(names, search_for))
