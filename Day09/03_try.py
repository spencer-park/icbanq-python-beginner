try:
    print("시도 코드")
    n1 = int('3')
    n2 = int('3.0')
except:
    print("오류 발생시 실행되는 영역")
finally:
    print("성공/실패 관련 없이 무조건 실행되는 영역")


# 오류 종류에 따라 제어할 수도 있다.
try:
    int('가')  # ValueError
    int([1, 2, 3])  # TypeError
    1/0  # ZeroDivisionError
except ValueError:
    print('ValueError에 대한 대응')
except TypeError:
    print('TypeError에 대한 대응')
except:
    print('그 외 Error에 대한 대응')
