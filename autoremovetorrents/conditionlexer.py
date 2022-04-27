import ply.lex as lex
from . import logger
from .exception.illegalcharacter import IllegalCharacter

class ConditionLexer(object):
    reserved = {
        'and': 'AND',
        'or': 'OR',
    }
    tokens = [
        'STRING', 'NUMBER',
        'LT', 'GT', 'EQ',
        'LPAREN', 'RPAREN',
    ] + list(reserved.values())

    # Regular expression of tokens
    t_EQ = r'='
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

    def t_STRING(self, t):
        r'[a-zA-Z][a-zA-Z0-9_\-]*'
        t.value = t.value.lower()
        t.type = self.reserved.get(t.value, 'STRING')
        return t
    
    def t_error(self, t):
        raise IllegalCharacter('Illegal character \'%s\'.' % t.value[0])

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self, optimize=1)
        # Set logger
        self._logger = logger.Logger.register(__name__)