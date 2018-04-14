from csv_reader import *
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import time
import os
import re
import sorter
import datetime


def cls():
	os.system('cls')


class Gui:
	def __init__(self, initial_csv_name):
		self.initial_file_name = initial_csv_name
		self.redundancy_counter = 1
		self.redundancy_break_point = 0

		self.master = Tk()
		self.master.resizable(False,False)
		self.master.title('Filtru CSV')
		self.master.configure(borderwidth=10, relief=GROOVE)

		self.master_checkbox_frame = Frame(self.master, borderwidth=20, relief=SOLID)
		self.master_checkbox_frame.pack(side=LEFT)

		self.master_entry = Frame(self.master, borderwidth=20, relief=SOLID)
		self.master_entry.pack(side=TOP)

		l = Style()
		l.configure('my.TLabel', font=('Helvetica', 12, 'italic') , foreground='grey')

		j = Style()
		j.configure('Label', font=('Helvetica', 12, 'bold', 'underline'))

		self.titlu_entry = Label(self.master_checkbox_frame, text="Coloane afisate :\n", style='Label')
		self.titlu_entry.pack()

		self.master_widget = Frame(self.master)
		self.master_widget.pack(side=TOP, expand=1)

		s = Style()
		s.configure('my.TButton', font=('Helvetica', 14,'bold'))

		self.button_1 = Button(self.master_widget, text='\nCautare\n', command=self.messageWindow, style='my.TButton')
		self.button_1.pack(side=LEFT, fill=BOTH)

		self.entry_1_variable = StringVar()
		self.entry_1 = Entry(self.master_entry, textvariable=self.entry_1_variable)
		self.entry_1.configure(font="Helvetica 16 bold", justify="left", width=28)
		self.entry_1.pack(side=TOP)
		self.entry_1.focus_force()

		self.front_total_label_var = StringVar()
		self.front_total_label = Label(self.master_entry, textvariable=self.front_total_label_var, style='my.TLabel')
		self.front_total_label.pack(pady=5, side=TOP, anchor=N)

		self.front_path_label_var = StringVar()
		self.front_path_label = Label(self.master_entry, textvariable=self.front_path_label_var,style='my.TLabel')
		self.front_path_label.pack(pady=0, side=TOP, anchor=N)

		### Init + config butonul de incarcare a altui fisier:
		self.button_2 = Button(self.master_widget, text='Reincarcare\n  document', command=self.reload_file,
							   style='my.TButton')
		self.button_2.pack(side=TOP, anchor=E, padx=5)
		### END Init + config butonul de incarcare a altui fisier:



		self.button_3 = Button(self.master_widget, text='Iesire', command=quit, style='my.TButton')
		self.button_3.pack(side=BOTTOM, anchor=E, padx=5)

		self.button_4 = Button(self.master_widget, text='Ajutor', command=self.help, style='my.TButton')
		self.button_4.pack(side=BOTTOM, anchor=E, padx=5)

		self.master_check_box()
		### Init + config subrutine interne:
		self.master_widget_bindings()
		### END Init + config subrutine interne:
		self.initial_file_loading()
		self.f_3_filter()
		self.front_total_label_var.set('Elemente totale gasite : {}'.format(str(len(self.main_string))))

		self.front_path_label_var.set(" Fisier curent : {}".format(self.opened_from))
		### Init Tk_loop:

		self.master.mainloop()

	def master_check_box(self):

		self.check_c1_index_var = StringVar()
		self.check_c1_index = Checkbutton(self.master_checkbox_frame, text='Index', variable=self.check_c1_index_var,
										  onvalue="Index", offvalue=None)
		self.check_c1_index_var.set("Index")
		self.check_c1_index.pack(side=TOP, anchor=W)

		self.check_c2_nr_dosar_var = StringVar()
		self.check_c2_nr_dosar = Checkbutton(self.master_checkbox_frame, text='Nr Dosar',
											 variable=self.check_c2_nr_dosar_var,
											 onvalue="Nr Dosar", offvalue=None)
		self.check_c2_nr_dosar_var.set("Nr Dosar")
		self.check_c2_nr_dosar.pack(side=TOP, anchor=W)

		self.check_c3_an_dosar_var = StringVar()
		self.check_c3_an_dosar = Checkbutton(self.master_checkbox_frame, text='An Dosar',
											 variable=self.check_c3_an_dosar_var,
											 onvalue="An Dosar", offvalue=None)
		self.check_c3_an_dosar_var.set("An Dosar")
		self.check_c3_an_dosar.pack(side=TOP, anchor=W)

		self.check_c4_nume_dosar_var = StringVar()
		self.check_c4_nume_dosar = Checkbutton(self.master_checkbox_frame, text='Procuror',
											   variable=self.check_c4_nume_dosar_var,
											   onvalue="Procuror", offvalue=None)
		self.check_c4_nume_dosar_var.set("Procuror")
		self.check_c4_nume_dosar.pack(side=TOP, anchor=W)

		self.check_c5_data_iup_var = StringVar()
		self.check_c5_data_iup = Checkbutton(self.master_checkbox_frame, text='Data IUP',
											 variable=self.check_c5_data_iup_var,
											 onvalue="Data IUP", offvalue=None)
		self.check_c5_data_iup_var.set("Data IUP")
		self.check_c5_data_iup.pack(side=TOP, anchor=W)

		self.check_c6_data_cup_var = StringVar()
		self.check_c6_data_cup = Checkbutton(self.master_checkbox_frame, text='Data CUP',
											 variable=self.check_c6_data_cup_var,
											 onvalue="Data CUP", offvalue=None)
		self.check_c6_data_cup_var.set("Data CUP")
		self.check_c6_data_cup.pack(side=TOP, anchor=W)

		self.check_c7_data_pma_var = StringVar()
		self.check_c7_data_pma = Checkbutton(self.master_checkbox_frame, text='Data PMA',
											 variable=self.check_c7_data_pma_var,
											 onvalue="Data PMA", offvalue=None)
		self.check_c7_data_pma_var.set("Data PMA")
		self.check_c7_data_pma.pack(side=TOP, anchor=W)

		self.check_c8_data_solutie_var = StringVar()
		self.check_c8_data_solutie = Checkbutton(self.master_checkbox_frame, text='Data Solutie',
												 variable=self.check_c8_data_solutie_var,
												 onvalue="Data Solutie", offvalue=None)
		self.check_c8_data_solutie_var.set("Data Solutie")
		self.check_c8_data_solutie.pack(side=TOP, anchor=W)

	def master_widget_bindings(self):
		# Buttons bindings
		self.button_1.bind('<Return>', lambda event: self.messageWindow())
		self.button_2.bind('<Return>', lambda event: self.reload_file())

		# Entrys bindings

		self.entry_1.bind('<Return>', lambda event: self.messageWindow())
		# Master window bindings

		self.master.bind('<Escape>', lambda event: self.master.destroy())

		self.check_c1_index.bind('<Return>', lambda event: self.messageWindow())
		self.check_c2_nr_dosar.bind('<Return>', lambda event: self.messageWindow())
		self.check_c3_an_dosar.bind('<Return>', lambda event: self.messageWindow())
		self.check_c4_nume_dosar.bind('<Return>', lambda event: self.messageWindow())
		self.check_c5_data_iup.bind('<Return>', lambda event: self.messageWindow())
		self.check_c6_data_cup.bind('<Return>', lambda event: self.messageWindow())
		self.check_c7_data_pma.bind('<Return>', lambda event: self.messageWindow())
		self.check_c8_data_solutie.bind('<Return>', lambda event: self.messageWindow())

	def initial_file_loading(self):
		self.main_array, self.path = csv_to_array(self.initial_file_name, 0, 1)
		self.main_string = ''
		self.opened_from = self.path
		self.front_path_label_var.set(" Fisier curent : {}".format(self.opened_from))

	def reload_file(self):
		self.main_array, self.path = csv_to_array('*.csv', 0, 1)
		if len(self.main_array) > 0:
			self.main_string = ''

		elif self.redundancy_counter > self.redundancy_break_point:
			answer = messagebox.askquestion('Nu ati selectat nici un fisier !',
											'Doriti incarcarea fisierului initial ?')
			if answer == 'no':
				time.sleep(1)
				messagebox.showerror('Aplicatia va iesi', 'Aplicatia va iesi in 1 secunda ...')
				self.master.quit()
			elif answer == 'yes':
				self.redundancy_counter = 0
				self.initial_file_loading()
		else:
			print(self.redundancy_counter)
			self.redundancy_counter += 1
			self.reload_file()

		self.entry_1.focus_force()
		self.entry_1.select_range(0, END)

		# self.opened_from = self.path.split('\'')[1]
		self.opened_from = re.findall('(?<=name.)(.*)(?=\smode)',self.path,re.I)[0]

		self.f_3_filter()
		self.front_total_label_var.set('Elemente totale gasite : {}'.format(str(len(self.main_string))))
		self.front_path_label_var.set(" Fisier curent : {}".format(self.opened_from))

	def messageWindow(self):
		# On start :

		self.f_3_filter()
		self.win = Toplevel()
		self.win.configure(borderwidth=10, relief=GROOVE)
		self.win.title('Rezultatele filtrarii ...')
		self.win.resizable(True, True)

		window_width = 0
		window_height = 300
		max_window_height = 700
		step_window_height = 50

		# Def cadru superior (va tine butoane + info)-va fi interiorul Cadrului principal
		self.top_frame = Frame(self.win)
		self.top_frame.configure(borderwidth=20, relief=SOLID)
		self.top_frame.pack(side=TOP, fill=X, padx=20, anchor=CENTER)

		# Def cadru inferior (va tine treeview + scrollbar)-va fi in interiorul Cadrului principal
		self.bottom_frame = Frame(self.win)
		self.bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=1, padx=20)

		# Def cadru cu butoane + widgeturi - va fi in interiorul Cadrului superior
		self.top_frame_button_progress = Frame(self.top_frame)
		self.top_frame_button_progress.pack(side=RIGHT)

		# Def cadru cu informatii misc
		self.top_frame_info = Frame(self.top_frame)
		self.top_frame_info.pack(side=LEFT)

		# Def scrollbar-va fi in interiorul Cadrului inferior
		self.scrollbar = Scrollbar(self.bottom_frame, orient=VERTICAL)

		# Def widgeturi - va fi in interiorul TOP FRAME INFO

		l = Style()
		l.configure('my.TLabel', font=('Helvetica', 12, 'italic') , foreground='grey')

		self.label_open_from_var = StringVar()
		self.label_open_from = Label(self.top_frame_info, textvariable=self.label_open_from_var, style='my.TLabel')
		self.label_open_from.pack()

		self.label_open_from_var.set("Fisier curent : {} ".format(self.opened_from))

		self.label_element_nr_var = StringVar()
		self.label_element_nr = Label(self.top_frame_info, textvariable=self.label_element_nr_var, style='my.TLabel')
		self.label_element_nr.pack(side=LEFT)

		# Def buton export
		self.but_1 = Button(self.top_frame_button_progress, command=self.children, text='Export', style='my.TButton')
		self.but_1.pack(side=LEFT, anchor=CENTER)

		# Def label progress
		self.label_1_var = StringVar()
		self.lab_1 = Label(self.top_frame_button_progress, textvariable=self.label_1_var)
		self.lab_1.pack(side=LEFT, anchor=CENTER)

		# Def progress bar
		self.progress = Progressbar(self.top_frame_button_progress, length=400, mode='determinate')
		self.progress.pack(side=LEFT, anchor=CENTER)

		cols = ('Index', 'Nr Dosar', 'An Dosar', 'Procuror', "Data IUP", "Data CUP", "Data PMA", "Data Solutie")
		dif_cols = [
			self.check_c1_index_var.get(),
			self.check_c2_nr_dosar_var.get(),
			self.check_c3_an_dosar_var.get(),
			self.check_c4_nume_dosar_var.get(),
			self.check_c5_data_iup_var.get(),
			self.check_c6_data_cup_var.get(),
			self.check_c7_data_pma_var.get(),
			self.check_c8_data_solutie_var.get()
		]
		displaycolumns = []

		self.tv = Treeview(self.bottom_frame, columns=cols, yscrollcommand=self.scrollbar.set)

		for index, column in enumerate(cols):
			self.tv.heading(column, text=column, anchor='center')
			self.tv.column(column, anchor='center', width=100)

		self.tv['show'] = 'headings'

		for index, value in enumerate(cols):
			if value == dif_cols[index]:
				displaycolumns.append(value)

		self.tv['displaycolumns'] = displaycolumns

		for each in displaycolumns:
			window_width += 100
		if len(displaycolumns) == 0:
			window_width += 100

		self.win.minsize(window_width - 100, int(max_window_height / 2))
		try:

			for index, element in enumerate(self.main_string):
				self.tv.insert('', 'end', values=(
					index + 1, element[0], element[1], element[2], element[3], element[4], element[5], element[6]))
				if window_height < max_window_height and len(self.main_string) <= 1:
					window_height += step_window_height * 3
				elif window_height < max_window_height:
					window_height += step_window_height

			self.tv.pack(fill=BOTH, expand=1, side=LEFT)
			self.scrollbar.config(command=self.tv.yview)
			self.scrollbar.pack(side=LEFT, fill=BOTH)

			for each in cols:
				self.tv.heading(each,
								text=each,
								command=lambda each_=each:
								sorter.treeview_sort_column(self.tv, each_, False))

			# Setarea nr de elmente pt labelul din widgeturi
			self.label_element_nr_var.set('Numar elemente returnate : {}'.format(str(len(self.tv.get_children()))))

			# On exit :
			self.win.bind('<Escape>', lambda event: self.win.destroy())
			self.win.bind('<Return>', lambda event: self.win.destroy())
			self.win.focus_force()
			self.entry_1.focus_force()
			self.entry_1.select_range(0, END)

		except IndexError as e:
			self.win.destroy()
			messagebox.showwarning('Eroare indexare ...', str(self.main_string[0][0]))
		# self.entry_1.focus_force()
		# self.entry_1.select_range(0, END)

		try:
			self.win.geometry('{}x{}'.format(window_width * 2, window_height))
		except:
			pass

	def children(self):
		max_items = len(self.tv.get_children())
		self.progress['maximum'] = max_items
		self.file_name = 'Export din {}{}{}_{}{}{}.csv'.format(datetime.datetime.now().hour,
															  datetime.datetime.now().minute,
															  datetime.datetime.now().second,
															  datetime.datetime.now().day,
															  datetime.datetime.now().month,
															  datetime.datetime.now().year)
		with open(self.file_name, 'w') as csv_file:
			fieldnames = ['Index',
						  'Numar Dosar',
						  'An Dosar',
						  'Nume Procuror',
						  'Data IUP',
						  'Data CUP',
						  'Data PMA',
						  'Data Solutie']

			writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
			writer.writeheader()

			for index, item in enumerate(self.tv.get_children()):
				self.progress['value'] = int(index)
				writer.writerow({'Index': self.tv.item(item)['values'][0],
								 'Numar Dosar': self.tv.item(item)['values'][1],
								 'An Dosar': self.tv.item(item)['values'][2],
								 'Nume Procuror': self.tv.item(item)['values'][3],
								 'Data IUP': self.tv.item(item)['values'][4],
								 'Data CUP': self.tv.item(item)['values'][5],
								 'Data PMA': self.tv.item(item)['values'][6],
								 'Data Solutie': self.tv.item(item)['values'][7]})
				self.label_1_var.set('{} %'.format(
					round((index / max_items) * 100, 1)
				))
				self.progress.update()
			self.progress['value'] = max_items
			self.label_1_var.set('100 %')
			time.sleep(0.5)
			messagebox.showinfo('Export finalizat', ' S-a exportat fisierul "{}"'.format(self.file_name))
			self.win.focus_force()

	def f_3_filter(self):
		try:
			self.main_string = []
			user_input = []
			processed_main_array = []
			for each in re.findall(r'[\w\.]+', self.entry_1.get(), re.IGNORECASE):
				user_input.append(each)
			for index, item in enumerate(self.main_array):
				nr_dosar = []
				temp_array = []
				nr_dosar.append(str(item[0]).split('/'))

				# Append pozitiile care se vor afisa in final

				# Append poz 0 pt intersectii (nr dosar)
				temp_array.append(nr_dosar[0][0])
				# Append poz 1 pt intersectii (an dosar)
				temp_array.append(nr_dosar[0][2])
				# Append poz 2 pt intersectii (nume procuror)
				temp_array.append(item[2])
				# Append poz 3 pt intersectii (Data IUP)
				temp_array.append(item[3])
				# Append poz 4 pt intersectii (Data CUP)
				temp_array.append(item[4])
				# Append poz 5 pt intersectii (Data PMA)
				temp_array.append(item[5])
				# Append poz 6 pt intersectii (Data Solutie)
				temp_array.append(item[6])
				processed_main_array.append(temp_array)

			list_1 = user_input
			list_2 = processed_main_array
			if len(list_1) <= 3 and len(list_1) > 0:
				set_1 = set(list_1)
			elif len(list_1) == 0:
				self.main_string.append(['NULL ARGUMENTS !'])
				list_1 = ['']
				set_1 = set(list_1)
			else:
				self.main_string.append(['TOO MANY ARGUMENTS !'])
				list_1 = ['']
				set_1 = set(list_1)
			cont = 0
			for i in list_2:
				cont_1 = 0
				set_2 = set(i)

				if set_1.intersection(set_2):
					for each in set_1:
						if each.lower() in i[2].lower() and list_1[0] not in ['', ' ']:
							list_1.remove(each)
							set_1 = set(list_1)
							if set_1.issubset(set_2):
								cont_1 += 1
								if cont_1 == len(set_1):
									self.main_string.append(i)
									cont_1 = 0
									cont = 0
								elif cont_1 == 1 and len(set_1) == 2:
									self.main_string.append(i)
									cont_1 = 0
									cont = 0
							list_1.append(each)
							set_1 = set(list_1)
						elif set_1.issubset(set_2):
							cont_1 += 1
							if cont_1 == len(set_1):
								self.main_string.append(i)
								cont_1 = 0
								cont = 0

				elif list_1[0].lower() in i[2].lower() \
						and list_1[0] not in ['', ' '] \
						and set(list_1[1:]).issubset(set_2) \
						and list_1[0] != None:
					self.main_string.append(i)
					cont = 0
					cont_1 = 0
				else:
					cont += 1
					if cont == len(list_2) \
							and 'Too many arguments !' not in self.main_string \
							and 'NULL ARGUMENTS' not in self.main_string:
						self.main_string.append(['NO MATCHES !'])
		except:
			messagebox.showerror('Format gresit !',
								 'Fisierul incarcat " {} "este incorect / format gresit ! \n\n Va rugam selectati alt fisier ! '.format(
									 self.opened_from))
			self.reload_file()

	def help(self):
		self.help = Toplevel()
		self.help.configure(borderwidth=10, relief=GROOVE)
		self.help.title('Ajutor ...')
		self.help.resizable(False,False)



		self.help_notebook = Notebook(self.help ,  style = 'Label')
		self.help_notebook.pack(fill = BOTH , expand = 1)

		self.help_page_1 = Frame(self.help_notebook)
		self.help_notebook.add(self.help_page_1, text='Filtrare si sintaxa ... ')

		self.help_page_1_label = Label(self.help_page_1 ,

text = '\n\n\n'
'	Pentru filtrare se pot folosi nume , numere de dosar sau ani ai dosalelor. Programul va sorta in \n functie de acestea si va afisa rezultatele intr-o fereastra separata. De exemplu, daca dorim sa cautam \ninformatii despre toti procurorii cu numele de "Vasile" care au dosar in anul "2015" , vom scrie :\n\n '
	   '					[ Vasile 2015 ] \n'
	   '					[ 2015 Vasile ] \n'
	   '					[ VAS 2015 ] \n'
	   '					[vasi 2015]\n\n'
'	Deasemenea putem folosi si / sau numarul de dosar pentru o filtrare mai exacta (de exemplu dosarul cu\n numarul "54" din "2012" care ii apartine lui "Constantin") :\n\n'
	   '					[ 54 cons 2012] \n'
	   '					[ Consta 2012 54 ] \n\n'
'	Pentru a afisa in fereastra de rezultate doar anumite coloane, cele nedorite se vor debifa.\n\n')



		self.help_page_1_label.pack()

		self.help_page_2 = Frame(self.help_notebook)
		self.help_notebook.add(self.help_page_2, text='Reincarcare document')
		self.help_page_2_label = Label(self.help_page_2,
text='\n\n\n'
'	Pentru a incarca unui document diferit asupra caruia se dorste filtrarea, apasati pe tasta 		   \n"Reincarcare document" si selectati fisierul dorit.\n\n\n\n'
'	ATENTIE ! Doar fisierele cu structura corecta vor fi acceptate ! Structura standard este \nurmatoarea :\n\n\n\n\n\n'
'	NUMAR DOSAR | coloana goala | PROCURORI | DATA IUP | DATA CUP | DATA PMA | DATA SOLUTIE')
		self.help_page_2_label.pack()


		self.help_page_3 = Frame(self.help_notebook)
		self.help_notebook.add(self.help_page_3, text='Export')
		self.help_page_3_label = Label(self.help_page_3,
text='\n\n\n	Rezultatele sortarii / filtrarii se pot exporta intr-un CSV separat pt salvarea datelor.\n'
'Pentru export se apasa butonul "Export" din fereastra de afisare a rezultatelor. Fisierul va aprea in\n'
'folderul curent de unde se ruleaza programul si va avea numele de "Export din ora curenta _ data curenta"')
		self.help_page_3_label.pack()





		#on exit
		self.help.bind('<Escape>', lambda event: self.help.destroy())
		self.help.bind('<Return>', lambda event: self.help.destroy())
		self.help.focus_force()
		self.entry_1.focus_force()
		self.entry_1.select_range(0, END)


app = Gui('export_1.csv')
