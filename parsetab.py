
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN CLOSEDATA CLOSEDIV CLOSEHEADER CLOSEHREF CLOSELIST CLOSEROW CLOSESPAN CONTENT DATE GARBAGE OPENDATA OPENDIV OPENHREF OPENLIST OPENSPAN PATTERN YES\n    start : OPENLIST DATE content CLOSELIST\n          | DATE content CLOSELIST\n    \n    content : CONTENT content\n            | DATE content\n            | OPENLIST content CLOSELIST content\n            | \n    \n    skipstart : GARBAGE skipstart\n              |  \n    '
    
_lr_action_items = {'OPENLIST':([0,3,4,5,7,8,15,],[2,8,8,8,8,8,8,]),'DATE':([0,2,3,4,5,7,8,15,],[3,4,5,5,5,5,5,5,]),'$end':([1,11,14,],[0,-2,-1,]),'CONTENT':([3,4,5,7,8,15,],[7,7,7,7,7,7,]),'CLOSELIST':([3,4,5,6,7,8,9,10,12,13,15,16,],[-6,-6,-6,11,-6,-6,14,-4,-3,15,-6,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'content':([3,4,5,7,8,15,],[6,9,10,12,13,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> OPENLIST DATE content CLOSELIST','start',4,'p_start','england.py',66),
  ('start -> DATE content CLOSELIST','start',3,'p_start','england.py',67),
  ('content -> CONTENT content','content',2,'p_content','england.py',93),
  ('content -> DATE content','content',2,'p_content','england.py',94),
  ('content -> OPENLIST content CLOSELIST content','content',4,'p_content','england.py',95),
  ('content -> <empty>','content',0,'p_content','england.py',96),
  ('skipstart -> GARBAGE skipstart','skipstart',2,'p_skipstart','england.py',111),
  ('skipstart -> <empty>','skipstart',0,'p_skipstart','england.py',112),
]
