from tkinter import *

root = Tk()

def onClick():
    myLabel = Label(root, text = 'Hey! The button was just clicked!')
    myLabel.grid(row=4, column=0)

myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My Name is Manfred Kurtz')
myButton = Button(root, text='Click Me!', command=onClick)
myButton2 = Button(root, text='Click Me!', state=DISABLED, padx=50, pady=25)

# myLabel1.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=3, column=0)
myButton2.grid(row=5, column=0)


root.mainloop()