def get_duplicates_numbers(numbers: list[int]) -> list[int]:
    """Get a list with duplicate elements.

    :param numbers: list[int]
    :return: list[int]
    """
    result = []
    for num in numbers:
        if (numbers.count(num) > 1) and (num not in result):
            result.append(num)
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 2, 4, 5]
    print(get_duplicates_numbers(nums))  # [1, 2]
    print(get_duplicates_numbers([1, 2, 3, 4, 5]))  # []

    # Second variant
    print(list(set([x for x in nums if nums.count(x) > 1])))  # [1, 2]
    
