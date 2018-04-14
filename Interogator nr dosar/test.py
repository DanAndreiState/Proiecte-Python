while True:

	list_1 = str(input('>>>')).split(' ')
	if len(list_1) == 0:
		break
	list_2 = \
		[['1', '2016', 'Enriche Iglesias'],
		 ['2', '2016', 'Enriche Iglesias'],
		 ['3', '2015', 'Mesi Romales'],
		 ['4', '2016', 'Enriche Iglesias'], ]

	set_1 = set(list_1)

	cont = 0
	cont_1 = 0
	for i in list_2:
		set_2 = set(i)

		if set_1.intersection(set_2):
			for each in set_1:
				if each in i[2] and list_1[0] not in ['', ' ']:
					list_1.remove(each)
					set_1 = set(list_1)
					if set_1.issubset(set_2):
						cont_1 += 1
						if cont_1 == len(set_1):
							print(i)
				elif set_1.issubset(set_2):
					cont_1 += 1
					if cont_1 == len(set_1):
						print(i)
		elif list_1[0] in i[2] and list_1[0] not in ['', ' ']:
			print(i)

		else:
			cont += 1
			if cont == len(list_2):
				print('No matches found !')



	#
	# 	if set_1.intersection(set_2):
	# 		if len(set_1.difference(set_2)) > 0:
	# 			for each in set_1.difference(set_2):
	# 				if each in i[2]:
	# 					for other_each in set_2:
	# 						if each in other_each and each not in ['', ' ']:
	# 							print(i)
	# 		else:
	# 			print(i)
	#
	# 	elif list_1[0] in i[2] and list_1[0] not in ['', ' '] and set(list_1[1:]).issubset(set_2):
	# 		print(i)
	#
	# 	else:
	# 		cont += 1
	# 		if cont == len(list_2):
	# 			print('No matches found !')


