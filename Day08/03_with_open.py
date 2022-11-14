# with문을 사용하면 close가 자동으로 되는 안전한 코드가 됩니다.

# WD 변경
import os, time
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

text = """icbanq여러분. 안녕하세요. 스펜서입니다.
파이썬 입문을 하고 있어요.
벌써 8번째 수업이네요."""

# with문을 이용한 파일 생성, as(alias, 앨리어스, 별칭)
with open('./03.txt', 'w') as fp:
    fp.write(text)

# 다른 코드 실행 중
while True:
    time.sleep(1)