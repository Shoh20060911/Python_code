# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
def newtons_method(x0, S, eplison=0.0001):
    f = lambda x: x**3-S
    f_prime =lambda x: 3 * x**2
    x = x0
    while abs(f(x)) > eplison:
        x = x - f(x) / f_prime(x)
    return x 
S = 30 
initial_guesses = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
for guess in initial_guesses:
    result = newtons_method(guess, S)
    print(f"Initial guess: {guess}, Result: {result}")
    

