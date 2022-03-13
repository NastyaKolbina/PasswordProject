import tkinter
import random
from tkinter import *

chars = '`1234567890-=\\~!@#$%^&*()_+|qwertyuiop[]QWERTYUIOP{}asdfghjkl;\'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>? '
chars_option2 = '1234567890qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM'

window = Tk()
window.title("PasswordGenerator")
window.geometry("350x350+450+150")
window.resizable(False, False)
window.configure(background="white")

lbl = Label(window,
            text="Generator's settings",
            justify=CENTER,
            background="white")
lbl.config(font=("Arial", 15))
lbl.place(x=85, y=5)

p_numbers = IntVar()
numbers_checkbutton = Checkbutton(text="Numbers",
                                  variable=p_numbers,
                                  onvalue=1,
                                  offvalue=0,
                                  background="white")
numbers_checkbutton.config(font=("Arial", 12))
numbers_checkbutton.place(x=20, y=45)

l_case = IntVar()
lowercase = Checkbutton(text="Lower case",
                        variable=l_case,
                        onvalue=1,
                        offvalue=0,
                        background="white")
lowercase.config(font=("Arial", 12))
lowercase.place(x=20, y=85)

u_case = IntVar()
uppercase = Checkbutton(text="Upper case",
                        variable=u_case,
                        onvalue=1,
                        offvalue=0,
                        background="white")
uppercase.config(font=("Arial", 12))
uppercase.place(x=20, y=125)

symbols = IntVar()
symbols_checkbutton = Checkbutton(text="Symbols",
                                  variable=symbols,
                                  onvalue=1,
                                  offvalue=0,
                                  background="white")
symbols_checkbutton.config(font=("Arial", 12))
symbols_checkbutton.place(x=20, y=165)

lbl = Label(window,
            text="Length of password:",
            background="white")
lbl.configure(font=("Arial", 10))
lbl.place(x=20, y=210)

txt = Entry(window, width=10)
txt.place(x=150, y=210)


def clicked():
    if p_numbers.get() == 0 and l_case.get() == 0 and u_case.get() == 0 and symbols.get() == 0 or txt.get() == '':
        warning = Tk()
        warning.title('warning')
        warning.geometry("320x80+470+370")
        warning_label = Label(warning
                              , text="Choose options or length",
                              font=("ArialBold", 20))
        warning_label.place(x=5, y=20)
    else:
        get_length = txt.get()
        window.destroy()
        second_window = Tk()
        second_window.title("secwin")
        second_window.geometry("350x200+470+370")
        second_window.config(background="white")
        sec_lbl = Label(second_window,
                        text="Choose password",
                        background="white")
        sec_lbl.configure(font=("Arial", 12))
        sec_lbl.place(x=100, y=5)
        third_txt = Entry(second_window, font=10, bd=0)
        third_txt.place(y=30)
        fourth_label = Entry(second_window, font=10, bd=0, background="white")
        fourth_label.place(y=60)
        fifth_label = Entry(second_window, font=10, bd=0, background="white")
        fifth_label.place(y=90)
        six_label = Entry(second_window, font=10, bd=0,background="white")
        six_label.place(y=120)

        password = ''
        sec_pas = ''
        third_pas = ''
        fourth_pas = ''

        if p_numbers.get() == 1 and l_case.get() == 1 and u_case.get() == 1 and symbols.get() == 1:
            for i in range(int(get_length)):
                password += random.choice(chars)
            third_txt.insert(0, password)
            third_txt.config(state="readonly")
            for i in range(int(get_length)):
                sec_pas += random.choice(chars)
            fourth_label.insert(0, sec_pas)
            fourth_label.config(state="readonly")
            for i in range(int(get_length)):
                third_pas += random.choice(chars)
            fifth_label.insert(0, third_pas)
            fifth_label.config(state="readonly")
            for i in range(int(get_length)):
                fourth_pas += random.choice(chars)
            six_label.insert(0, fourth_pas)
            six_label.config(state="readonly")

        elif p_numbers.get() == 1 and l_case.get() == 1 and u_case.get() == 1:
            for i in range(int(get_length)):
                password += random.choice(chars_option2)
            third_txt.insert(0, password)
            third_txt.config(state="readonly")
            for i in range(int(get_length)):
                sec_pas += random.choice(chars_option2)
            fourth_label.insert(0, sec_pas)
            fourth_label.config(state="readonly")
            for i in range(int(get_length)):
                third_pas += random.choice(chars_option2)
            fifth_label.insert(0, third_pas)
            fifth_label.config(state="readonly")
            for i in range(int(get_length)):
                fourth_pas += random.choice(chars_option2)
            six_label.insert(0, fourth_pas)
            six_label.config(state="readonly")


btn = Button(text="Create password", font="5", padx=40, background="#c2c6cc", command=clicked)
btn.place(x=45, y=285)

window.mainloop()
