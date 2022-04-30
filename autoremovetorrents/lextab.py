# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AND', 'EQ', 'GT', 'LPAREN', 'LT', 'NUMBER', 'OR', 'RPAREN', 'STRING'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NUMBER>\\d+(\\.\\d+)?)|(?P<t_STRING>[a-zA-Z][a-zA-Z0-9_\\-]*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_EQ>=)|(?P<t_GT>>)|(?P<t_LT><)', [None, ('t_NUMBER', 'NUMBER'), None, ('t_STRING', 'STRING'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'EQ'), (None, 'GT'), (None, 'LT')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
