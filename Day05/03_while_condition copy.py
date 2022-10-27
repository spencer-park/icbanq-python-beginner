# while문의 기본 사용
total = 1
while total < 1024:  # total 1024이상이라는 목표
    total *= 2
print(total)


# while문의 기본 사용 > 몇번 곱했을까?
total = 1
count = 0
while total < 1024:  # total 1024이상이라는 목표
    total *= 2
    count += 1
print(total, count)