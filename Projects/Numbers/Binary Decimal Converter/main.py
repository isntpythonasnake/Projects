import PySimpleGUI as sg

sg.theme('Reddit')
layout = [[sg.Text('Convert Binary to Decimal and back!')],
          [sg.Radio('Binary', key='radio1', group_id=1), sg.Radio('Decimal', key='radio2', group_id=1)],
          [sg.Text('Input: '), sg.Input('', key='itext')],
          [sg.Button('CONVERT', key='Button'), sg.Text('The answer will display here!', key='ans')]]

window = sg.Window('Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Button' and values['radio1'] and not values['radio2']:
        value = int(values['itext'])
        result = bin(value)
        window["ans"].update(value=str(result).replace("0b", "Answer in Binary: "))
    elif event == 'Button' and values['radio2'] and not values['radio1']:
        value = values['itext']
        result = int(value, 2)
        window["ans"].update(value="Answer in Decimal: " + str(result))
    print(values, event)
window.close()
