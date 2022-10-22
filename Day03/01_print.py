# 출력함수 print의 사용 방법
# print(*values) 출력할 값 인자를 원하는 만큼 입력하기
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, 'a', 'b', 'c', [1, 2, 3])

# print(*values, sep=) 값 사이에 구분자(seperator) 지정. 기본은 ' '
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep='')
print(1, 2, 3, 4, 5, sep='-')

# print(*values, sep=, end=) 출력 마무리에 붙일 문자. 기본 지정은 '\n'
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, end='')
print(1, 2, 3, 4, 5)