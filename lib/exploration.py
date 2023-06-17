from lib.functions import combinations
from typing import List

class Term:
    def __init__(self, coefficient: int, exponent: int):
        self.coefficient = coefficient
        self.exponent = exponent

    def __str__(self):
        match self.exponent:
            case 0: return f'{print_coefficient(self.coefficient)}'
            case _: return f'{print_coefficient(self.coefficient)}x{print_exponent(self.exponent)}'

def print_coefficient(value: int):
    match value:
        case 1: return ''
        case _: return str(value)

def print_exponent(value: int):
    match value:
        case 1: return ''
        case _: return f'^{str(value)}'


class Polynomial:
    def __init__(self, terms: List[Term]):
        self.terms = terms

    def __str__(self):
        return ' + '.join(map(str, self.terms))


# (ax + b)^n
def binomial_expansion(a: int, b: int, n: int):
    terms = []
    for i in range(n + 1):
        terms.append(Term(coefficient=combinations(n, i)*(a**(n - i))*(b**(i)), exponent=(n - i)))
    print(Polynomial(terms))


