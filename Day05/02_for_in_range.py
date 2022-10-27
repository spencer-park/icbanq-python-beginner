# 연속된 숫자 데이터 만드는 range([start], end[, step])
print(list(range(6)))
print(list(range(1, 6)))
print(list(range(1, 6, 2)))

# int - list for 예시
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# range로 표현
for number in range(6):
    print(number)

print('-'*10)

# int - list for 예시
numbers = [1, 3, 5, 7, 9]
for number in numbers:
    print(number)

# range로 표현
for number in range(1, 10, 2):
    print(number)

print('-'*10)

# 구구단
for i in range(1, 10):
    print("{} x {} = {}".format(3, i, 3 * i))


print('-'*10)

# 구구단(전체)
for i in range(1, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i * j))