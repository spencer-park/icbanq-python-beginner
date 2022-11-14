# WD 변경
import os
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

# load_data
load_data = [
    ('학생1', 100),
    ('학생2', 90),
    ('학생3', 70),
]

# 템플릿
greeting_message = """{}님 안녕하십니까.
담당자 스펜서입니다.
국가시험 OOO의 결과를 안내해드립니다.
감사합니다.
점수 : {}"""

# 성적표 파일 생성
for m in load_data:
    username = m[0]
    score = m[1]
    filename = "./{} 결과표.txt".format(username)  # 파일 경로까지 포함해서 만들자
    
    # 메세지 생성
    new_message = greeting_message.format(username, score)
    print(new_message)
    
    # 파일 생성
    with open(filename, 'w') as fp:
        fp.write(new_message)
