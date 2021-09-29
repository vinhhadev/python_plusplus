my_list = [(2, 5), (4, 1), (0, 0)]
lst = len(my_list)
for i in range(0, lst):
    for j in range(0, lst - i - 1):
        if (my_list[j][1] > my_list[j + 1][1]):
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)