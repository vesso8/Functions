def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    result = []
    for func_name , nums in args:
        res = func_name(*nums)
        result.append(res)
    return result

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))