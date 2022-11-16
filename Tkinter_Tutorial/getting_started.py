from tkinter import *

root = Tk()

def onClick():
    hello = f'Hello, {e.get()}!'
    myLabel = Label(root, text=hello)
    myLabel.grid(row=4, column=0)

myLabel1 = Label(root, text='Hello World!')
# myLabel2 = Label(root, text='My Name is Manfred Kurtz')
myButton = Button(root, text='Submit', command=onClick)
myButton2 = Button(root, text='Click Me!', state=DISABLED, padx=50, pady=25)

e = Entry(root, width=50)
e.insert(0, 'Enter Your Name: ')
e.grid(row=0, column=0)
myLabel1.grid(row=1, column=0)
# myLabel2.grid(row=2, column=0)
myButton.grid(row=3, column=0)
myButton2.grid(row=5, column=0)


root.mainloop()