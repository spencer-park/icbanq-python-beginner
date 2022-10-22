# 셋 타입 - 중복이 없는 데이터 관리 구조
number_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
number_set = {1, 1, 1, 2, 2, 2, 3, 3, 3}
print(number_list, number_set)

# 특정 부분만 추출해서 고르거나(index, indexing) 범위 선택(slice, slicing)이 '불가'하다
# print(number_set[0])
# print(number_set[0:1])

# 리스트, 튜플, 문자열의 변환이 가능하다.
basket_list = ['apple', 'apple', 'banana', 'banana', 'coconut']
basket_set = set(basket_list)
print(basket_set)

text = "aaabbbcccddd"
text_set = set(text)
print(text_set)