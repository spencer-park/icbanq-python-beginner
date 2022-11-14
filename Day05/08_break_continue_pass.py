# pass : 아무것도 안하는 명령어. 일단 영역만 잡고 넘기자(pass)
for i in range(1, 10):
    if i % 3 == 0:
        pass  # 3의 배수 일 때 무엇을 할 지 영역만 확보


# continue : 음.. 일단 이번 차례는 넘기고 다음 차례 계속해(continue)
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)

print('-'*10)

# break : 헉. 멈춰! 중지! 부셔!(break)
for i in range(1, 10):
    if i % 3 == 0:
        break
    print(i)


print('-'*10)


# 369게임 50까지
for i in range(1, 50):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print('짝')
    else:
        print(i)

print('-'*10)

# 369게임 50까지 - continue 이용해서
for i in range(1, 50):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print('짝')
        continue
    print(i)

print('-'*10)

# 보석 찾기
items = ['돌1', '나무1', '돌2', '보석', '나무2', '독사1']
basket = []
for i in items:
    print('{}을/를 찾았다'.format(i))
    if i == '보석':
        basket.append(i)
        break
print(basket)

print('-'*10)

items = ['돌1', '나무1', '돌2', '보석', '나무2', '보석']
basket = []
for i in items:
    print('{}을/를 찾았다'.format(i))
    if i == '보석':
        basket.append(i)
print(basket)
    
