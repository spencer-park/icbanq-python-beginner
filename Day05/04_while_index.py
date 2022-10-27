# list 예시 (01_for_in_list.py) : 반복 기준이 리스트의 요소 개수
texts = ['아', '이', '씨', '뱅', '큐']
for text in texts:
    print(text)


# while 예시 : 목표를 '리스트의 개수만큼 반복한다'로 변환하는 작업 필요
texts = ['아', '이', '씨', '뱅', '큐']
index = 0
while index < len(texts):
    print(texts[index])
    index += 1

print('-'*10)

# 중첩 리스트 for
users = [
    ['스펜서', 500], ['마크', 4000], ['조안', 20]
]
for user in users:
    print(user)
    # print(user[0])


# while 변환
users = [
    ['스펜서', 500], ['마크', 4000], ['조안', 20]
]
index = 0
while index < len(users):
    print(users[index])
    # print(users[index][0])
    index += 1

print('-'*10)

# int-list 예시
numbers = [3, 5, 7, 9, 12]
circles = []
for number in numbers:
    print(number * number * 3.14)
    circles.append(number * number * 3.14)
print(circles)


# while로 변환 > 먼저 print, 이후 append 구현
numbers = [3, 5, 7, 9, 12]
circles = []
index = 0
while index < len(numbers):
    print(numbers[index] * numbers[index] * 3.14)
    circles.append(numbers[index] * numbers[index] * 3.14)
    index += 1
print(circles)