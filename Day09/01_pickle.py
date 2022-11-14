import os, pickle

# WD 변경
os.chdir(os.path.dirname(__file__))  # os.chdir('원하는 경로')

# 확인
class_number = 5
member = ['스펜서', '까마귀', '벌새']
teacher = {
    'name' : '귀도',
    'lang' : 'Python'
}

# pickle로 저장
save_data = [class_number, member, teacher]
with open('01_pickle.pickle', 'wb') as fp:
    pickle.dump(save_data, fp)

# pickle에서 가져오기
with open('05_pickle.pickle', 'rb') as fp:
    load_data = pickle.load(fp)
print(load_data)