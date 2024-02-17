#!C:\Python312\python.exe
#!python3
"""
Summary - random password generator
"""
import sys
import random
from tkinter import Tk, Label, Entry, Button, END
import pyperclip

# function for generation of password, length is 8 (chars)
UPPERCASE_CHARS = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # without IO
LOWERCASE_CHARS = "abcdefghijkmnpqrstuvwxyz"  # without lo
DIGITS_CHARS = "23456789"  # without 10
SPECIAL_CHARS = "!@#$%^&*"


def get_random_password():
    """
    Summary - Function for generation of password, length is 10 (chars)
    Returns:
        TYPE: new password
    """
    pass_length = 10
    password1 = random.choice(UPPERCASE_CHARS)  # only one uppercase
    password2 = random.choice(LOWERCASE_CHARS)  # one lowercase
    password3 = random.choice(DIGITS_CHARS)  # one digit
    password4 = random.choice(SPECIAL_CHARS)  # only one special char
    random_source = LOWERCASE_CHARS + DIGITS_CHARS
    remove_chars = [password2, password3]  # remove the picked chars
    for item_x in remove_chars:
        random_source = random_source.replace(item_x, "")
    # pick 6 non-repeated chars
    random_str = "".join(random.sample(random_source, pass_length - 4))
    new_password = password2 + password3 + password4 + random_str
    password_list = list(new_password)  # convert str to list
    random.SystemRandom().shuffle(password_list)  # randomize the list
    new_password = "".join(password_list)  # convert list to string
    new_password = password1 + new_password  # 1st char is uppercase
    pyperclip.copy(new_password)  # copy to clipboard
    return new_password


def generate_pw():
    """Summary - function for generation of password"""
    entry.delete(0, END)
    password1 = get_random_password()
    entry.insert(0, password1)


def copy_pw():
    """Summary - function for copying password to clipboard"""
    random_password = entry.get()
    pyperclip.copy(random_password)


def close_window():
    """Sumary - destroying the main window"""
    root.destroy()


# create GUI window
root = Tk()
root.wm_attributes("-topmost", 1)
root.title("Python - Password Generator")
root.wm_minsize(380, 250)
root.option_add("*Font", "Helvetica 12")
root.configure(background="light yellow")

# create label and entry to show password generated
Title1 = Label(root, text="\n", background="light yellow")
Title1.grid(row=1, column=1)

Random_password = Label(root, text="Password: ", background="light yellow")
Random_password.grid(row=2, column=1)

entry = Entry(root, width=12, font="Consolas 22 bold", justify="center")
entry.grid(row=2, column=2)

Title2 = Label(root, text="\n\n", background="light yellow")
Title2.grid(row=4, column=1)

# create buttons Copy which will copy password to clipboard
# Generate which will generate the password
generate_button = Button(root, text="Generate", command=generate_pw)
generate_button.grid(row=4, column=2)

copy_button = Button(root, text="Copy to clipboard", command=copy_pw)
copy_button.grid(row=5, column=2)

exit_button = Button(root, text="Exit", command=close_window)
exit_button.grid(row=6, column=3)

# start the GUI
# root.mainloop()
if __name__ == "__main__":
    sys.exit(root.mainloop())
