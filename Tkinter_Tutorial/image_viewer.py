import os
from PIL import ImageTk, Image
import tkinter as tk

root = tk.Tk()
root.title('Image Viewer')

img_dir = f'{os.path.abspath(os.getcwd())}/img'
files_list = [f'{file}' for file in os.listdir(img_dir) if '.jpg' in file]

img_list = []
for file in files_list:
    img = Image.open(f'img/{file}')
    img = ImageTk.PhotoImage(img)
    img_list.append(img)

labels_list = []
for img in img_list:
    label = tk.Label(root, image=img)
    labels_list.append(label)


def create_buttons():
    global current_index
    button_back = tk.Button(
        root, text='<<', command=lambda: move(current_index - 1))
    button_quit = tk.Button(
        root, text='Quit', command=root.quit)
    button_forward = tk.Button(
        root, text='>>', command=lambda: move(current_index + 1))
    button_back.grid(row=0, column=0)
    button_quit.grid(row=0, column=1)
    button_forward.grid(row=0, column=2)


def change_statusbar():
    global status
    try:
        status.grid_remove()
    except:
        pass
    status = tk.Label(
        root, 
        text=f'Image {current_index + 1} of {len(labels_list)}',
        bd=1,
        relief=tk.SUNKEN)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.E+tk.W)


def move(idx=0):
    global current_index, my_label
    if idx >= len(labels_list) or idx < 0:
        idx = 0
    try:
        my_label.grid_remove()
    except:
        pass
    current_index = idx
    my_label = labels_list[current_index]
    my_label.grid(row=1, column=0, columnspan=3)
    change_statusbar()


create_buttons()
move()
root.mainloop()