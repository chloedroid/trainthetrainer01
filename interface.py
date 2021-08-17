from tkinter import *
from tkinter import messagebox


app = Tk()

def ditinfo():
    info = Label(app, text="DIT = Data Interventie Team", font=('Comic Sans', 18, 'bold'))
    info.grid(row=2, column=1)

DIT = Button(app, text="Your name?", command=ditinfo)
DIT.grid(row=1, column=1)

app.title"Probeersel"
app.configure(bg="red")

app.mainloop()






