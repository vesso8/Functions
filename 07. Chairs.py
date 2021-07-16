# from itertools import combinations
#
# result = list(combinations(input().split(", "), int(input())))
# for x , y in result:
#     print(x, y , sep= ", ")

def combination(name, count, current_names=[]):
    if len(current_names) == count:
        print(', '.join(current_names))
        return
    for i in range(len(name)):
        current_names.append(name[i])
        combination(name[i+1:], count,current_names)
        current_names.pop()

names = input().split(", ")
n = int(input())
combination(names,n)