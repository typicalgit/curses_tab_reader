import logging
import pprint
import re

logging.basicConfig(filename='log')

logger = logging.getLogger(__name__)

class Tab():
  def __init__(self,tab_file_name,tab_name=None):
    self.tab_file_name = tab_file_name
    self.tab_name = tab_name
    self.tab_text = open_tab_file(tab_file_name)
    if self.tab_name == None:
       self.tab_name = tab_file_name
    else:
      self.tab_name = tab_name
    self.sections = get_sections(self.tab_text,self.tab_name)


def open_tab_file(file_path):
  with open(file_path,"r") as file:
    tab = file.read()
  file.close()
  return tab

def get_sections(tab,tab_name):
  sections = {}

  # RETURN None if tab not populated
  if tab is None or tab == "":
    return None

  # CHECK headings are in text
  pattern = re.compile(r"\[.+?\]")
  if not re.search(pattern,tab):
    sections[tab_name] = text
    return sections

  # SPLIT text and find headings
  texts = re.split(pattern,tab) 
  # DEL item 0 as comes before 1st heading
  texts = texts[1:]

  headings = re.findall(pattern, tab)

  for heading, text in zip(headings, texts):
    sections[heading] = text
  return sections

def get_section_strings(section):
  out = []
  rgx_str = r"[A-G|a-g]\|\|.+"
  rgx_pat = re.compile(rgx_str)
  matches = rgx_pat.findall(section)
  out = matches.copy()  
#  for match in matches:
#    out.append(str(match).replace("\n",""))

  return out

def adjust_len_strings(line):
  char_cnt = 0
  # GET LONGEST STRING LENGTH
  for string in line:
    if len(string[1]) > char_cnt:
      char_cnt = len(string[1])
  #IF LEN STRING LOWER ADD CHARS
  for i,string in enumerate(line):
    if len(string[1]) < char_cnt:
      chars_to_add = char_cnt - len(string[1])
      # ADD CHARS
      for char in range(chars_to_add):
        string[1] += '-'
  return line

def get_lines(strings):
  lines = []
  line = []
  for i in range( len(strings) ):
    string = strings[i]
    open = string[:3]
    rest = string[3:]
    line.append( [open,rest] )
    if len(line) % 6 == 0:
      line = adjust_len_strings(line)
      lines.append(line)
      line = []
  lines_summary = summarise_lines(lines)
  return lines,lines_summary

def add_ng_to_line(ng,line):
  if line == []:
    line = ng
    return line
  for ndx,note in enumerate(ng):
    line[ndx] = str(line[ndx]) + str(note)
  return line

def summarise_line(line):
  gap_cnt = 0
  ng = []
  found = False
  note_summary = []
  new_line = []
  onotes = []
  string1 = line[0][1]
  char_cnt = len(string1)
  # GET OPEN NOTES
  for string in line:
    onotes.append(string[0])
  onotes.insert(0,'gap')
  #LOOP CHARS IN STRING TO GET
  #NDX FOR EACH CHAR IN STRINGS
  for ndx in range(char_cnt):
    #CHECK IF NOTE ON ANY STRING
    for string in line:
      ng.append(string[1][ndx])
      if string[1][ndx] != '-':
        found = True
    #IF NOTE ON STRING ADD ALL
    #NOTES TO LIST
    if found:
      ng.insert(0,gap_cnt)
      note_summary = add_ng_to_line(ng,note_summary)
      gap_cnt = 0
    else:
      gap_cnt += 1
    # RESET NG AND FOUND FLAG
    ng = []
    found = False
  #ADD ONOTES BACK TO STRINGS
  for i in range(len(onotes)):
    new_line.append([onotes[i],note_summary[i]])
  return new_line

def summarise_lines(lines):
  lines_summary = []
  for line in lines:
    line_summary = summarise_line(line)
    lines_summary.append(line_summary) 
  return lines_summary


