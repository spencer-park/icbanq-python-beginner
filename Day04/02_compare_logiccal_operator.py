# 비교 논리 연산자
# 비교 연산자 1 - 값의 비교
exp1 = 3 == 3
exp2 = 3 != 3
exp3 = 3 > 3
exp4 = 3 >= 3
exp5 = 3 < 3
exp6 = 3 <= 3
print(exp1, exp2, exp3, exp4, exp5, exp6)

# 비교 연산자 2 - 주소의 비교
num1 = 2
num2 = 2
print(num1 == num2, num1 is num2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(num1 == num2, num1 is num2)

# 논리 연산자
exp1 = True and True
exp2 = False and True
exp3 = False and False
print(exp1, exp2, exp3)  # True False False

exp1 = True or True
exp2 = False or True
exp3 = False or False
print(exp1, exp2, exp3)  # True True False

exp1 = not True
exp2 = not False
print(exp1, exp2)

# quiz
exp1 = not True and True
exp2 = not False or 5 > 3
exp3 = not False or 5 > 3 + 3
print(exp1, exp2, exp3)  # False True True


# [팁] 타입이 동일한지 확인하는 isistance
exp1 = isinstance(1, int)
exp2 = isinstance(1.0, int)
print(exp1, exp2)