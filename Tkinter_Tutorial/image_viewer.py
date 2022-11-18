import os
from PIL import ImageTk, Image
from tkinter import Tk, Button, Label

current_index = 0

root = Tk()
root.title('Image Viewer')

img_dir = f'{os.path.abspath(os.getcwd())}/img'
files_list = [f'{file}' for file in os.listdir(img_dir) if '.png' in file]

img_list = []
for file in files_list:
    img = Image.open(f'img/{file}')
    img = ImageTk.PhotoImage(img)
    img_list.append(img)

labels_list = []
for img in img_list:
    label = Label(root, image=img)
    labels_list.append(label)


def move(idx=0):
    if idx >= len(labels_list) or idx < 0:
        idx = 0
    global current_index
    global my_label
    my_label.grid_remove()
    current_index = idx
    my_label = labels_list[current_index]
    my_label.grid(row=1, column=0, columnspan=3)


my_label = labels_list[current_index]
my_label.grid(row=1, column=0, columnspan=3)

button_back = Button(
    root, text='<<', command=lambda: move(current_index - 1))
button_quit = Button(
    root, text='Quit', command=root.quit)
button_forward = Button(
    root, text='>>', command=lambda: move(current_index + 1))

button_back.grid(row=0, column=0)
button_quit.grid(row=0, column=1)
button_forward.grid(row=0, column=2)

root.mainloop()