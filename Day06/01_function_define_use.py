# 함수 생성
def pick(item, ea):
    """무엇을 주웠는지 알려준다"""
    print("나는 '{}' 을/를 '{}'개 주었다.".format(item, ea))


def greet(username):
    """아침 인사를 한다"""
    print("안녕하세요! {} 좋은 아침이에요~".format(username))


def clean():
    print("청소를 시작합니다")

# 함수 사용
pick('거미줄', 2)
greet('스펜서')
clean()

# 에러 발생 상황
# pick('거미줄')
# greet('스펜서', '숩휀서')
# clean('우리 집')
# hello()