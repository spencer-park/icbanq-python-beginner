from datetime import datetime, timedelta, timezone

# 현재 시간
now = datetime.now()
print(now, type(now))

# 세계별 : 독일 시간 UTC+1, 한국 시간 UTC+9
de_tz = timezone(timedelta(hours=1))
de_now = datetime.now(tz=de_tz)
print(de_now, now)  # 독일, 한국


# 특정 시각 - 특정 시각 = 시간차(timedelta)
future = datetime(2100, 1, 1)
interval = future - now
print(interval, type(interval))

# 시간차
pray_period = timedelta(days=1000, hours=2)
finish_day = now + pray_period
print(finish_day, type(finish_day))

# 시간 원하는 포맷(문자열)
print('{}:{}'.format(now.hour, now.minute))
date1 = now.strftime("%Y %m %d %p %I %H %M %S %A")
date2 = now.strftime("%Y년 %m월 %d일 %p %I:%M:%S %a")  # 낮은 버전의 Python에선 한글 섞을 시 오류
date3 = now.strftime("%Y{} %m{} %d{} %p %I:%M:%S %a").format('년', '월', '일')
print(date1)
print(date2)
print(date3)