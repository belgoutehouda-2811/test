from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    try:
        selection = x.get()
        if selection == 0:
            print("You ordered pizza!")
        elif selection == 1:
            print("You ordered hamburger!")
        elif selection == 2:
            print("You ordered hotdog!")
        else:
            print("Please select your order!")
    except TclError:
        print("Please select your order!")

window = Tk()
window.title("Food Order System")

# Load images with error handling
try:
    pizzaImage = PhotoImage(file='pizza.png')
except TclError:
    print("Warning: pizza.png not found, using placeholder")
    pizzaImage = PhotoImage()  # Empty image as fallback

try:
    hamburgerImage = PhotoImage(file='hamburger.png')
except TclError:
    print("Warning: hamburger.png not found, using placeholder")
    hamburgerImage = PhotoImage()

try:
    hotdogImage = PhotoImage(file='hotdog.png')
except TclError:
    print("Warning: hotdog.png not found, using placeholder")
    hotdogImage = PhotoImage()

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar(value=-1)  # Set default value to -1 (no selection)

# Create a label for instructions
Label(window, text="Select your food:", font=("Arial", 16)).pack(pady=10)

for index in range(len(food)):
    radiobutton = Radiobutton(
        window,
        text=food[index].capitalize(),  # Capitalize food names
        variable=x,
        value=index,
        padx=20,
        font=("Arial", 14),  # Changed from Impact to more common Arial
        image=foodImages[index],
        compound='left',
        indicatoron=0,
        width=300,  # Slightly reduced width
        height=60,  # Added height for better appearance
        command=order,
        anchor='w'  # Align text to the left west
    )
    radiobutton.pack(anchor=W, padx=20, pady=5)

# Add a separator
Label(window, text="-" * 50).pack(pady=10)

# Add a quit button
Button(window, text="Quit", font=("Arial", 14),
       command=window.destroy, bg="red", fg="white",
       width=20).pack(pady=10)

window.mainloop()