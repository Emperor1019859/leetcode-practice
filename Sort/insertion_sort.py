numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(numbers: list[int]) -> list:
    temp_nums = [next(iter(numbers))]

    for idx in range(1, len(numbers)):
        current_idx = 0
        while numbers[idx] > temp_nums[current_idx]:
            if current_idx < len(temp_nums) - 2:
                current_idx += 1
            else:
                current_idx = len(temp_nums)
                break
        temp_nums.insert(current_idx, numbers[idx])

    return temp_nums


result = insertion_sort(numbers)
print(result)
