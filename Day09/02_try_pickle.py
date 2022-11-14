import pickle

try:
    # pickle에서 가져오기
    with open('02_pickle.pickle', 'rb') as fp:
        current_data = pickle.load(fp)
except:
    # 실패하면 해당 코드 실행
    class_number = -1
    member = []
    teacher = {
        'name' : '미정',
        'lang' : '미정'
    }
    current_data = [class_number, member, teacher]


print(current_data)
