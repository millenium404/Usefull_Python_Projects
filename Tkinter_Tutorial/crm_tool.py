import os
from tkinter import *



root = Tk()
root.title('Some cool stuff in here')
mwidth = int(root.winfo_screenwidth() // 3) # Get screen resolution
mheight = int(root.winfo_screenheight() // 1.5) # Get screen resolution
root.geometry(f'{mwidth}x{mheight}') # Set main window size
# root.configure(background='white')
base_dir = os.path.abspath(os.getcwd())




root.mainloop()