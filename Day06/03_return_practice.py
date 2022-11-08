def count_negative(n_list):
    count = 0  # local
    for n in n_list:
        if n < 0:
            count += 1
    return count


n_list = [-3, -2, -1, 0, 1, 2, 3, 4]
count = count_negative(n_list)  # global
print(f'{n_list} 는 음수가 {count}')