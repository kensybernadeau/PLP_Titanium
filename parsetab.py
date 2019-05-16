
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAR COMMA DOT EQUALS FUN_NO_PARAM FUN_SINGLE_PARAM FUN_WITHOUT_OPERATION ID INT LKEY LP RKEY RP SEMICOLON STRINGstatement : IDstatement : fun\n                    | assignment\n                    | empty\n                   assignment : file_assignment\n                  | fun_assignment\n                    fun : fun_no_param\n                | fun_single_param\n                | fun_without_operationfun_without_operation : FUN_WITHOUT_OPERATION LP STRING RP fun_no_param : ID DOT FUN_NO_PARAM LP RP fun_single_param : ID DOT FUN_SINGLE_PARAM LP STRING RPfile_assignment : ID EQUALS IDfun_assignment : ID EQUALS fun_without_operationempty :  '
    
_lr_action_items = {'ID':([0,13,],[2,17,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,17,18,22,23,25,],[-15,0,-1,-2,-3,-4,-7,-8,-9,-5,-6,-13,-14,-10,-11,-12,]),'FUN_WITHOUT_OPERATION':([0,13,],[11,11,]),'DOT':([2,],[12,]),'EQUALS':([2,],[13,]),'LP':([11,15,16,],[14,20,21,]),'FUN_NO_PARAM':([12,],[15,]),'FUN_SINGLE_PARAM':([12,],[16,]),'STRING':([14,21,],[19,24,]),'RP':([19,20,24,],[22,23,25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'fun':([0,],[3,]),'assignment':([0,],[4,]),'empty':([0,],[5,]),'fun_no_param':([0,],[6,]),'fun_single_param':([0,],[7,]),'fun_without_operation':([0,13,],[8,18,]),'file_assignment':([0,],[9,]),'fun_assignment':([0,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID','statement',1,'p_help','titanium_parser.py',22),
  ('statement -> fun','statement',1,'p_statement','titanium_parser.py',39),
  ('statement -> assignment','statement',1,'p_statement','titanium_parser.py',40),
  ('statement -> empty','statement',1,'p_statement','titanium_parser.py',41),
  ('assignment -> file_assignment','assignment',1,'p_assignment','titanium_parser.py',48),
  ('assignment -> fun_assignment','assignment',1,'p_assignment','titanium_parser.py',49),
  ('fun -> fun_no_param','fun',1,'p_fun','titanium_parser.py',55),
  ('fun -> fun_single_param','fun',1,'p_fun','titanium_parser.py',56),
  ('fun -> fun_without_operation','fun',1,'p_fun','titanium_parser.py',57),
  ('fun_without_operation -> FUN_WITHOUT_OPERATION LP STRING RP','fun_without_operation',4,'p_fun_without_operation','titanium_parser.py',63),
  ('fun_no_param -> ID DOT FUN_NO_PARAM LP RP','fun_no_param',5,'p_fun_no_param','titanium_parser.py',73),
  ('fun_single_param -> ID DOT FUN_SINGLE_PARAM LP STRING RP','fun_single_param',6,'p_fun_single_param','titanium_parser.py',100),
  ('file_assignment -> ID EQUALS ID','file_assignment',3,'p_file_assignment','titanium_parser.py',125),
  ('fun_assignment -> ID EQUALS fun_without_operation','fun_assignment',3,'p_fun_assignment','titanium_parser.py',139),
  ('empty -> <empty>','empty',0,'p_empty','titanium_parser.py',207),
]
