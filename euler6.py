list_one = []
list_two = []
bucket_list = []

for x in range(1,101):
	list_one.append(x**2)
	list_two.append(x)
bucket_list.append(sum(list_one))
bucket_list.append(sum(list_two)**2)

print bucket_list
print bucket_list[-1] - bucket_list[-2]