import PySimpleGUI as sg 

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

    return result 

def getLabelledInputBox(box_name, tag_name):
    return [sg.Text(f'{box_name}: '), sg.Input(f'-{tag_name}-')]

def gui():
    layout1 = [[sg.Text('Welcome to our maths calculator! What would you like to calculate?')],
               [sg.Button('Combinations')],
               [],
               [sg.Button('Exit')]]

    layout2 = [[sg.Text('Calculating combinations. Your result: '), sg.Text(key = '-COM-')],
               [sg.Text('Total: '), sg.Input(key = '-TOT-')],
               [sg.Text('Choose: '), sg.Input(key = '-CHO-')],
               [sg.Button('Calculate', key = '-C1-')],
               [], [sg.Button('Back')]] 

    layout = [[sg.Column(layout1, key = '-DEF-'), sg.Column(layout2, key = '-COL2-', visible = False)]]

    window = sg.Window('Maths Calculator', layout)

    while True:
        event, values = window.read()
        print(event, values)

        if event in ('Exit', None):
            break 

        if event == 'Combinations':
            window['-DEF-'].update(visible = False)
            window['-COL2-'].update(visible = True)

        if event == '-C1-':
            window['-COM-'].update(combinations(int(values['-TOT-']), int(values['-CHO-'])))
        
        if event == 'Back': 
            window['-COL2-'].update(visible = False)
            window['-DEF-'].update(visible = True)

if __name__ == '__main__':
    gui()