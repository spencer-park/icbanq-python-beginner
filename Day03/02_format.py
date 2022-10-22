# format을 통해 변수 값을 문자열에 넣기
student = "김OO"
school = "아이씨뱅큐"
principal = "스펜서"

# 기본 사용 방법
text = "안녕하십니까 {} 학부모님 저는 {} 교장 {}입니다."
text = text.format('김OO', '아이씨뱅큐', '스펜서')
print(text)

# 변수와 기본 사용 방법
text = "안녕하십니까 {} 학부모님 저는 {} 교장 {}입니다."
print(text.format(student, school, principal))

# (예습) 나중에 배울 반복문과 학생 리스트를 함께
students = ["김OO", "이OO", "박OO", "곽OO"]
school = "아이씨뱅큐"
principal = "스펜서"
text = "안녕하십니까 {} 학부모님 저는 {} 교장 {}입니다."

for student in students:
    print(text.format(student, school, principal))


# {0} {1} 과 {변수명1} {변수명2}를 활용
student = "김OO"
school = "아이씨뱅큐"
principal = "스펜서"
text = "안녕하십니까 {0} 학부모님 저는 {1} 교장 {2}입니다. {0}가 우수한 성적을 거두었습니다."
print(text.format(student, school, principal))

student = "김OO"
school = "아이씨뱅큐"
principal = "스펜서"
text = "안녕하십니까 {a} 학부모님 저는 {b} 교장 {c}입니다. {a}가 우수한 성적을 거두었습니다."
print(text.format(a = student, b = school, c = principal))

text = "안녕하십니까 {student} 학부모님 저는 {school} 교장 {principal}입니다. {student}가 우수한 성적을 거두었습니다."
print(text.format(student = student, school = school, principal = principal))