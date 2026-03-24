from tkinter import *

def display():
    if (x.get()==1):
      print(" tkinter is cool!")
    else:
        print(" tkinter is interesting!")
window = Tk()

x = IntVar()
y = IntVar()

def display1():
    if (y.get()==1):
         print("python is cool!")
    else:
        print(" python is interesting!")
checkbox = Checkbutton(window, text="I think :",
                       variable=x, onvalue=1, offvalue=0, command=display)
checkbox.pack()
checkbox.config(font=("Arial", 20))   #change de font
checkbox.config(fg="#993969")#foreground color
checkbox.config(bg="#399699") #background color
checkbox.config(activebackground="pink") #background color
checkbox.config(activeforeground="black") #foreground color

checkbox = Checkbutton(window, text="And maybe :", variable=y, onvalue=1, offvalue=0, command=display1)
checkbox.pack()

#photo=PhotoImage(file='icone.png')
#checkbox.config(image=photo, compound="right"   )
#checkbox.config(padx=35, pady=15, width=100, height=50)


window.mainloop()