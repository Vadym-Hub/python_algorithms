# ПЕРЕВОРОТ СТРОКИ


some_string = 'Hello, World!'

def reverse_string(s):
    chars = list(s)  # розбиваем строку на символы

    for i in range(len(s) // 2):
        # до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)

print(some_string)
print(reverse_string(some_string))

# Питонский вариант, самый быстрый и легкий
print(some_string[::-1])