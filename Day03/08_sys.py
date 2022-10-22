# 시스템 관련 모듈
import sys

# 터미널에서 입력한 인자 값 사용하기
# 실행 시 명령어 python3 08_sys.py spencer 7 202.2
print(sys.argv)
print(sys.argv[0], type(sys.argv[0]))
print(sys.argv[1], type(sys.argv[1]))
print(sys.argv[2], type(sys.argv[2]))
print(sys.argv[3], type(sys.argv[3]))
# print(sys.argv[4], type(sys.argv[4]))  # IndexError: list index out of range