import PySimpleGUI as sg 
sg.theme('DarkAmber')

def getLabelledInputBox(box_name, tag_name):
    return [sg.Text(f'{box_name}: ', size = (15, 1)), sg.Input(key = f'-{tag_name}-')]

def factorial(n):
    match n:
        case 0: return 1
        case 1: return 1
        case other: return n * factorial(n-1)

def combinations(total, choose):
    if total == choose:
        return 1     

    diff = total - choose

    f_total = factorial(total)
    f_choose = factorial(choose)
    f_diff = factorial(diff)

    result = f_total / (f_choose * f_diff)

    return int(result)

def bin_expand(a, b, pow):
    result = ''

    for i in range(pow + 1):
        if pow - i == 0:
            result += f'+ {b**pow}'
        elif i == 0:
            result += f'{a**pow}x^{pow} '
        else:
            result += f'+ {(combinations(pow, i) * (b**i) * a**(pow - i))}x^{pow - i} '

    return result
    
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
            if int(values['-CHO-']) > int(values['-TOT-']):
                sg.popup('Total has to be greater than choose!!!')
            else:
                window['-COM-'].update(combinations(int(values['-TOT-']), int(values['-CHO-'])))
        
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