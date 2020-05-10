def checkPassword(s):
	count = 0 
	replace = 0
	remove = 0
	n = len(s)
	add = 0

	if(n <= 3):
		return(6-n)

	if len(s) > 20:
		remove += len(s) - 20
	elif len(s) < 6:
		add += 6 - len(s)

	found_l = False
	found_u = False
	found_d = False


	for x in s:
		if found_l and found_d and found_u:
			break
		if not found_l:
			if 97 <= ord(x) <= 122:
				found_l = True

		if not found_u:
			if 65 <= ord(x) <= 90:
				found_u = True

		if not found_d:
			if 48 <= ord(x) <= 57:
				found_d = True

	if not found_d:

		replace += 1
	if not found_l:

		replace += 1

	if not found_u:
		replace += 1

	if(add > replace):
		replace = add

	temp = " "
	series = []
	for x in s:
		if(x == temp[0]):
			temp += x

		else:
			if(len(temp) >= 3):
					series.append([len(temp),temp])
			temp = x


	if(len(temp) >= 3):
		series.append([len(temp),temp])

	

	

	for x in series:
		if(x[0] %3 == 0 and remove > 0):
			x[0] -= 1
			remove -= 1
			count += 1

	for x in series:
		if(x[0] %3 == 1 and remove > 1):
			x[0] -= 2
			remove -= 2
			count += 2


	all = True
	while(remove > 2):
		all = False
		for x in series:
			if(remove < 2):
				break

			if(x[0] % 3 == 2):
				remove -= 3
				x[0] -= 3
				count += 3
				all = True




	for ind,x in enumerate(series):
		if(x[0] >= 3):
			count += x[0] // 3
			if(replace != 0):
				replace -= x[0] // 3
			if(replace < 0):
				replace = 0



	return(count+replace+remove)
