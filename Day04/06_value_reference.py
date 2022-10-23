# 값과 주소
# 값과 주소가 같을 경우 1
a = 2
b = 2
print(id(a), id(b))
print(a==b, a is b)

# 값과 주소가 같을 경우 2
list1 = [100, 90, 80]
list2 = list1
print(list1, list2)
print(id(list1), id(list2))
print(list1==list2, list1 is list2)

# 값은 같으나 주소가 다를 경우 2
student1 = [100, 90, 80]
student2 = [100, 90, 80]
print(student1, student2)
print(id(student1), id(student2))  # 다르다
print(student1==student2, student1 is student2)  # True False

# Quiz 값은 ? 주소는?
student1 = [100, 90, 80]
student2 = student1
student2[0] = 70  # [70, 90, 80]
print(student1, student2)
print(id(student1), id(student2))  # 같다
print(student1==student2, student1 is student2)  # True True