import PySimpleGUI as sg
import pyperclip
import os
import getpass
import json

u = getpass.getuser()

text_saved = []

f = open(f"/home/{u}/.config/clipboard.json", "a+")

dictionary = {'clipboard':[]}
jsonString = json.dumps(dictionary, indent=4)

if(f.read(1) != "{"):
    f.write(jsonString)
    f.close()
else:
    z = f.read()
    f.close()

nf = open(f"/home/{u}/.config/clipboard.json", "a+")

json_clipboard = nf.read()
print(json_clipboard)

def process_values(value):
    text_saved.append(value)
    print(text_saved)
    print(os.path.realpath(__file__))

sg.theme('Dark Blue 3')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pasty', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if(len(text_saved) <= 10):
        text_clipboard = pyperclip.paste()
        process_values(text_clipboard)
        text_clipboard = ''
    #print('You entered ', values[0][0])
    print(text_saved)
    
window.close()
f.close()
