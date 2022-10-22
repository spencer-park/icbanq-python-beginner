# 리스트 타입
user = ['spencer', 7, 202.2, 10000]  # 이름 나이 키 연봉
print(user, '의 타입은', type(user))

# 문자열과 구조가 비슷하다. 특정 부분만 추출해서 고르거나(index, indexing) 범위 선택(slice, slicing) 할 수 있다
print(user[0])
print(user[1])

print(user[0:2])
print(user[0:3])

# 문자열과 다르게 특정 부분만 골라서 수정하는 것은 가능하다.
user[0] = 'Spencer'
user[3] += 5000
print(user)

# del 연산자로 특정 item 삭제가 가능
del user[3]
print(user)


# list()로 문자열을 리스트로 변환하는 것은 가능
greeting_str = "Hello"
greeting_list = list(greeting_str)
print(greeting_list)

# str()로 리스트로 변환하는 것도 가능은 한데, 기대하고 다름
greeting_str = str(greeting_list)
print(greeting_str)  # '['H', 'e', 'l', 'l', 'o']'

# [팁] 원상복귀하려면 다음 방식을 사용 > 데이터 타입의 함수, 문자열 함수를 배우는 시간에 알아보자
greeting_str = ''.join(greeting_list)
print(greeting_str)