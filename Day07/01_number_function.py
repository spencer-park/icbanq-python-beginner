# 2일차에서 배운 int(), float()도 함수. 많이 할 것이 없다.
n1, n2 = 3, 3.5
print(n1, float(n1))
print(n2, int(n2))

# 나중에 개선될 수도 있는 소수점 연산
print(1.1 + 2.2)  # 3.3000000000000003
print(1.1 + 2.7)  # 3.8000000000000003
# 컴퓨터에서 부동 소수점 숫자는 정확하게 저장할 수 없다.
# 10/3 = 3.333333333333....
# 가장 매우 작은 근사치를 저장하는 방법을 택한다.
# 이런 한계점 때문에 위와 같은 현상이 있다.

# 9일차에 배울 라이브러리 참조 방식을 미리 활용해서 해결
from decimal import Decimal
print(Decimal(1.1) + Decimal(2.2))
print(Decimal(1.1) + Decimal(2.7))
print(Decimal('1.1') + Decimal('2.2'))
print(Decimal('1.1') + Decimal('2.7'))

# 효율성 측면 때문에 Decimal은 필요할 때만
# 수치 연산이 정확해야할 때. 금융권같이 이슈가 생길 수 있는 부분. 유효한 소수점 자리 수를 제한할 때