my_list = ['Python', 'Java', 'PHP', (1, 2, 3)]
for item in my_list:
    res = type(item) is tuple
    if (res == True) :
        _index = my_list.index(item)
        print(f'Số lượng phần tử: {_index}')