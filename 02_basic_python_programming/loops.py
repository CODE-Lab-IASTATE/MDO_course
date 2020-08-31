# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 17:00:17 2020

@author: raulv
"""

# ------ if statement ------ 
# Check x is positive or negative
x = -10
if x < 0:
    x = 0
    print('x is neagative')
elif x == 0:
    print('x = 0')
else:
    print('x is positive')

# ------ for loop ------ 
# print content of list y using for loop
y = [1,5,10,20]  # create list y

for i in y:
    print('i=',i)
    
# ------ while loop ------ 
# count number till 9
count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1









