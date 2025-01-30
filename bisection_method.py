# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:50:57 2024

@author: user
"""

def bisection_cubic_root(S):
    eplison = 0.0001
    numGuesses = 0
    low = 0.0
    high = max(1.0, S)
    ans = (high + low) / 2.0
    
    while abs(ans**3 -S)>= eplison:
        print(f'low = {low}, high = {high}, abs = {ans}')
        numGuesses += 1
        if ans**3 <S:
            low = ans
        else:
            high = ans
        ans = (high + low )/2.0
        
    print(f'numGuesses = {numGuesses}')
    print(f'{ans} is close to the cubic root of {S}')
    return ans, numGuesses
 