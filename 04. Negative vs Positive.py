def separate_positive(numbers):
    positive = []
    for nums in numbers:
        if nums >= 0:
            positive.append(nums)
    return sum(positive)

def separate_negative(numbers):
    negative = []
    for nums in numbers:
         if nums < 0:
            negative.append(nums)
    return sum(negative)

nums = [int(el) for el in input().split()]
print(separate_negative(nums))
print(separate_positive(nums))
if abs(separate_negative(nums)) > separate_positive(nums):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")