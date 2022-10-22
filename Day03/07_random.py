# 랜덤과 난수 관련 모듈
import random

# 난수 생성
print(random.random())  # 0~1 float
print(random.randint(0, 255))  # 0~255 int
print(random.uniform(0, 255))  # 0~255, float

# 리스트와 랜덤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice = random.choice(numbers)
print(choice)

sample = random.sample(numbers, 3)
print(sample)

# 섞기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
random.shuffle(numbers)
print(numbers)
random.shuffle(numbers)
print(numbers)