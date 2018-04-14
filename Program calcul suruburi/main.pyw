from tkinter import *

root = Tk()
root.geometry("335x200")
root.title("Calculator suruburi")
root.resizable(0, 0)
root.config(bg="white")
root.config(relief=RIDGE, borderwidth=3)

grame_1_var = DoubleVar()
grame_per_um = Entry(root, textvariable=grame_1_var)
grame_per_um.grid(row=0, column=0, padx=10, pady=10)
grame_per_um.config(bg="#33CCFF", justify=CENTER, width=11, relief=SUNKEN, borderwidth=2)
grame_per_um.config(font="Arial 16 bold")
grame_1_var.set(0)

label_per = Label(root, text="grame per")
label_per.grid(row=0, column=1)
label_per.config(font="Arial 10 bold", bg="white")

label_per = Label(root, text="buc")
label_per.grid(row=0, column=3)
label_per.config(font="Arial 10 bold", bg="white")

spinbox_default_var = DoubleVar()
spinbox_default_var.set(10)
spinbox = Spinbox(root, from_=1, to=99, textvariable=spinbox_default_var)
spinbox.grid(row=0, column=2, padx=10)
spinbox.config(width=2, font="Arial 16 bold", bg="#33CCFF", justify=CENTER)

line_label = Label(root, text="______________________________________________________________")
line_label.grid(row=1, columnspan=4)
line_label.config(justify=CENTER, bg="white")

label_per_3 = Label(root, text="Grame total")
label_per_3.grid(row=2, columnspan=5)
label_per_3.config(font="Arial 10 bold", bg="white")

grame_2_var = DoubleVar()
grame_2_var.set(0)
grame_brut = Entry(root, textvariable=grame_2_var)
grame_brut.grid(row=3, columnspan=4, padx=10, pady=10)
grame_brut.config(bg="#33CCFF", justify=CENTER, width=10, relief=SUNKEN, borderwidth=2)
grame_brut.config(font="Arial 20 bold")

grame_3_var = IntVar()
grame_total_label = Label(root, textvariable=grame_3_var)
grame_total_label.grid(row=4, columnspan=4, padx=10, pady=10)
grame_total_label.config(bg="white", justify=CENTER, width=20, relief=RIDGE, borderwidth=3)
grame_total_label.config(font="Arial 16 bold")


def set_me():
    try:
        main_var = spinbox_default_var.get() * grame_2_var.get() / grame_1_var.get()
        root.after(200, set_me)

        if main_var >= 1 and main_var < 2:
            grame_3_var.set("= " + str(int(round(main_var, 0))) + " bucata")
        elif main_var > 2:
            grame_3_var.set("= " + str(int(round(main_var, 0))) + " bucati")
        elif main_var > 0 and main_var < 1:
            grame_3_var.set("mai putin de 1 bucata ???")
        else:
            grame_3_var.set("nici o bucata")

        grame_total_label.config(bg="white")
        grame_per_um.config(bg="#33CCFF")
        grame_brut.config(bg="#33CCFF")
        spinbox.config(bg="#33CCFF")
    except:
        root.after(200, set_me)
        grame_3_var.set("N/A")
        grame_total_label.config(bg="#FF5247")

        try:
            grame_1_var.get() - 1
        except:
            grame_per_um.config(bg="#FF5247")

        try:
            grame_2_var.get() - 1
        except:
            grame_brut.config(bg="#FF5247")
        try:
            spinbox_default_var.get() - 1
            if spinbox_default_var.get() > 0 and spinbox_default_var.get() < 100:
                spinbox.config(bg="#33CCFF")
            else:
                spinbox.config(bg="#FF5247")
        except:
            spinbox.config(bg="#FF5247")
root.after(200, set_me)
root.mainloop()
