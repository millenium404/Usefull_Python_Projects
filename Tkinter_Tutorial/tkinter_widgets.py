from tkinter import *
# PIL Image Class is conflicting with Tkinter Image Class, so import like this:
import PIL as pil

root = Tk()
root.title('Some cool stuff in here')
# Can't get the icon stuff working for now
# root.iconbitmap('/some_path_in_here/favico.ico')

# Creating Frames
frame_1 = LabelFrame(root, text='First Frame in here', padx=50, pady=50)
frame_1.grid(row=0, column=0, padx=10, pady=10)
button = Button(frame_1, text='Dont Click!')
button.grid(row=1, column=3)
button2 = Button(frame_1, text='Dont Click!')
button2.grid(row=2, column=2)

# Creating Radio Buttons
frame_2 = LabelFrame(root, text='Second Frame in here', padx=50, pady=50)
frame_2.grid(row=1, column=0, padx=10, pady=10)
r = IntVar() # Tkinter internal Variable
r.set('2')

modes = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion'),
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in modes:
    Radiobutton(frame_2, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    radioLabel = Label(frame_2, text=value)
    radioLabel.pack()

# Radiobutton(
#     frame_2, text='Option 1', variable=r, value=1, command=lambda: clicked(
#         r.get())).pack()

submit_button = Button(frame_2, text='Submit', command=lambda: clicked(pizza.get()))
submit_button.pack()

root.mainloop()