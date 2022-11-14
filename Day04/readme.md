# 사칙연산자
- `+  -  *  /  %` 를 이용한 연산
- `/`  나누기,  `//` 몫,  `%` 나머지
- `*` 곱하기,  `**` 거듭제곱

# 비교연산자
- `==, !=, >, >=, <. <=` 과 `is`
- 전자는 값의 비교
- 후자 is는 주소의 비교
- 자세히는 따로 값 비교, 주소 비교를 다뤄보겠습니다.

# 논리연산자
- `and or not`
- and or : 2개 이상의 참/거짓 결과를 종합하거나
- not : 참/거짓 결과를 반전시키거나

# 파이썬 연산자 우선순위
- 여러 연산자가 한 줄에 있을 경우, 먼저 실행되는 우선순위
- [파이썬 연산자 우선순위](https://docs.python.org/3/reference/expressions.html#operator-precedence)
  1. 거듭제곱 `**`
  2. 사칙연산 `*   /  //  %`
  3. 사칙연산 `+ -`
  4. `is  <  <=  >  >=  !=  ==`
  5. `not`
  6. `and`
  7. `or`

# 불리언(bool) 타입
- 종류 : bool
- 값의 종류 : True, False
- 참과 거짓의 결과를 나타낸다.
- 생성 방법 : True, False 직접 작성, 비교&논리 연산 등의 결과, `bool()`로 변환
- 파이썬의 모든 데이터는 값은 달라도 조건문과 많났을 때(=Bool변환 되었을 때) True 또는 False 중 하나로 변환된다.
- flasy : 거짓으로 인정되는 데이터. 비어있다(0). 없다(None)라는 유형의 값은 False로 처리된다. 나머지는 True로 인정.

# 조건문 - if와 else
- 주어진 상황의 참과 거짓을 판단하여 알맞은 코드를 실행한다.
- block이라는 문법 표기 방법을 사용한다. (Tab 1개 또는 Space 4개 활용)

# 조건문 - elif
- if와 else는 참과 거짓일 경우 2가지를 표현가능하다.
- elif를 사용하면 3가지 이상의 상황을 표현할 수 있다.

# 값 비교와 주소 비교
- 저장된 메모리 주소를 확인 id()
- VSCode, thonny python에서 확인할 수 있고
- pythontutor로 시각적으로 확인할 수도 있다.
- [파이썬 연산자 우선순위](https://docs.python.org/3/reference/expressions.html#operator-precedence)
