numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(numbers: list[int]):
    def merge(left: list, right: list):
        result = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        return result + left[left_index:] + right[right_index:]

    if len(numbers) == 1:
        return numbers

    # split array info left and right
    middle_index = int(len(numbers) / 2)
    left = numbers[:middle_index]
    right = numbers[middle_index:]

    return merge(merge_sort(left), merge_sort(right))


result = merge_sort(numbers)
print(result)
