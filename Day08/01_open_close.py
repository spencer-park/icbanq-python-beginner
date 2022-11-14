text = """icbanq여러분. 안녕하세요. 스펜서입니다.
파이썬 입문을 하고 있어요.
벌써 8번째 수업이네요."""

# 파일 생성 - 파이썬이 실행되는 위치
# fp = open('01.txt', 'w')  
fp = open('./01.txt', 'w')
fp.write(text)
fp.close()  # 쓰면 꼭 닫아야 합니다.

# 현재 Working Directory 확인
import os
print(os.getcwd())
print()

# WD 변경
import os
print(__file__)
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

# 파일 생성 - WD 변경 후
fp = open('./01.txt', 'w')
fp.write(text)
fp.close()  # 쓰면 꼭 닫아야 합니다.
