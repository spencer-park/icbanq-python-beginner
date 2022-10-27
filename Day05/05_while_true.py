# while condition
number = int(input("0을 입력할 때까지 반복 : "))
while number != 0:
    number = int(input("0을 입력할 때까지 반복 : "))
print('종료')


# while True
number = int(input("0을 입력할 때까지 반복 : "))
while True:
    if number == 0 :
        break
    number = int(input("0을 입력할 때까지 반복 : "))
print('종료')


# while True 응용
user_input = input("0을 입력할 때까지 반복 : ")
basket = []
while True:
    if user_input == "0" :
        break
    basket.append(user_input)
    user_input = input("0을 입력할 때까지 반복 : ")
print('종료', basket)