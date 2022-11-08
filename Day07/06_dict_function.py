user_dict = {'name': 'spencer', 'age': 7, 'height': 202.2, 'salary': 10000}

# key만, value만 모아서 보기
print(user_dict.keys())
print(user_dict.values())
print(list(user_dict.keys()))
print(list(user_dict.values()))

# item 단위로 튜플로 모아서 보기
print(user_dict.items())
print(list(user_dict.items()))

# items()를 이용한 for문
for key, value in user_dict.items():
    print("{}의 값은 {}입니다.".format(key, value))