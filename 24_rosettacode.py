from operator import mul, sub, add


def div(a, b):
    if b == 0:
        return 999999.0
    return a / b


ops = {mul: '*', div: '/', sub: '-', add: '+'}


def solve24(num, how, target):
    if len(num) == 1:
        if round(num[0], 5) == round(target, 5):
            yield str(how[0]).replace(',', '').replace("'", '')
    else:
        for i, n1 in enumerate(num):
            for j, n2 in enumerate(num):
                if i != j:
                    for op in ops:
                        new_num = [n for k, n in enumerate(num) if
                                   k != i and k != j] + [op(n1, n2)]
                        new_how = [h for k, h in enumerate(how) if
                                   k != i and k != j] + [
                                      (how[i], ops[op], how[j])]
                        yield from solve24(new_num, new_how, target)

"""
tests = [
    [10, 7, 2, 7],
    [5, 7, 5, 4],
    [1, 4, 6, 6],
    [2, 3, 7, 3],
    [1, 6, 2, 6],
    [7, 9, 4, 10],
    [6, 4, 2, 2],
    [5, 7, 9, 7],
    [3, 3, 8, 8],  # Difficult case requiring precise division
    [8, 7, 9, 7],  # No solution
    [9, 4, 4, 5],  # No solution
]
"""
tests = []
nums = []
def get_a():
    valid_a = False
    while not valid_a:
        a = input("Enter first number: ")
        while not a.isdigit():
            a = input("Input is not an integer yo. Enter first number: ")
        a = int(a)
        if a not in range(1, 11):
            print("Bro, your card doesn't exist.")
            valid_a = False
        else:
            valid_a = True
            return int(a)

def get_b():
    valid_b = False
    while not valid_b:
        b = input("Enter second number: ")
        while not b.isdigit():
            b = input("Input is not an integer yo. Enter second number: ")
        b = int(b)
        if b not in range(1, 11):
            print("Bro, your card doesn't exist.")
            valid_b = False
        else:
            valid_b = True
            return int(b)

def get_c():
    valid_c = False
    while not valid_c:
        c = input("Enter third number: ")
        while not c.isdigit():
            c = input("Input is not an integer yo. Enter third number: ")
        c = int(c)
        if c not in range(1, 11):
            print("Bro, your card doesn't exist.")
            valid_c = False
        else:
            valid_c = True
            return int(c)

def get_d():
    valid_d = False
    while not valid_d:
        d = input("Enter fourth number: ")
        while not d.isdigit():
            d = input("Input is not an integer yo. Enter fourth number: ")
        d = int(d)
        if d not in range(1, 11):
            print("Bro, your card doesn't exist.")
            valid_d = False
        else:
            valid_d = True
            return int(d)

a = get_a()
b = get_b()
c = get_c()
d = get_d()
nums.append(a)
nums.append(b)
nums.append(c)
nums.append(d)
tests.append(nums)


for nums in tests:
    print(nums, end=' : ')
    try:
        print(next(solve24(nums, nums, 24)))
    except StopIteration:
        print("No solution found")
