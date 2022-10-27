# 구구단 for
for i in range(1, 10):
    print("{} x {} = {}".format(3, i, 3 * i))


# 구구단 while
xs = range(1, 10)
index = 0
while index < len(xs):
    print("{} x {} = {}".format(3, xs[index], 3 * xs[index]))
    index += 1


# Quiz 구구단 전체 while로 구현하기