#!/bin/python
import sys
import tabReader as tr
import pprint

def openTab(file_path):
  with open(file_path,"r") as file:
    tab = file.read() 
  file.close()
  return tab

def main():
  file_path = sys.argv[1]
  tab_text = openTab(file_path)
  tab = tr.Tab(tab_text)
  sections = tab.sections
  section_strings = tr.getSectionAsStrings(sections[0])
  subsections = tr.getSubsections(section_strings)
  notes = tr.getNextNotes(subsections[0])
  summary = tr.summariseNotes(notes)
  pprint.pprint(summary)

main()
