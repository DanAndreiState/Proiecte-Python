import tkinter as tk
from tkinter import filedialog
import os


def open_file_dialog():
	root = tk.Tk()
	root.withdraw()
	try:
		file_path = filedialog.askopenfilename(
			filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
			initialdir=os.path.dirname(os.path.abspath(__file__)),
			title = "Selectati fisierul CSV !"
		)
		return file_path
	except Exception as e:
		print(e)
		exit()