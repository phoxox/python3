#!python3
"""
Summary - unlock microsoft Excel files
Attributes:
    layout (TYPE): window layout
    window (TYPE): PySimpleGUI window
"""
from subprocess import run, Popen
import PySimpleGUI as sg

sg.theme('SystemDefault')
sg.set_options(font=("Arial", 16), button_color=('black', 'light blue'))

# Both radio buttons are in the same "RADIO1" group,
# so only one of them can be selected.
layout = [
    [sg.T("")],
    [sg.Text('Select a file to unlock/unprotect')],
    [sg.Text('File:', size=(5, 1)),
     sg.Input(), sg.FileBrowse()],
    [
        sg.T("         "),
        sg.Radio('Unlock Worksheet', "RADIO1", default=True, key='--worksheet')
    ],
    [
        sg.T("         "),
        sg.Radio('Unlock Workbook', "RADIO1", default=False, key='--workbook')
    ],
    [
        sg.T("         "),
        sg.Checkbox('Unprotect VBA Project', default=False, key='--vba')
    ],
    [sg.T("")],
    [
        sg.T("         "),
        sg.Button('Start', size=(8, 1)),
        sg.Button('Exit', size=(8, 1))
    ],
    [sg.T("")],
    [sg.T("         "),
     sg.Text("", size=(55, 2), key='-COMPLETE-MSG-')],
]

# Setting Window
window = sg.Window('Crack Excel File',
                   layout,
                   size=(800, 450),
                   location=(400, 200),
                   resizable=True)

# Showing the Application, also GUI functions can be placed here.
while True:
    event, values = window.read()
    ARG = ""
    if values['--worksheet'] is True:
        ARG = ARG + " " + "-ws"
    if values['--workbook'] is True:
        ARG = ARG + " " + "-wb"
    if values['--vba'] is True:
        ARG = ARG + " " + "-vba"

    FILE_NAME = str(values[0])
    # final_ARG = '"{}"'.format(FILE_NAME) + " " + ARG

    if event == 'Start':
        result = run("py craxcel.py " + f'"{FILE_NAME}"' + " " + ARG,
                     capture_output=True,
                     text=True,
                     check=False,
                     shell=True)
        # executes a command and waits for it to finish
        # "py craxcel.py " + '"{}"'.format(FILE_NAME) + " " + ARG,
        # f-string or format() to take care the spaces in name file
        sg.popup("Result:", result.stdout)
        # move the cracked file to folder c:\downloads
        # execution of a program as a child process
        with Popen('cmd /c "move unlocked\\*.* c:\\downloads"',
                   shell=True) as proc:
            print("moving the file")  # just do something
        # shutil.move("unlocked\\*.*", "c:\\downloads")
        window['-COMPLETE-MSG-'].update(
            'Cracked file has been moved to c:\\downloads', font=("Arial", 16))

    # if event == sg.WIN_CLOSED or event == "Exit":
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
