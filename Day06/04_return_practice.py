def counter_number_state(n_list):
    state = {
        'positive' : 0,
        'negative' : 0,
        'zero' : 0,
    }
    for n in n_list:
        if n > 0:
            state['positive'] += 1
        elif n < 0:
            state['negative'] += 1
        else:
            state['zero'] += 1
    return state


numbers = [-3, -2, -1, 0, 1, 2, 3, 4]
counter = counter_number_state(numbers)
print(counter)
