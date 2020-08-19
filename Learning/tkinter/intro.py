from tkinter import *

page = Tk()
page.title("Nihal")


def click():
	label = Label(page, text="CLICKED").pack()


lab1 = Label(page, text="Typing is permitted!").pack()
entry = Entry(page).pack()
button = Button(page, text="Here it is!", command=click, fg="red", bg='#ffb3fe').pack()
print(entry)
page.mainloop()