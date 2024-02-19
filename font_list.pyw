#!python3
"""Summary - List all the fonts_list
Attributes:
    display (TYPE): listbox
    fonts_list (TYPE): all available fonts_list
    root (TYPE): window
    scroll (TYPE): scrollbar
"""
import sys
from tkinter import Tk, Listbox, Scrollbar
from tkinter import font
from tkinter import BOTH, YES, NO, LEFT, RIGHT, END, Y

root = Tk()
root.title("Font Families")
root.option_add("*Font", "Helvetica 14")
root.wm_minsize(380, 250)

fonts_list = list(font.families())
fonts_list.sort()

# remove fonts begin with '@' from the list
prefixes = ["@"]
fonts_list = [
    select for select in fonts_list
    if not any(prefix in select for prefix in prefixes)
]

display = Listbox(root)
display.pack(fill=BOTH, expand=YES, side=LEFT)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y, expand=NO)

scroll.configure(command=display.yview)
display.configure(yscrollcommand=scroll.set, background="light yellow")

for item in fonts_list:
    display.insert(END, item)

# show window
# root.mainloop()
if __name__ == "__main__":
    sys.exit(root.mainloop())
