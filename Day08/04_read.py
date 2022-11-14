# WD 변경
import os, time
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

# 상대 경로
fp1 = open('03.txt')  # WD변경시
fp1.close()

# fp2 = open('./Day08/03.txt') # WD 미변경시
# fp2.close()

# 절대 경로
print(__file__)
fp3 = open('/Users/spencerpark/learn/icbanq_python_beginner/Day08/03.txt')  # Mac은 앞에가 Root(/) 위치로 시작
fp3.close()

# read - 한번에 읽기 : str
with open('03.txt') as fp:
    print(fp.read())
    print(fp.tell())  # 현재 커서 위치 확인
    fp.seek(0)  # 커서 위치 옮기기, 영어는 1씩, 한글은 3씩 차지
    print(fp.tell())  # 현재 커서 위치 확인
    print(fp.read())


# readline - 한 줄씩 읽기 : str
print('=' * 10)
with open('03.txt') as fp:
    print(fp.readline())
    print(fp.readline())
    print(fp.readline())

# readlines - 한 번에 + 한 줄씩에 읽고 리스트로 반환 : list
print('=' * 10)
with open('03.txt') as fp:
    print(fp.readlines())
