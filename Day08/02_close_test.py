# open()이 되면 close()는 반드시 해줘야합니다.
# 1. 프로그램 실행 도중에 해당 파일이 다른 곳에서 읽어질 필요가 있다거나
# 2. 여러 프로그램이 돌던 도중 오류로 open() 된 상태로 종료될 경우. 해당 파일에 접근 못하는 상태가 될 수도 있습니다.
# 3. 기술 발전이 되어 예외상황이 있긴 하지만, 기본적으로 파일은 작업 데이터 손상/유실을 막기위해 하나의 접근 상태만 허용합니다. 
# 4. 관련 이미지로는 파일 = 팩으로 된 음료수. 파일객체 = 빨대. 팩 음료수엔 하나만 꽂을 수 있다.

# WD 변경
import os, time
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

text = """icbanq여러분. 안녕하세요. 스펜서입니다.
파이썬 입문을 하고 있어요.
벌써 8번째 수업이네요."""

# 파일 생성
fp = open('./02.txt', 'w')
fp.write(text)
# fp.close()  # 쓰면 꼭 닫아야 합니다.

# 다른 코드 실행 중
while True:
    time.sleep(1)