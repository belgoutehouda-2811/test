from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if (x.get()==0):
         print("You ordered pizza!")
    elif (x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("select your order please!")

window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]
x= IntVar()
for index  in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],  #Add texts

                              variable=x , #groups radiobuttons together 
                              #if they share
                               # the same variables
                              value = index     , #assigns each radiobutton 
                              #a different value
                              padx= 20 ,
                              font=("impact",50),
                              image=foodImages[index],#adds image to radiobutton
                              compound= 'left' , #adds image § text(left-side
                              indicatoron=0 , # eliminate circle indicators
                              width = 375, #sets width of radio buttons
                              command=order #set command of radiobutton to funtion
                              )
    radiobutton.pack(anchor=W)
window.mainloop()