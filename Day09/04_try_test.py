# try를 이용한 최대 시도 횟수 코드
# if문과 비슷하지만 조건이 True/False 인가? 오류 발생인가?

# 최대 시도 횟수 5번 제한 코드
age = -1
attempt = 0
while attempt < 5:
    attempt += 1  # finally로 빼도 된다.
    try:
        age = int(input("나이를 입력해주세요(정수) : "))
        break
    except:
        print("올바른 값이 아닙니다. 시도횟수 : {}".format(attempt))
print("프로그램 종료")