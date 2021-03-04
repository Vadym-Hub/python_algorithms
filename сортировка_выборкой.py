# СОРТИРОВКА ВЫБОРКОЙ

nums = [5, 7, 6, 9, 8, 2, 4, 3, 1]

print("Было:", nums)


for i in range(len(nums)):
    lowest = i  # первый елемент примем за найменьший

    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j  # нашли елемент меньше в правом срезе

    nums[i], nums[lowest] = nums[lowest], nums[i]

print("Стало:", nums)
