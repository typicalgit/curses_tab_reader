#!/usr/bin/env python3

def dict_max_val_len(dicky):
  length = 0
  for key in dicky.keys():
    if len(dicky[key]) > length:
      length = len(dicky[key])
  return length
