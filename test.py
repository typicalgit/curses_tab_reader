#!/bin/python
listy = ['a','b','c','d','e','f']

listy2 = [ item + '-' if item == 'a' else item for item in listy]

ah = (item + '-' * 4 for item in listy)

print(ah(listy))
