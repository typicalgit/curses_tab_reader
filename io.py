import os
import pickle

def save_dictionary(dictionary, filename):
  directory = "saves"
  
  # Create the "saves" directory if it doesn't exist
  if not os.path.exists(directory):
    os.makedirs(directory)
  
  filepath = os.path.join(directory, filename)
  
  with open(filepath, 'wb') as file:
    pickle.dump(dictionary, file)

def load_dictionary(filename):
  directory = "saves"
  filepath = os.path.join(directory, filename)
  
  with open(filepath, 'rb') as file:
    dictionary = pickle.load(file)
  
  return dictionary

def save_class(obj, filename):
  directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves')
  if not os.path.exists(directory):
    os.makedirs(directory)
  
  filepath = os.path.join(directory, filename)
  with open(filepath, 'wb') as file:
    pickle.dump(obj, file)

def load_class(filename):
  directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saves')
  filepath = os.path.join(directory, filename)
  with open(filepath, 'rb') as file:
    obj = pickle.load(file)
  return obj
