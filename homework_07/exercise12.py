set1 = {1, 2, 4, 7}
set2 = {1, 3, 4, 6}

#difference_update
set1.difference_update(set2)
print(set1)

#intersection_update
x = {1, 4, 3}
y = {3, 4, 5}
x.intersection_update(y)
print(x)

#isdisjoint
x = {1, 4, 5}
y = {3, 5, 6}
z = x.isdisjoint(y)
print(z)

#issubset
x = {'a', 'b', 'c'}
y = {'c', 'b', 'a', 'd', 'e'}
z = x.issubset(y)
print(z)

#issuperset
x = {'c', 'b', 'a', 'd', 'e'}
y = {'a', 'b', 'c'}

z = x.issuperset(y)
print(z)

#symmetric_difference_update
x = {"apple", "facebook", "samsung"}
y = {"google", "microsoft", "facebook"}

x.symmetric_difference_update(y)
print(x)
