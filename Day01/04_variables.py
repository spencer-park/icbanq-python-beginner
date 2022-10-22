# 변수 사용 방법
name = "Spencer"
age = 7
salary = 10000  # 달러

# 한 살을 더 먹었다.
age = age + 1
print(age)

# 또 한 살을 더 먹었다.
age += 1
print(age)

# 개명을 했다.
name = "Dispencer"
print(name)

# 일을 쉬기로 했다.
salary = 0
print(salary)

# 다시 일을 시작했다.
salary = 20000
print(salary)

# 연봉 변수를 삭제 했다.
del salary
# print(salary)


# 변수의 이름 규칙
# 숫자가 먼저 나올 수 없다.
# 1major = 'Computer'
# 2major = 'Science'

major1 = 'Computer'
major2 = 'Science'

# 특수문자는 _만 허용한다.
_gravity = 9.8
gravity_earth = 9.8

# print를 변수로 사용한다면 print()함수를 사용할 수 없다. > 색도 다르고 Ctrl+클릭으로 찾아봐도 다르다.
print = "뺏어야지!"
print(print)

# 파이썬에서 변수와 함수는 CapWord보단 snake_case를 권장한다.
GravityEarth = 9.8  # CapWord
gravity_earth = 9.8  # snake_case
