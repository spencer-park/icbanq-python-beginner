# 글자 타입은 str 이다. 파이썬에선 '글자'보단 '문자열'이라고 부른다
name = "Spencer"
lang = 'Python'
profile_comment = """안녕하세요 스펜서입니다.
저는 파이썬에 관심이 있습니다.
읽어주셔서 감사합니다."""

print(name, '의 타입은', type(name))
print(lang, '의 타입은', type(lang))
print(profile_comment)


# 함수로 생성 및 변환
birth_year = 2002
birty_day = 1225
print(birth_year + birty_day)  # 3227

birth_year = str(birth_year)
birty_day = str(birty_day)
print(birth_year + birty_day)  # 20021225


# 특정 부분만 추출해서 고르거나(index, indexing) 범위 선택(slice, slicing) 할 수 있다
greeting_message = "Hello Python! Hello icbanq!"  # 총 27자.
print(greeting_message[0])
print(greeting_message[1])
print(greeting_message[-1])
print(greeting_message[-2])

print(greeting_message[0:1])
print(greeting_message[0:2])
print(greeting_message[2:5])

# Quiz - 'Hello icbanq!' 만 출력하려면?
print(greeting_message[14:27])
print(greeting_message[14:])  # 끝까지는 생략가능

# Quiz - 'Hello Python!' 만 출력하려면?
print(greeting_message[0:13])
print(greeting_message[:13])

# Step을 줄 수도 있다. [start:end:step]
text = "a1Ab2Bc3Cd4D"
print(text[0:12:3])
print(text[1:12:3])
print(text[2:12:3])

# 특정 부분만 골라서 수정하는 것은 불가
# greeting_message[1] = 'a'  # 문자열은 item 할당(값 삽입 및 교체)를 지원하지 않는다
