import ply.lex as lex
from . import logger
from .exception.illegalcharacter import IllegalCharacter

class ConditionLexer(object):
    reserved = {
        'and': 'AND',
        'or': 'OR'
    }
    tokens = [
        'CONDITION', 'NUMBER',
        'LT', 'GT',
        'LPAREN', 'RPAREN',
    ] + list(reserved.values())

    # Regular expression of tokens
    t_LT = r'<'
    t_GT = r'>'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    
    # Ignored characters
    t_ignore = ' \t'
    
    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        t.value = float(t.value)
        return t

    def t_CONDITION(self, t):
        r'[a-zA-Z_]+'
        t.value = t.value.lower()
        t.type = self.reserved.get(t.value, 'CONDITION')
        return t
    
    def t_error(self, t):
        raise IllegalCharacter('Illegal character \'%s\'.' % t.value[0])

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self)
        # Set logger
        self._logger = logger.Logger.register(__name__)