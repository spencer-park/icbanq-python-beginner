import keyword
from platform import python_branch
print(keyword.kwlist)

'''
'False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield'
'''

# 값을 할당하는 = 을 붙이는 순간 오류를 표현하는 빨간 밑줄이 뜬다.
# True = 3
# def = 3
# if = 3
# return = 3