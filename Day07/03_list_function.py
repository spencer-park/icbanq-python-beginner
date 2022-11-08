user = ['spencer', 7, 202.2]
print(len(user))

# 새로운 데이터 추가 append
user.append(10000)
print(user)
user += [20000,]
print(user)

# 삽입 insert
user = ['spencer', 7, 202.2]
user.insert(1, 10000)
print(user)

# 값 탐색 > 인덱스 반환 index, 개수 세기 count
numbers = [100, 70, 30, 50, 60, 70, 100]
print(numbers.index(70))
print(numbers.index(30))
print(numbers.count(100))

# 값 탐색 > 삭제 remove
numbers.remove(100)
print(numbers)
numbers.remove(30)
print(numbers)

# 리스트 합치기 확장 extend
score1 = [30, 50, 70]
score2 = [20, 40, 60]
total_score = score1 + score2  # 비파괴적
print(total_score)  
score1.extend(score2)  # 파괴적
print(score1) 

# 반전 - .reverse(), reversed()
numbers = [2, 4, 6, 1, 3, 5]
print(list(reversed(numbers)))  # 비파괴적
numbers.reverse()  # 파괴적
print(numbers)

# 정렬(오름차순) - .sort(), sorted()
numbers = [2, 4, 6, 1, 3, 5]
print(list(sorted(numbers)))  # 비파괴적
numbers.sort()  # 파괴적. 
print(numbers)


# 정렬(내림차순)
numbers = [2, 4, 6, 1, 3, 5]
print(list(sorted(numbers, reverse=True)))  # 비파괴적
numbers.sort(reverse=True)  # 파괴적. 
print(numbers)
