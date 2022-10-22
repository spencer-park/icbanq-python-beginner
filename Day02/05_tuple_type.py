# 튜플 타입 - 리스트와 구조는 같으나 특정 부분의 수정이 불가능 하다는 것이 다르다.
user = ('spencer', 7, 202.2, 10000)  # 이름 나이 키 연봉
print(user, '의 타입은', type(user))

# 문자열과 구조가 비슷하다. 특정 부분만 추출해서 고르거나(index, indexing) 범위 선택(slice, slicing) 할 수 있다
print(user[0])
print(user[1])

print(user[0:2])
print(user[0:3])

# 문자열과 다르게 특정 부분만 골라서 수정하는 것은 가능하다.
# user[0] = 'Spencer'
# user[3] += 5000

# 리스트, 문자열 변환이 가능하다.
greeting_str = 'Hello'
greeting_tuple = tuple(greeting_str)
print(greeting_tuple)

basket_list = ['apple', 'banana', 'coconut']
basket_tuple = tuple(basket_list)
print(basket_tuple)