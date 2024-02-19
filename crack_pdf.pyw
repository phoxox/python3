#!python3
"""Summary - To unlock a pdf file without renaming it
"""
import PySimpleGUI as sg
import pikepdf


def crack_pdf_file(file_name):
    """Summary - The actual script to unlock the pdf file"""
    init_pdf = pikepdf.open(file_name)
    new_pdf = pikepdf.new()
    new_pdf.pages.extend(init_pdf.pages)
    new_pdf.save(str(file_name))


# Default settings of the application window
sg.theme("SystemDefault")
sg.set_options(font=("Arial", 16), button_color=("black", "light blue"))

layout = [
    [sg.T("")],
    [sg.Text("Select a pdf file to unlock")],
    [sg.Text("File:", size=(5, 1)),
     sg.Input(), sg.FileBrowse()],
    [
        sg.T("         "),
        sg.Button("Start", size=(8, 1)),
        sg.Button("Exit", size=(8, 1)),
    ],
    [sg.T("")],
    [sg.T("         "),
     sg.Text("", size=(25, 2), key="-COMPLETE-MSG-")],
]

# Setting application window
window = sg.Window(
    "Crack PDF File",
    layout,
    size=(800, 300),
    location=(400, 200),
    resizable=True,
)

# Showing the application, also GUI functions can be placed here.
while True:
    event, values = window.read()
    READ_NAME = str(values[0])
    # READ_NAME => file_name in function
    if event == "Start":
        crack_pdf_file(READ_NAME)
        window["-COMPLETE-MSG-"].update("Finished!", font=("Arial", 28))

    if event in (sg.WIN_CLOSED, "Exit"):
        break

window.close()
