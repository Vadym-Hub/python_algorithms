# ВЫЧЕСЛЕНИЕ ФАКТОРИАЛА
# Произведение всех натуральных чисел, меньше или равныx n.
# Факториал обозначается n! n!=1⋅2⋅3…(n−1)⋅n.

number = 5

# Метод рекурсии
# (рекурсия не может вызвать сама себя больше 1000 раз)
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

print("Факториал числа {n} равен {f}".format(n=number, f=factorial(number)))


# Метод цыклом
def factorial(n):
    if n == 0:
        return 1

    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i
    return f
print("Факториал числа {n} равен {f}".format(n=number, f=factorial(number)))
print(factorial(10))