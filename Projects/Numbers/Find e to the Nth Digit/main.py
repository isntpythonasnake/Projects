# NUMBERS | Find PI to the Nth Digit
import PySimpleGUI as sg
import math

sg.theme('Reddit')
layout = [[sg.Text('Find e to the Nth Digit')],
          [sg.Text('Input Nth Digit: '), sg.Input('', key='itext')],
          [sg.Button('SUBMIT', key='Button'), sg.Text('The answer will display here!', key='ans')]]

window = sg.Window('e to the Nth Digit', layout)
while True:
    event, values = window.read()
    inputText = values['itext']
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Button' and not inputText.isdigit() or inputText == '' or int(inputText) <= 0 or int(inputText) >= 12:
        window["ans"].update(value=str("Please enter an integer larger than 0 and smaller than 12!"))
    else:
        e = math.e
        result = round(e, int(inputText))
        window["ans"].update(value=str("Rounded e: " + str(result)))
window.close()
