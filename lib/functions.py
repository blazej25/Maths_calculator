from math import log10, floor

def round_sd(num, sd):
    num = round(num, -int(floor(log10(abs(num)))) + (sd - 1))    

    return num

def separator(inp: str):
    inp = list(map(int, inp.split('/')))

    return inp 

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

def combinations_q(total, choose):
    result = 0 

    numerator = 1
    choose = int(choose)

    if '/' in total:
        total = separator(total)

        if choose == 1:
            numerator = total[0]/total[1]
        else:
            for i in range(choose):
                numerator *= total[0]/total[1] - i
    else:
        total = float(total)

        if choose == 1:
            numerator == total 
        else:
            for i in range(choose):
                numerator *= total - i 

    result = numerator / factorial(choose)    

    ratio = (result).as_integer_ratio()

    if ratio[1] == 1:
        return str(ratio[0])
    else:
        return f'{ratio[0]}/{ratio[1]}'

def bin_expand(a, b, pow):
    result = ''

    for i in range(pow + 1):
        if pow - i == 0:
            result += f'+ {b**pow}'
        elif i == 0:
            result += f'{a**pow}x^{pow} '
        else:
            result += f'+ {(combinations(pow, i) * (b**i) * a**(pow - i))}x^{pow - i} '

    result = result.replace('^1', '')

    if result[0] == '1' and result[1] == 'x':
        result = result.replace('1', '', 1)

    return result