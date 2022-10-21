import PySimpleGUI as sg
import math

sg.theme('Reddit')
layout = [[sg.Text('Find the cost of tiles in a floor area!')],
          [sg.Text('Width: '), sg.Input('', key='wtext')],
          [sg.Text('Length: '), sg.Input('', key='ltext')],
          [sg.Text('Cost of 1 tile: '), sg.Input('', key='ctext')],
          [sg.Button('CALCULATE', key='Button')],
          [sg.Text('Area of Room: ', key='AreaAns')],
          [sg.Text('Total Cost of tiles: ', key='CostAns')]]

window = sg.Window('Cost of Tiles', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Button':
        try:
            wvalue = float(values['wtext'])
            lvalue = float(values['ltext'])
            ctext = float(values['ctext'])
            avalue = wvalue * lvalue
            cvalue = avalue * ctext
        except ValueError:
            window["AreaAns"].update(value="Please enter a decimal or number!")
        else:
            window["AreaAns"].update(value="Area of floor: " + str(avalue) + "m²")
            window["CostAns"].update(value="Total cost: $" + str(cvalue))
    print(values, event)
window.close()
