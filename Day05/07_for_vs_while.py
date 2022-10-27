# 두 가지 차이가 명확히 들어나는 예시
# 원본 데이터의 변경
numbers = [0, 1, -1, 0, 1, -1, 0, 1, -1]
for n in numbers:
    if n < 0:
        n *= -1
print(numbers)


numbers = [0, 1, -1, 0, 1, -1, 0, 1, -1]
index = 0
while index < len(numbers):
    if numbers[index] < 0:
        numbers[index] *= -1
    index += 1
print(numbers)


# 반복 횟수가 불분명 할 때
# 예시 1 : while condition
number = int(input("0을 입력할 때까지 반복 : "))
while number != 0:
    number = int(input("0을 입력할 때까지 반복 : "))
print('종료')


# 예시 2 : while문의 기본 사용 > 몇번 곱했을까?
total = 1
count = 0
while total < 1024:  # total 1024이상이라는 목표
    total *= 2
    count += 1
print(total, count)
