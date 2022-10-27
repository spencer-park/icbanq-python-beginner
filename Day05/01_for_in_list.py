# list 예시
texts = ['아', '이', '씨', '뱅', '큐']
for text in texts:
    print(text)


# str 예시
texts = '아이씨뱅큐'
for text in texts:
    print(text)


# 중첩 리스트
users = [
    ['스펜서', 500], ['마크', 4000], ['조안', 20]
]
for user in users:
    print(user)
    # print(user[0])


# int-list 예시
numbers = [3, 5, 7, 9, 12]
for number in numbers:
    print(number * number * 3.14)


# int-list 예시
numbers = [3, 5, 7, 9, 12]
circles = []
for number in numbers:
    print(number * number * 3.14)
    circles.append(number * number * 3.14)
print(circles)