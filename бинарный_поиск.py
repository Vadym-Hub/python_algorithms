# БИНАРНЫЙ ПОИСК


nums = [5, 7, 6, 9, 8, 4, 2, 3, 1]
nums.sort()  # сортируем
print(nums)

search_for = 9  # что ищем

lowest = 0
highest = len(nums) - 1
index = None  # будущий индекс искомого елемента

while(lowest <= highest) and (index is None):
    # повторяем пока не найдено
    mid = (lowest+highest) // 2  # середина

    if nums[mid] == search_for:
        # нашли по серединке
        index = mid
    else:
        if search_for < nums[mid]:
            # ищем в левой части списка (среза)
            highest = mid - 1
        else:
            # ищем в правой части списка (среза)
            lowest = mid + 1

print('Искомый елемент', search_for, 'находится под ындексом', index)
