# def abs_values(nums):
#     values = [abs(float(el)) for el in nums]
#     return values
#
# numbers = input().split()
# print(abs_values(numbers), sep=", ")


def make_absolute(seq):
    return [abs(el) for el in seq]

nums = [float(el) for el in input().split()]
print(make_absolute(nums))