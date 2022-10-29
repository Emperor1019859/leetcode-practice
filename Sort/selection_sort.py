numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(numbers: list[int]):
    numbers_copy = numbers.copy()
    ans = []

    for _ in range(len(numbers_copy)):
        min = next(iter(numbers_copy))
        for num in numbers_copy:
            if num < min:
                min = num
        ans.append(min)
        related_idx = numbers_copy.index(min)
        numbers_copy.pop(related_idx)

    return ans


result = selection_sort(numbers)
print(result)
