# 숫자 타입은 int, float, complex_type
from types import AsyncGeneratorType


age = 7
print(age, '의 타입은', type(age))

score = 88.7
print(score, '의 타입은', type(score))

polar_coordinate = 1-2j  # +-를 띄어쓰지 않도록 주의
print(polar_coordinate, '의 타입은', type(polar_coordinate))


# 함수를 통한 생성
age = int(7)
score = float(88.7)
polar_coordinate = complex(1, -2)
print(type(age), type(score), type(polar_coordinate))


# 함수를 통한 형 변환(숫자->숫자)
age = int(7.0)
score = float(88)
polar_coordinate = complex(age)
print(age, score, polar_coordinate)
print(type(age), type(score), type(polar_coordinate))


# 함수를 통한 형 변환(글자->숫자)
age = int('7')
print(age, type(AsyncGeneratorType))
# age = int('7.0')  # ValueError. 10진법 수를 넣어달라!

score = float('88')
print(score, type(score))

score = float('88.7')
print(score, type(score))