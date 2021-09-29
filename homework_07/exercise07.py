tup1 = ('Python', 'Java', 'HTML', 'CSS', 1, 2)
tup2 = ('C++', 'Java', 3, 4)

common_s = set(tup1) & set(tup2)

if (len(common_s) > 0) :
    print('Có phần tử trung nhau')
    for i in common_s:
        print(f'Phần tử trùng nhau là: {i}')
else:
    print('Không có phần tử trùng nhau')
