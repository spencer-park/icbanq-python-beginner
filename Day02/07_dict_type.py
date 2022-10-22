# 딕셔너리 타입 dict - 값의 의미 기재하기
user_list = ['spencer', 7, 202.2, 10000]  # 이름 나이 키 연봉
user_dict = {'name': 'spencer', 'age': 7, 'height': 202.2, 'salary': 10000}
print(user_dict, '의 타입은 ', type(user_dict))

# 보기 좋게 표현하기
user_dict = {
    'name': 'spencer', 
    'age': 7, 
    'height': 202.2, 
    'salary': 10000
}

# 특정 부분 조회 가능
print(user_dict['name'])
print(user_dict['salary'])

# 특정 부분 접근 후 수정 가능
user_dict['name'] = 'Spencer'
user_dict['salary'] += 5000
print(user_dict)

# 특정 부분 삭제 가능
del user_dict['salary']
print(user_dict)

# 함수로 생성 - 억지로 이렇게 사용하진 않고, 대체로 외부에서 가져온 데이터가 이미 이런 구조일 대 dict()를 사용
user_list = [['name', 'spencer'], ['age', 10], ('height', 230.7)]  # 이중 리스트
user_dict = dict(user_list)
print(user_dict)