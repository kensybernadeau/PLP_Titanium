
import ply.lex as lex
from ply.lex import TOKEN
import re


# reserved Words
reserved = {
    'FUN_NO_PARAM': ['evaluate','evaluateOverflow','open','show', 'eAll', 'sAll'],
    'FUN_WITHOUT_OPERATION': ['process'],
    'FUN_SINGLE_PARAM': ['open'],
}

# All lexers must provide a list tokens that defines all of the possible token names
# that can be produced by the lexer. This list is always required and is used to
# perform a variety of validation checks. The tokens list is also used by the yacc.py module to identify terminals.
# When building the master regular expression, rules are added in the following order:
# 1. All tokens defined by functions are added in the same order as they appear in the lexer file.
# 2. Tokens defined by strings are added next by sorting them in order of decreasing regular expression
# length (longer expressions are added first).
# For example, if you wanted to have separate tokens for "=" and "==", you need to make sure that "==" is checked first.
# tokens
tokens = [
    'INT',
    'EQUALS', 'ID', 'DOT',
    'COMMA', 'LP', 'RP', 'STRING','CHAR',
    'LKEY','RKEY','SEMICOLON',
             # 'XG'
] + list(reserved)


# Each token is specified by writing a regular expression rule compatible with Python's re module.
#  Each of these rules are defined by making declarations with a special prefix t_ to indicate that it defines a token.
# Declaration of Basic Regular Expressions
t_EQUALS = r'\='
t_DOT = r'\.'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LP = r'\('
t_RP = r'\)'
# t_XG = r'/'

# Regex Patterns
reg_fun_no_param = re.compile('|'.join(reserved['FUN_NO_PARAM']))
reg_fun_single_param = re.compile('|'.join(reserved['FUN_SINGLE_PARAM']))
reg_fun_without_operation = re.compile(reserved.get('FUN_WITHOUT_OPERATION')[0])

#Regex
@TOKEN(reg_fun_no_param .pattern)
def t_FUN_NO_PARAM(t):
    return t


@TOKEN(reg_fun_single_param .pattern)
def t_FUN_SINGLE_PARAM(t):
    return t


@TOKEN(reg_fun_without_operation .pattern)
def t_FUN_WITHOUT_OPERATION(t):
    return t


# Generic Regex

def t_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'

    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Using this, it is usually possible to compute column information as a separate step.
# For instance, just count backwards until you reach a newline.
# Compute column.
# input is the input text string
#  token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# The t_eof() function is used to handle an end-of-file (EOF) condition in the input.
# As input, it receives a token type 'eof' with the lineno and lexposattributes set appropriately.
# The main use of this function is provide more input to the lexer so that it can continue to parse.
# I leave it for possible new functionality
 # EOF handling rule
# def t_eof(t):
#     # Get more input (Example)
#     more = raw_input('... ')
#     if more:
#         self.lexer.input(more)
#         return self.lexer.token()
#     return None


# Lexer
# For improved performance, it may be desirable to use Python's optimized mode
lexer1 = lex.lex(optimize=1)
# For the purpose of debugging, we can use this method
# I leave this method method commented for possible new functionality.
# lexer = lex.lex(debug=1)


lexer = lex.lex(reflags=re.UNICODE)

