import ply.lex as lex
from . import logger

class ConditionLexer(object):
    tokens = (
        'CONDITION', 'NUMBER',
        'LT', 'GT',
        'AND', 'OR',
        'LPAREN', 'RPAREN',
    )

    # Regular expression of tokens
    t_CONDITION = r'[a-zA-z_]+'
    t_LT = r'<'
    t_GT = r'>'
    t_AND = r'and'
    t_OR = r'or'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    
    # Ignored characters
    t_ignore = ' \t'
    
    def t_NUMBER(self, t):
        r'\d+(\.\d+)?'
        try:
            t.value = float(t.value)
        except ValueError:
            self._logger.warning('Cannot convert %s to float number; Set to 0.', t.value)
            t.value = 0
        return t
    
    def t_error(self, t):
        self._logger.warning('Illegal character \'%s\'.', t.value[0])
        t.lexer.skip(1)

    def __init__(self):
        # Build the lexer
        self.lexer = lex.lex(module=self)
        # Set logger
        self._logger = logger.Logger.register(__name__)