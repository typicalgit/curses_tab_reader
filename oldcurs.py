#!/bin/python
import curses
import time
import sys
import tabReader as tr
import proj_utils as putil

mode = 'w' #w=Whole, s=Summary

def key_changes(k):
  if k == ord('w'):
    mode = 'w'
  if k == ord('s'):
    mode = 's'

def check_spacing(win,note_dict):
  nr_notes = len(note_dict)
  height,width = win.getmaxyx()
  # get spacing
  space = (height - 2) / nr_notes
  if space < 1:
    win.addstr(0,0,"NOT ENOUGH INES IN TERM")
    win.refresh()
    time.sleep(5)
    exit()

def draw_onotes(win,note_dict):
  open_notes = note_dict.keys()
  height,width = win.getmaxyx()
  # get spacing
  check_spacing(win,note_dict)
  #DRAW OPEN NOTES
  row = 1
  col = 2
  for onote in open_notes:
    onote = str(onote)
    if onote == 'gap':
      continue
    win.addstr(row,col,onote)
    row += 1
  #END   

def create_pads(win,whole_note_dict,sum_note_dict):
  whole_note_cnt = putil.dict_max_val_len(whole_note_dict)
  sum_note_cnt = putil.dict_max_val_len(sum_note_dict)
  open_notes = whole_note_dict.keys()
  height,width = win.getmaxyx()
#CREATE PADS
#WHOLE IS FULL TAB
#SUM IS PAD WITH GAPS REMOVED
  whole_pad = curses.newpad(height - 2,whole_note_cnt + 2)
  sum_pad = curses.newpad(height - 2,sum_note_cnt * 2 + 2)

  # CHECK SPACE TO DISPLAY NOTES
  check_spacing(win,sum_note_dict)

#DRAW NOTES TO PADS
  #WHOLE PAD
  row = 0
  for note_ndx in range(whole_note_cnt):
    for onote in open_notes:
      if onote == 'gap':
        continue
      note = whole_note_dict[onote][note_ndx]
      note = str(note)
      whole_pad.addstr(row,note_ndx,note)
      row += 1
    row = 0

  #SUMMARY PAD
  #GAP SIZE IS WRITTEN AFTER AND
  #SHOWN BETWEEN NOTES
  row = 0
  col = 1
  for note_ndx in range(sum_note_cnt):
    for onote in open_notes:
      note = sum_note_dict[onote][note_ndx]
      note = str(note)
      if onote == 'gap':
        continue
      sum_pad.addstr(row,col,note)
      row += 1
    col += 2
    row = 0

  win.refresh()
  sum_pad.refresh(0,0,1,6,height,width - 2)

#END   

def main(stdscr):
  file_path = sys.argv[1]
  tab_file = tr.open_tab_file(file_path)
  Tab = tr.Tab(tab_file)
  sections = Tab.sections
  section_strings = tr.get_section_strings(sections[0])
  lines,summary = tr.get_lines(section_strings)
  line_dict = dict(lines[0])
  summary_dict = dict(summary[0])

  draw_onotes(stdscr,summary_dict)
  create_pads(stdscr,line_dict,summary_dict)
  k = 0
  while k != ord('q'):
    k = stdscr.getch()
    key_changes(k)
   # write_notes(stdscr,summary)


curses.wrapper(main)
