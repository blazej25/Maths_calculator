import PySimpleGUI as sg 
from lib.functions import bin_expand, combinations_q  
from lib.save import read, save, clear

sg.theme('DarkAmber')

def getLabelledInputBox(box_name, tag_name):
    return [sg.Text(f'{box_name}: ', size = (15, 1)), sg.Input(key = f'-{tag_name}-')]

def twoOptions(opt1, opt2, text):
    layout = [[sg.Text(f'{text}', size = (15, 1))], [sg.Button(f'{opt1}'), sg.Button(f'{opt2}')]]
    
    return layout
   
def gui():
    layout1 = [[sg.Text('Welcome to our maths calculator! What would you like to calculate?')],
               [sg.Button('Combinations'), sg.Button('Binomial expansion')],
               [sg.Text('')],
               [sg.Button('History'), sg.Button('Exit')]]

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

    layout4 = [[sg.Text('Here are your last ten results:')],
               [sg.Text(key = '-MEM-')],
               [sg.Button('Clear'), sg.Button('Back')]]

    layout = [[sg.Column(layout1, key = '-DEF-'), 
               sg.Column(layout2, key = '-COL2-', visible = False), 
               sg.Column(layout3, key = '-COL3-', visible = False), 
               sg.Column(layout4, key = '-COL4-', visible = False)]]

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
            r1 = combinations_q(values['-TOT-'], values['-CHO-'])
            window['-COM-'].update(r1)
            save('Combinations', r1)
        
        if 'Back' in event: 
            window[f'-COL{curr_layout}-'].update(visible = False)
            window['-DEF-'].update(visible = True)
            curr_layout = 1 

        if event == 'Binomial expansion':
            window['-DEF-'].update(visible = False)
            window['-COL3-'].update(visible = True)
            curr_layout = 3

        if event == '-C2-':
            r2 = bin_expand(int(values['-A-']), int(values['-B-']), int(values['-POW-']))
            window['-BIN-'].update(r2)
            save('Binomial expansion', r2)

        if event == 'History':
            window['-DEF-'].update(visible = False)
            window['-COL4-'].update(visible = True)
            window['-MEM-'].update(read())
            curr_layout = 4

        if event == 'Clear':
            clear()
            window['-MEM-'].update(read())

if __name__ == '__main__':
    gui()