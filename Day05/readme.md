# 영상 분량 조절
- 영상 실습 코드는 01, 02, 03, 05, 08만 진행

# 반복문
반복문은 크게 for와 while이 있습니다.
for는 반복할 개수가 명확할 때 + 반복이 횟수(개수)가 주요점일 때,
while은 반복할 횟수가 명확하지 않을 때 + 반복이 달성할 목표 수치/값이 주요점일 때

# for 반복문
반복할 개수가 명확할 때 + 반복할 횟수가 주 목적일 때
예시로 리스트의 개수만큼 반복하자는 반복할 개수도 명확하고 반복의 기준이 개수(횟수)이다.

자주 사용하는 패턴
```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
```

```python
for i in range(6):
    print(i)
```


# while 반복문
```python
numbers = [0, 1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index])
```

```python
total = 1
while total < 1024 :
    total *= 2
print(total)
```

# (생략) for-while 비교
for는 가능한게 while도 가능하다.
하지만 while가능한 게 for는 불가능한 경우가 있다.
또한 반복에 사용된 원본데이터를 바꿀 때는 while이 쓰인다.


# 제어문 명령어 - break, continue, pass
프로그램 로직의 구현 = 반복문 for, while + 조건문 if elif else + 명령어 pass, break, continue

