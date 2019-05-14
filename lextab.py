# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('CHAR', 'COMMA', 'DOT', 'EQUALS', 'FUN_NO_PARAM', 'FUN_SINGLE_PARAM', 'FUN_WITHOUT_OPERATION', 'ID', 'INT', 'LKEY', 'LP', 'RKEY', 'RP', 'SEMICOLON', 'STRING'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_FUN_NO_PARAM>evaluate|BufferOverFlow|open|show)|(?P<t_FUN_SINGLE_PARAM>open)|(?P<t_FUN_WITHOUT_OPERATION>process)|(?P<t_INT>-?\\d+)|(?P<t_STRING>\\"(.+?)\\")|(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_newline>\\n+)|(?P<t_COMMENT>\\#.*)|(?P<t_EQUALS>\\=)|(?P<t_DOT>\\.)|(?P<t_COMMA>\\,)|(?P<t_SEMICOLON>\\;)|(?P<t_LP>\\()|(?P<t_RP>\\))', [None, ('t_FUN_NO_PARAM', 'FUN_NO_PARAM'), ('t_FUN_SINGLE_PARAM', 'FUN_SINGLE_PARAM'), ('t_FUN_WITHOUT_OPERATION', 'FUN_WITHOUT_OPERATION'), ('t_INT', 'INT'), ('t_STRING', 'STRING'), None, ('t_ID', 'ID'), ('t_newline', 'newline'), ('t_COMMENT', 'COMMENT'), (None, 'EQUALS'), (None, 'DOT'), (None, 'COMMA'), (None, 'SEMICOLON'), (None, 'LP'), (None, 'RP')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
