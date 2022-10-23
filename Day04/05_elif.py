# 조건문 if elif else case1
name = 'Spencer'
# name = 'John'
age = 18
salary = 10000

if salary < 1500:
    print('세금 미납부 대상자입니다.')
elif 1500 <= salary < 5000:
    print('세금 납부 유형 1 대상자입니다.')
else:
    print('세금 납부 유형 2 대상자입니다.')

# 조건문 if elif else case2
press_btn = 'btn_A'

if press_btn == 'btn_A':
    print('LEDs :', ['ON', 'OFF', 'OFF'])
elif press_btn == 'btn_B':
    print('LEDs :', ['OFF', 'ON', 'OFF'])
elif press_btn == 'btn_C':
    print('LEDs :', ['OFF', 'OFF', 'ON'])
else:
    print('LEDs :', ['OFF', 'OFF', 'OFF'])