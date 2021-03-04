# СОРТИРОВКА ПУЗЫРЬКОМ

nums = [2, 5, 1, 8, 7, 3, 4, 6, 9]
print(nums)


swaps = True
while swaps:
    swaps = False

    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)


# Более оптимизированная версия
for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
