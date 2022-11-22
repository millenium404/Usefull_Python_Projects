import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Some cool stuff in here')
mwidth = root.winfo_screenwidth() # Get screen resolution
mheight = root.winfo_screenheight() # Get screen resolution
root.geometry(f'{mwidth}x{mheight}') # Set main window size
base_dir = os.path.abspath(os.getcwd())
# Can't get the icon stuff working for now
# root.iconbitmap('/some_path_in_here/favico.ico')

# Creating Frames, Messageboxes and Windows
# Types: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno('This is my Popup!', 'Hello World')
    print(response) # 'askyesno' returns True or False
    Label(frame_1, text=response).grid(row=3, column=0, columnspan=3)
    if response is True:
        Label(frame_1, text='You clicked Yes!').grid(
            row=3, column=0, columnspan=3)
    else:
        Label(frame_1, text='You clicked No!').grid(
            row=3, column=0, columnspan=3)


def open_image():
    global top, my_img
    top.filename = filedialog.askopenfilename(
        initialdir=base_dir,
        title='Select a File',
        filetypes=(('JPEG files', '*.jpg'), ('PNG files', '*.png'))
        )
    filepath = Label(top, text=top.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(top.filename))
    img_label = Label(top, image=my_img).pack()


def open_window():
    # if opening an image file in function, make the 'my_img' variable global!
    global top
    top = Toplevel()
    top.title('Image Window')
    top.geometry(f'{mwidth // 2}x{mheight // 2}')
    button_open = Button(top, text='Open Image', command=open_image).pack()
    button_close = Button(top, text='Close', command=top.destroy).pack()


frame_1 = LabelFrame(root, text='First Frame in here', padx=50, pady=50)
frame_1.grid(row=0, column=0, padx=10, pady=10)
button_popup = Button(frame_1, text='Popup!', command=popup)
button_popup.grid(row=1, column=3)
button_nwindow = Button(frame_1, text='New Window', command=open_window)
button_nwindow.grid(row=2, column=2)


# Creating Radio Buttons and CheckBoxes
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

# Checkbutton(frame_2, text='Check this box!', variable=r).pack(anchor=W)

submit_button = Button(frame_2, text='Submit', command=lambda: clicked(pizza.get()))
submit_button.pack()

root.mainloop()