nums = [1, 4, 6, 8, 9, 10]


def count_evens(nums):
    new_nums = [1 for items in nums if items % 2 == 0]
    return sum(new_nums)
