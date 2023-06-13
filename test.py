import PySimpleGUI as sg

layout = [[sg.Text('This is a test. Please write something.')],
          [sg.Input(key='-IN-')],
          [sg.Button('Read'), sg.Exit()],
          [sg.Text(key = '-TXT-')]]

window = sg.Window('test', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Read':
        window['-TXT-'].update(values['-IN-'])

window.close()