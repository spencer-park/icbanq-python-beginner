def count_negative(*n_list):
    print(n_list)
    count = 0  # local
    for n in n_list:
        if n < 0:
            count += 1
    return n_list, count


result = count_negative(-3, -2, -1, 9, 1, 2, 3, 4)  # global
print('데이터 {}, 음수가 {}'.format(result[0], result[1]))