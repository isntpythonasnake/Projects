# NUMBERS | Find PI to the Nth Digit
import PySimpleGUI as sg
import math

sg.theme('Reddit')
layout = [[sg.Text('Find Pi to the Nth Digit')],
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
        pi = math.pi
        result = round(pi, int(inputText))
        window["ans"].update(value=str("Rounded Pi: " + str(result)))
window.close()
