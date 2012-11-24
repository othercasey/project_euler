list_o_fibs = [1, 1]
print list_o_fibs
while list_o_fibs[-1] + list_o_fibs[-2] < 4000000:
	list_o_fibs.append(list_o_fibs[-1] + list_o_fibs[-2])

print list_o_fibs

even_fibs_lie = []

for x in list_o_fibs:
	if x % 2 == 0:
		even_fibs_lie.append (x)

print even_fibs_lie
print sum (even_fibs_lie)

print "happy programming dance"