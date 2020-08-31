# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:44:33 2020

@author: 
"""


def square(n):  #define function
    ans = n**2  # a is local variable
    return ans  # returns an answer to where function is called

# Square of number x
x = 5
x_square = square(x)  # calling function square
print('x_square=', x_square)
