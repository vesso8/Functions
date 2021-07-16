def even_odd(*args):
    nums_collector = []
    command = args[-1]
    if command == "even":
        for nums in args:
            if nums == "even":
                break
            if nums % 2 == 0:
                nums_collector.append(nums)
    else:
        for nums in args:
            if nums == "odd":
                break
            if not nums % 2 == 0:
                nums_collector.append(nums)
    return nums_collector


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))