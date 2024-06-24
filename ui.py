from tkinter import *

root = Tk()

# create the board background
canv = Canvas(root, width=1300, height=1500, bg='grey')
canv.grid(row=2, column=3)
img = PhotoImage(file="C://Users//denni//Pictures//field.png")
canv.create_image(20, 20, anchor=NW, image=img)


# Create the Roll button
def button_clicked():
    # Call script here
    # Update the UI
    print("Button clicked!")


# Creating a button with specified options
button = Button(root,
                text="Roll",
                command=button_clicked,
                activebackground="blue",
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=10,
                pady=5,
                width=15,
                wraplength=100)

button.grid(row=2, column=3)

# Todo make a function that shows who is on base & call it at start of every inning & after every button click
mainloop()
