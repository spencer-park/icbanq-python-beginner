# 수학 관련 모듈
import math

# 수학 관련 값(변수)
print(math.pi)
print(math.e)

# 삼각함수
print(math.sin(30))  # 기대한 값 1/2, 라디안 값으로 입력 된 것

deg_30 = math.pi / 6
print(math.sin(deg_30))
print(round(math.sin(deg_30), 1))

deg_30 =  math.radians(30)
print(math.sin(deg_30))
print(round(math.sin(deg_30), 1))

# 로그함수
print(math.log(math.e))
print(math.log10(100))
print(math.log2(8))