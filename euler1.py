my_list = []
for x in range(1000):
    if x % 5 == 0 or x % 3 == 0:
        my_list.append(x)

print my_list
print sum (my_list)