from tkinter import *

class App:
	def __init__(self,co):
		self.co = co
		self.root = Tk()

		self.entry_in = Entry(self.root)
		self.entry_in.bind("<KeyRelease>", self.push_me)
		self.entry_in.pack()



		self.root.mainloop()
	def push_me(self,event=None):
		self.co +=1
		print(self.co)



