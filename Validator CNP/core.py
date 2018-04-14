import re


class Cnp():
	# CNP : [S][AA][LL][ZZ][CJ][XXX][C]

	def __init__(self, cnp):
		self.temp_div = 0
		self.cnp = cnp
		self.control_number = '279146358279'
		self.cod_judet = {
			'01': 'Alba',
			'02': 'Arad',
			'03': 'Argeș',
			'04': 'Bacău',
			'05': 'Bihor',
			'06': 'Bistrița-Năsăud',
			'07': 'Botoșani',
			'08': 'Brașov',
			'09': 'Brăila',
			'10': 'Buzău',
			'11': 'Caraș-Severin',
			'12': 'Cluj',
			'13': 'Constanța',
			'14': 'Covasna',
			'15': 'Dâmbovița',
			'16': 'Dolj',
			'17': 'Galați',
			'18': 'Gorj',
			'19': 'Harghita',
			'20': 'Hunedoara',
			'21': 'Ialomița',
			'22': 'Iași',
			'23': 'Ilfov',
			'24': 'Maramureș',
			'25': 'Mehedinți',
			'26': 'Mureș',
			'27': 'Neamț',
			'28': 'Olt',
			'29': 'Prahova',
			'30': 'Satu Mare',
			'31': 'Sălaj',
			'32': 'Sibiu',
			'33': 'Suceava',
			'34': 'Teleorman',
			'35': 'Timiș',
			'36': 'Tulcea',
			'37': 'Vaslui',
			'38': 'Vâlcea',
			'39': 'Vrancea',
			'40': 'București',
			'41': 'București S.1',
			'42': 'București S.2',
			'43': 'București S.3',
			'44': 'București S.4',
			'45': 'București S.5',
			'46': 'București S.6',
			'51': 'Călărași',
			'52': 'Giurgiu'
		}

	def test_validity(self):

		split_validate = re.compile(
			r'^([1-9])'
			r'(\d{2})'
			r'(0[1-9]|1[0-2])'
			r'(0[1-9]|[12]\d|3[01])'
			r'(0[1-9]|[123]\d|4[0-6]|5[12])'
			r'(\d{3})'
			r'(?<!0{3})(\d)')

		if re.match(split_validate, self.cnp):
			temp_sum = 0
			for index, element in enumerate(self.cnp[0:12]):
				temp_sum += int(element) * int(self.control_number[index])
			self.temp_div = temp_sum % 11
			if self.temp_div == 10:
				self.temp_div = 1
			if int(self.temp_div) == int(self.cnp[-1]):
				return True
			else:
				return False
		else:
			return False

	def explode_values(self):
		ex_S = re.compile(r'^([1-9])\d{0,12}')
		ex_AA = re.compile(r'^\d(\d{2})\d{0,10}')
		ex_LL = re.compile(r'^\d{3}(0[1-9]|1[0-2])\d{0,8}')
		ex_ZZ = re.compile(r'^\d{5}(0[1-9]|[12]\d|3[01])\d{0,6}')
		ex_CJ = re.compile(r'^\d{7}(0[1-9]|[123]\d|4[0-6]|5[12])\d{0,4}')
		ex_XXX = re.compile(r'^\d{9}(\d{3})(?<!0{3})\d*')

		def reduce_list(in_list):
			if type(in_list) == list:
				if len(in_list) > 0:
					return str(in_list[0])
				else:
					return '  '


		return reduce_list(re.findall(ex_S, self.cnp)),  \
			   reduce_list(re.findall(ex_AA, self.cnp)), \
			   reduce_list(re.findall(ex_LL, self.cnp)), \
			   reduce_list(re.findall(ex_ZZ, self.cnp)), \
			   reduce_list(re.findall(ex_CJ, self.cnp)), \
			   reduce_list(re.findall(ex_XXX, self.cnp))
