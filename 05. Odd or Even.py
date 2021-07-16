def odd_or_even(command_type, nums):
    nums_collector = []
    if command_type == "Odd":
        for odd_nums in nums:
            if not odd_nums % 2 == 0:
                nums_collector.append(odd_nums)
    elif command_type == "Even":
        for even_nums in nums:
            if even_nums % 2 == 0:
                nums_collector.append(even_nums)
    return sum(nums_collector) * len(nums)

command = input()
numbers = [int(el) for el in input().split()]
print(odd_or_even(command, numbers))