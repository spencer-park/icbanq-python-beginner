# 시간 제어 모듈 time
import time

# 현재 시간 정보 확인하기
print(time.localtime())
print(time.localtime().tm_year)

# 일시 정지
print('Stop 1s')
time.sleep(1)
print('Go')

print('Stop 0.5')
time.sleep(.5)  # 0.5
print('Go')

# [팁] 시간 차이 계산하기
print(time.time(), type(time.time()))  # 1970년 1월 1일 00:00 (UTC)부터 지난 시간

start = time.time()
time.sleep(.3)
end = time.time()
print(end - start)