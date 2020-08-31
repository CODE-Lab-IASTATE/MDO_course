# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:15:42 2020

@author:
"""
#
## ------------ Running your first python program --------
print('Hello World')

#
## ------------ Using Python as a Calculator --------
# type below directly in output window (IPython console)
2 + 2

50 - 5*6

(50 - 5*6) / 4

8 / 5  # division always returns a floating point number
#
#
## ------------ Use of variables ------------
# Area of rectangle
width = 20
height = 5 * 9
Area = width * height
print('Area of rectangle=',Area)

# use of string as variable
char = 'Area of rectangle is:'
print(char,Area)


# ------------ Lists ------------
squares = [1, 4, 9, 16, 25]
print(squares)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)

# List indexing 
squares_index_0 = squares[0]
squares_index_1 = squares[1]
print(squares_index_0)  # indexing returns the item
print(squares_index_1)  # indexing returns the item

#List slice
squares_1_to_3 = squares[1:3]
print(squares_1_to_3)





