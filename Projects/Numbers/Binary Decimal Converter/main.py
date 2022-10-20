import PySimpleGUI as sg

sg.theme('Reddit')
layout = [[sg.Text('Convert Binary to Decimal and back!')],
          [sg.Text('Decimal: '), sg.Input('', key='dtext')],
          [sg.Text('Binary: '), sg.Input('', key='btext')],
          [sg.Button('Convert Decimal', key='DtoBButton'), sg.Button('Convert Binary', key='BtoDButton')],
          [sg.Text('The answer will display here!', key='ans')]
          ]

window = sg.Window('Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'DtoBButton':
        dvalue = int(values['dtext'])
        result = bin(dvalue)
        window["ans"].update(value=str(result).replace("0b", "Answer: "))
    elif event == 'BtoDButton':
        bvalue = values['btext']
        result = int(bvalue, 2)
        window["ans"].update(value="Answer: " + str(result))

window.close()
