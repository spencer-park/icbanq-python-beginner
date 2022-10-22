# 입력 함수 input()
# 기본 사용 방법
name = input()
age = input("당신의 나이는? : ")
print(name, age, type(name), type(age))

# 숫자를 입력 -> 형 변환
age = int(input("당신의 나이는? : "))
print(age, type(age))

# 여러 개를 입력 -> 문자열 함수 .split()
basket = input("구매한 물품 목록 : ").split()
print(basket)

# [팁] 여러 숫자를 입력 -> 문자열 함수 .split() -> 리스트 각 value에 대해서 형변환 map(int, 리스트) -> list()
score = input("국가시험 점수는 : ").split()
print(score)

score = list(map(int, input("국가시험 점수는 : ").split()))
print(score)
print(sum(score)/len(score))
