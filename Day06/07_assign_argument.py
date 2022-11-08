# 함수 생성
def pick(item, ea):
    """무엇을 주웠는지 알려준다"""
    print("나는 '{}' 을/를 '{}'개 주었다.".format(item, ea))


pick('거미줄', 2)
pick(3, '나무판자')
pick(ea = 3, item = '나무판자')


# 응용
def pick(item, ea = 1):
    """무엇을 주웠는지 알려준다"""
    print("나는 '{}' 을/를 '{}'개 주었다.".format(item, ea))

pick('거미줄', 2)
pick('나무판자')
pick(ea = 3, item = '나무판자')
