from core import Cnp as Clasa_Cnp
from tkinter import *
import re


class Gui():
	def __init__(self):

		self.default_color = 'LightSteelBlue1'
		self.true_vaidate_color = 'lawn green'
		self.false_validate_color = 'firebrick1'
		self.input_error = 'orange'

		self.fonts = 'Calibri 22 bold'

		self.master = Tk()
		self.master.geometry()
		self.master.resizable(False, False)
		self.master.title("Va rugam introduce-ti un CNP pentru validare ...")

		self.entry_var = StringVar()
		self.entry = Entry(self.master, textvariable=self.entry_var)
		self.entry.config(font="avantgarde  36 bold",
						  bg=self.default_color,
						  justify='center',
						  borderwidth='2',
						  relief=SOLID)
		self.entry.grid(row=0, column=0, columnspan=2, padx='1', pady='2')
		self.entry.focus_force()

		self.label_S = Label(self.master, text='Sexul :')
		self.label_S.config(font = self.fonts)
		self.entry_var_S = StringVar()
		self.entry_S = Entry(self.master, textvariable=self.entry_var_S)
		self.entry_S.config(font = self.fonts,bg=self.default_color,justify='center',borderwidth='1',relief=SOLID)
		self.label_S.grid(row=1, column=0, padx='1', pady='1')
		self.entry_S.grid(row=1, column=1, padx='1', pady='1')

		self.label_ZZLLAA = Label(self.master, text='Data nașterii :')
		self.label_ZZLLAA.config(font = self.fonts)
		self.entry_var_ZZLLAA = StringVar()
		self.entry_ZZLLAA = Entry(self.master, textvariable=self.entry_var_ZZLLAA)
		self.entry_ZZLLAA.config(font = self.fonts,bg=self.default_color,justify='center',borderwidth='1',relief=SOLID)
		self.label_ZZLLAA.grid(row=2, column=0, padx='1', pady='1')
		self.entry_ZZLLAA.grid(row=2, column=1, padx='1', pady='1')

		self.label_CJ = Label(self.master, text='Judetul nașterii :')
		self.label_CJ.config(font = self.fonts)
		self.entry_var_CJ = StringVar()
		self.entry_CJ = Entry(self.master, textvariable=self.entry_var_CJ)
		self.entry_CJ.config(font = self.fonts,bg=self.default_color,justify='center',borderwidth='1',relief=SOLID)
		self.label_CJ.grid(row=3, column=0, padx='1', pady='1')
		self.entry_CJ.grid(row=3, column=1, padx='1', pady='1')

		self.label_XXX = Label(self.master, text='Număr ordine :')
		self.label_XXX.config(font = self.fonts)
		self.entry_var_XXX = StringVar()
		self.entry_XXX = Entry(self.master, textvariable=self.entry_var_XXX)
		self.entry_XXX.config(font = self.fonts,bg=self.default_color,justify='center',borderwidth='1',relief=SOLID)
		self.label_XXX.grid(row=4, column=0, padx='1', pady='1')
		self.entry_XXX.grid(row=4, column=1, padx='1', pady='1')

		self.label_C = Label(self.master, text='Cifră de control :')
		self.label_C.config(font=self.fonts)
		self.entry_var_C = StringVar()
		self.entry_C = Entry(self.master, textvariable=self.entry_var_C)
		self.entry_C.config(font=self.fonts, bg=self.default_color,justify='center',borderwidth='1',relief=SOLID)
		self.label_C.grid(row=5, column=0, padx='1', pady='1')
		self.entry_C.grid(row=5, column=1, padx='1', pady='1')

		self.entry.bind('<KeyRelease>', self.event_init)
		self.entry.bind('<FocusIn>', self.focus_select)
		self.entry_S.bind('<KeyRelease>', self.event_init)
		self.entry_ZZLLAA.bind('<KeyRelease>', self.event_init)
		self.entry_CJ.bind('<KeyRelease>', self.event_init)
		self.entry_XXX.bind('<KeyRelease>', self.event_init)
		self.entry_C.bind('<KeyRelease>', self.event_init)


		self.master.mainloop()

	def focus_select(self, event):
		if len(self.entry.get()) == 13:
			self.entry.select_range(0, END)

	def validate(self):
		cnp = Clasa_Cnp(self.entry.get())
		if len(self.entry.get()) > 20:
			self.entry_var.set(str(self.entry.get())[0:20])
		if str(self.entry.get()).isdigit():
			try:
				if cnp.test_validity() == True and len(self.entry.get()) == 13:
					self.entry.config(bg=self.true_vaidate_color)
					self.master.title("CNP-ul este corect !")
				elif cnp.test_validity() == False and len(self.entry.get()) == 13:
					self.entry.config(bg=self.false_validate_color)
					self.master.title("CNP-ul este incorect !")
				elif len(self.entry.get()) > 13:
					self.entry.config(bg=self.input_error)
					self.master.title("CNP-ul este prea lung ! {}/13 cifre ...".format(len(self.entry.get())))
				elif len(self.entry.get()) < 13:
					self.entry.config(bg=self.default_color)
					self.master.title("CNP-ul este prea scurt ! {}/13 cifre ...".format(len(self.entry.get())))
				else:
					self.entry.config(bg=self.default_color)
					self.master.title("Va rugam introduce-ti un CNP pentru validare ...")
			except ValueError:
				self.entry.config(bg=self.input_error)
				self.master.title("CNP-ul introdus contine unul sau mai multe caractere nepermise !")
		elif len(self.entry.get()) == 0:
			self.entry.config(bg=self.default_color)
			self.master.title("Va rugam introduce-ti un CNP pentru validare ...")
		else:
			self.entry.config(bg=self.input_error)
			self.master.title("CNP-ul introdus contine unul sau mai multe caractere nepermise !")

	def explode(self):
		cnp=Clasa_Cnp(self.entry.get())
		a, b, c, d, e, f = Clasa_Cnp(self.entry.get()).explode_values()
		judete = Clasa_Cnp(self.entry.get()).cod_judet


		try:
			if a != '9' and int(a) % 2 == 1:
				if int(a) != 7:
					self.entry_var_S.set('Bărbat')
					self.entry_S.config(bg=self.true_vaidate_color)
				else:
					self.entry_var_S.set('Bărbat (Rezident)')
					self.entry_S.config(bg=self.true_vaidate_color)

			elif a != '9' and int(a) % 2 == 0:
				if int(a) != 8:
					self.entry_var_S.set('Femeie')
					self.entry_S.config(bg=self.true_vaidate_color)
				else:
					self.entry_var_S.set('Femeie (Rezidentă)')
					self.entry_S.config(bg=self.true_vaidate_color)
			elif a == '9':
				self.entry_var_S.set('Cetațean străin')
				self.entry_S.config(bg=self.true_vaidate_color)
			if len(self.entry.get()) == 0:
				self.entry_S.config(bg=self.default_color)
		except ValueError:
			if self.entry.get() == '':
				self.entry_var_S.set('')
				self.entry_S.config(bg=self.default_color)
			elif re.match(r'[^\d]+',str(self.entry.get())):
				self.entry_var_S.set('')
				self.entry_S.config(bg=self.default_color)
			else:
				self.entry_var_S.set('Nespecificat')
				self.entry_S.config(bg=self.false_validate_color)

		if b != '  ' and a != '':
			if a == '1' or a == '2':
				b = '19' + str(b)
			elif a == '3' or a == '4':
				b = '18' + str(b)
			elif a == '5' or a == '6':
				b = '20' + str(b)
			elif a == '7' or b == '8':
				b = '19' + str(b)
			else:
				b = '19' + str(b)
		else:
			b = '____'
		if c != "  ":
			c = str(c) + '.'
		else:
			c = '__' + '.'
		if d != '  ':
			d = str(d) + '.'
		else:
			d = '__' + '.'
		self.entry_var_ZZLLAA.set('{}{}{}'.format(d, c, b))

		if b =='____' and c =='__.' and d =='__.':
			self.entry_var_ZZLLAA.set('')
			self.entry_ZZLLAA.config(bg=self.default_color)
		elif b =='____' or c =='__.' or d =='__.':
			self.entry_ZZLLAA.config(bg=self.false_validate_color)
		elif self.entry_S.get() != '' and b !='____' and c !='__.' and d !='__.':
			self.entry_ZZLLAA.config(bg=self.true_vaidate_color)

		try:
			self.entry_var_CJ.set(judete[str(e)])
			self.entry_CJ.config(bg=self.true_vaidate_color)
		except:
			if len(self.entry.get()) <=8:
				self.entry_var_CJ.set('')
				self.entry_CJ.config(bg=self.default_color)
			elif len(self.entry.get()) > 8:
				self.entry_var_CJ.set('Invalid ({})'.format(self.entry.get()[7:9]))
				self.entry_CJ.config(bg=self.false_validate_color)


		if str(f) != '  ':
			self.entry_var_XXX.set(str(f))
			self.entry_XXX.config(bg=self.true_vaidate_color)
		else:
			self.entry_var_XXX.set('')
			self.entry_XXX.config(bg=self.default_color)

		if cnp.test_validity() == False and len(self.entry.get()) == 13:
			self.entry_var_C.set(self.entry.get()[-1])
			self.entry_C.config(bg=self.false_validate_color)
		elif cnp.test_validity() == True and len(self.entry.get()) == 13:
			self.entry_var_C.set(self.entry.get()[-1])
			self.entry_C.config(bg=self.true_vaidate_color)
		else:
			self.entry_var_C.set('')
			self.entry_C.config(bg=self.default_color)

	def event_init(self, event):
		self.validate()
		self.explode()


gui = Gui()
