import datetime
import os
from tkinter import *

# import , citire si inchiderea txt-ului

t1_start = datetime.datetime.now()  # start boot count

file_name_to_open = 'brut.txt'
txt_in = open(file_name_to_open, 'r')
txt_out = txt_in.readlines()
txt_in.close()

# initializare dictionar + delimitator oras

main_dic = {}
master_slave_len_delimiter = 29

# inserare elemente in dictionar

temp = ''
for i in txt_out:
	count = 0
	if len(str(i)) > master_slave_len_delimiter:
		main_dic[i] = []
		temp = i
		continue
	main_dic.setdefault(temp, []).append(i.strip('\n'))
	counter = 0

	for a, b in main_dic.items():
		for c in b:
			counter += 1

t1_end = datetime.datetime.now()  # stop boot count


# definirea modulului de interogare + returnare valori

def key_loop(key_in):
	display_vector = []
	display_name = []
	display_value = []
	for j, k in main_dic.items():
		for l in k:
			if re.findall(key_in, l, re.IGNORECASE):
				found_name = re.findall(r'(?!\s)[\w\s-]{3,}', l)
				found_value = re.findall(r'(?![\d\.\s]+).+', j)
				display_name.append(str(found_name).strip('[]\''))
				display_value.append(str(found_value).strip('[]\''))
				display_vector.append('({}) : {}'.format(str(found_name).strip('[]\''),
														 str(found_value).strip('[]\'')))

	return display_name, display_value, display_vector


# initializare GUI (pozitie + geometrie + variabile)

root = Tk()
root.geometry("1180x300")
root.title("IRS Frontend")
root.resizable(0, 0)
root.config(bg="white")
root.config(relief=RIDGE, borderwidth=3)

var_in = StringVar()
entry_in = Entry(root, textvariable=var_in)
entry_in.grid(row=0, column=1, padx=1, pady=1)
entry_in.config(bg='#f2f2f2', width=13, relief=SOLID)
entry_in.config(font="Arial 20 bold",
				justify=CENTER, selectbackground='grey')
var_in.set('')

name_list = Listbox(root)
name_list.grid(row=1, column=0)
name_list.configure(width=25, borderwidth=0, takefocus=0, font="Arial 9 bold",
					justify=RIGHT)

value_list = Listbox(root)
value_list.grid(row=1, column=1)
value_list.configure(width=140, activestyle=NONE, font="Arial 9 bold",
					 justify=CENTER, selectbackground='grey', bg='#f2f2f2', relief=SOLID)

misc_data_var = StringVar()
misc_data = Label(root, textvariable=misc_data_var)
misc_data.grid(row=3, column=0, columnspan=1)
misc_data.configure(borderwidth=4, width=25, bg="white",
					justify=LEFT, font="Arial 9 italic", fg='grey')

misc_data_2_var = StringVar()
misc_data_2 = Label(root, textvariable=misc_data_2_var)
misc_data_2.grid(row=2, column=0, columnspan=1)
misc_data_2.configure(borderwidth=4, width=25, bg="white",
					  justify=LEFT, font="Arial 9 italic", fg='grey')

misc_data_3_var = StringVar()
misc_data_3 = Label(root, textvariable=misc_data_3_var)
misc_data_3.grid(row=4, column=0, columnspan=1)
misc_data_3.configure(borderwidth=4, width=25, bg="white",
					  justify=LEFT, font="Arial 9 italic", fg='grey')

misc_data_4_var = StringVar()
misc_data_4 = Label(root, textvariable=misc_data_4_var)
misc_data_4.grid(row=4, column=1)
misc_data_4.configure(borderwidth=4, width=140, bg="white",
					  justify=LEFT, font="Arial 9 italic", fg='grey')

# atribuirea datelor de debug globale

misc_data_3_var.set("Boot time = {} milliseconds"
					.format(int((t1_end - t1_start).microseconds / 1000)))

misc_data_4_var.set('File opened from : {} ({} kb)'.format(os.path.abspath(file_name_to_open),
														   os.path.getsize(file_name_to_open) / 1000))


# definirea modulului de atribuire a valorilor catre GUI + atribuirea datelor de debug locale

def display_loop(event):
	t1 = datetime.datetime.now()  # start query count

	name_vector, value_vector, merge_vector = key_loop(var_in.get())
	if len(var_in.get()) > 0 and len(var_in.get()) <= 10:
		name_list.delete(0, END)
		value_list.delete(0, END)
		for m in range(len(merge_vector)):
			if m <= 9:
				name_list.insert(m, name_vector[m])
				value_list.insert(m, value_vector[m])
			elif m > 9:
				break
		if len(merge_vector) == 0:
			name_list.insert(0, '"{}" nu este in lista !'.format(var_in.get()))
			value_list.insert(0, '---------' * 10)
	elif len(var_in.get()) > 10:
		name_list.delete(0, END)
		value_list.delete(0, END)
		tmp = var_in.get()
		var_in.set(tmp[0:10])
		name_list.insert(0, '"{}" nu este in lista !'.format(var_in.get()))
		value_list.insert(0, '---------' * 10)
	else:
		name_list.delete(0, END)
		value_list.delete(0, END)

	t2 = datetime.datetime.now()  # stop query count

	misc_data_var.set("Query time = {} milliseconds"
					  .format(int((t2 - t1).total_seconds() * 1000)))
	if len(merge_vector) == counter:
		misc_data_2_var.set("{} / {} elements returned"
							.format('0', counter))
	elif len(merge_vector) != counter:
		misc_data_2_var.set("{} / {} elements returned"
							.format(len(merge_vector), counter))


# definirea modulelor de selectie automata a listei + grafica primara GUI + definirea primei iteratii a timpului de query si nr elemente

def select_list(event):
	value_list.select_set(0)
	value_list.configure(bg='#e6f2ff')


def unselect_list(event):
	value_list.select_clear(0)
	value_list.configure(bg='#f2f2f2')


def focus_entry(event):
	entry_in.configure(bg='#e6f2ff')


def unfocus_entry(event):
	entry_in.configure(bg='#f2f2f2')


value_list.bind("<FocusIn>", select_list)
value_list.bind("<FocusOut>", unselect_list)
entry_in.bind('<FocusIn>', focus_entry)
entry_in.bind('<FocusOut>', unfocus_entry)

misc_data_var.set("Query time = {} milliseconds"
					  .format(0))
misc_data_2_var.set("{} / {} elements returned"
							.format('0', counter))

# definirea conditiei de update a GUI + crearea buclei principale a frameului "root"
entry_in.bind("<KeyRelease>", display_loop)
root.mainloop()
