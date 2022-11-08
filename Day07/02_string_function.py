text = "Hello Spencer"
print(len(text))
print(text.find('S'))
print(text.count('e'))
print(text.count('Spencer'))
print(text.center(20))
print(text.ljust(20))
print(text.rjust(20))

text = "Hello Spencer"
text.upper()  # 파괴적인 처리
print(text)

text.lower()
print(text)

text = "Hello Spencer"
print(text.split())
print(text)  # 원본 변화가 없다. 비파괴적인 처리

text = "Spencer Depencer Spencer Depencer"
text = text.replace('Depencer', 'Spencer')
print(text)