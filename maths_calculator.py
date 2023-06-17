import PySimpleGUI as sg 
from lib.functions import bin_expand, combinations_q  

sg.theme('DarkAmber')

def getLabelledInputBox(box_name, tag_name):
    return [sg.Text(f'{box_name}: ', size = (15, 1)), sg.Input(key = f'-{tag_name}-')]
   
def gui():
    layout1 = [[sg.Text('Welcome to our maths calculator! What would you like to calculate?')],
               [sg.Button('Combinations'), sg.Button('Binomial expansion')],
               [],
               [sg.Button('Exit')]]

    layout2 = [[sg.Text('Calculating combinations. Your result: '), sg.Text(key = '-COM-')],
               getLabelledInputBox('Total', 'TOT'),
               getLabelledInputBox('Choose', 'CHO'),
               [sg.Button('Calculate', key = '-C1-')],
               [sg.Button('Back')]] 

    layout3 = [[sg.Text('Expanding a binomial.')],
               getLabelledInputBox('a', 'A'),
               getLabelledInputBox('b', 'B'),
               getLabelledInputBox('Power', 'POW'),
               [sg.Button('Calculate', key = '-C2-'), sg.Button('Back')], 
               [sg.Text('The binomial expansion is: '), sg.Text(key = '-BIN-')]]
               
    
    layout = [[sg.Column(layout1, key = '-DEF-'), sg.Column(layout2, key = '-COL2-', visible = False), sg.Column(layout3, key = '-COL3-', visible = False)]]

    window = sg.Window('WolframSigma', layout)

    curr_layout  = 1
    while True:
        event, values = window.read()
        print(event, values)

        if event in ('Exit', None):
            break 

        if event == 'Combinations':
            window['-DEF-'].update(visible = False)
            window['-COL2-'].update(visible = True)
            curr_layout = 2 

        if event == '-C1-':
            window['-COM-'].update(combinations_q(values['-TOT-'], values['-CHO-']))
        
        if 'Back' in event: 
            window[f'-COL{curr_layout}-'].update(visible = False)
            window['-DEF-'].update(visible = True)
            curr_layout = 1 

        if event == 'Binomial expansion':
            window['-DEF-'].update(visible = False)
            window['-COL3-'].update(visible = True)
            curr_layout = 3

        if event == '-C2-':
            window['-BIN-'].update(bin_expand(int(values['-A-']), int(values['-B-']), int(values['-POW-'])))

if __name__ == '__main__':
    gui()