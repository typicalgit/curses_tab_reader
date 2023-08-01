#!/bin/python

def is_empty(list_in):
  isEmpty = False
  if type(lisg_in) != list:
    isEmpty = True
  if len(list_in) < 1:
    isEmpty = True
  return isEmpty

def remove_blanks(list_in):
  list_out = []
  for i in list_in:
    if len(i) > 0:
      list_out.append(i)
  return list_out

def to_str(list_in):
  list_out = []
  for i in range(len(inArr)):
    str_val = str(list_in[i])
    list_out.append(str_val)
  return list_out

def contains_str(list_in, str_in)
  found = False
  if type(str_in) != string:
    exit
  if len(str_in) < 1:
    exit
  for item in list_in:
    if str(item) == str_in:
      found = True
  return found

def contains_substr(list_in, str_in)
  found = False
  if type(str_in) != string:
    exit
  if len(str_in) < 1:
    exit
  for item in list_in:
    if str_in in str(item):
      found = True
  return found
