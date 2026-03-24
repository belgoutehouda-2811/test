from tkinter import *



def submit():
    username  = entry.get()
    print("Hello"+ username)

def delete():
    entry.delete(0, END) #deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character
window = Tk()
submit=Button(window, text="Submit", command=submit)
submit.pack(side=RIGHT)

delete =Button(window, text="Delete", command=delete)
delete.pack(side = RIGHT)

backspace =Button(window, text="backspase", command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=("calibri", 20))
entry.config(bg="white")
entry.config(fg="#7f9939")
entry.insert(0,'Python')
#entry.config(state=DISABLED)
entry.config(width=10)
entry.pack()
window.mainloop()