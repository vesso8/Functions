def even_nums(nums):
    if int(nums) % 2 == 0:
        return True
    return False

numbers = [int(el) for el in input().split()]
even_numbers_sep = filter(even_nums,numbers)
print(list(even_numbers_sep))
