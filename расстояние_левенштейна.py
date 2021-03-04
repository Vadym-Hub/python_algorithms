# РАССТОЯНИЕ ЛЕВЕНШТЕЙНА(РЕДАКЦИОННОЕ НЕТОЧНОЕ СРАВНЕНИЕ СТРОК)


def my_dist(a, b):
    def recursive(i, j):
        if i == 0 or j == 0:
            # если строка пустая, то расстояние равняется ее длинне (n вставок)
            return max(i, j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковые, просто съедаем их
            return recursive(i-1, j-1)
        else:
            # иначе щитаем минимальный вариант
            return 1 + min(
                recursive(i, j-1),  # удаление символа
                recursive(i-1, j),  # вставка символа
                recursive(i-1, j-1),  # замена символа
            )
    return recursive(len(a), len(b))


str1 = "Привет"
str2 = "Приветики"

lev = my_dist(str1, str2)
print("Рассстояние Левенштейна: " + str(lev))

bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100

print(f"""
        Строка №1 : {str1}
        Строка №2 : {str2}
        ====================
        Схожесть : {pct}%
       """)
