numbers = {2, 4, 6, 2, 4, 6}
print(numbers)

# 삽입 add
numbers.add(7)
print(numbers)

# 다른 것 찾기. 빼기와 같은 개념
numbers1 = {1, 2, 3, 4, 5}
numbers2 = {1, 2, 3, 4, 5, 6, 7}
print(numbers1.difference(numbers2))
print(numbers2.difference(numbers1))