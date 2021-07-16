def rounding_nums(seq):
    return [round(el) for el in seq]

numbers = [float(el) for el in input().split()]

print(rounding_nums(numbers))