import ply.lex as lex
import ply.yacc as yacc
import os
import sys

# DEFINING TOKENS
tokens = ('OPEN_TABLE', 'CLOSE_TABLE', 'OPEN_HEADER', 'CLOSE_HEADER', 'OPEN_PARA', 'CLOSE_PARA', 'OPEN_LIST', 'CLOSE_LIST',
          'CONTENT', 'OPEN_SPAN', 'CLOSE_SPAN', 'GARBAGE', 'WRONG_DATA', 'FIG_CAPTION_OPEN', 'FIG_CAPTION_CLOSE')

t_ignore = '\t'

str1 = ""

# Tokenizer Rules
def t_OPEN_TABLE(t):
    r'Pandemic.chronology</span>'
    return t


def t_CLOSE_PARA(t):
    r'</p[^>]*>'


def t_FIG_CAPTION_CLOSE(t):
    r'</figure[^>]*>'
    return t

def t_OPEN_SPAN(t):
    r'<span[^>]*>'


def t_CLOSE_SPAN(t):
    r'</span[^>]*>'


def t_OPEN_HEADER(t):
    r'<h[^>]*>'
    return t


def t_CLOSE_HEADER(t):
    r'</h[^>]*>'
    return t


def t_OPEN_PARA(t):
    r'<p[^>]*>'


def t_OPEN_LIST(t):
    r'<li[^>]*>'
    return t




def t_FIG_CAPTION_OPEN(t):
    r'<figure[^>]*>'
    return t

def t_CLOSE_LIST(t):
    r'</li[^>]*>'
    return t




def t_WRONG_DATA(t):
    r'&\#91;[0-9a-zA-Z]+&\#93; | &\#160;'


def t_CONTENT(t):
    r'[A-Za-z0-9,. ()\'–-]+'
    return t


def t_CLOSE_TABLE(t):
    r'Summary</span>'
    return t
def t_GARBAGE(t):
    r'<[^>]*>'
def t_error(t):
    t.lexer.skip(1)

# GRAMMAR RULES

def p_start(p):
    '''start : table'''
    p[0] = p[1]


def p_skip(p):
    '''skip : CONTENT skip
            | empty'''


def p_handle_header(p):
    '''handle_header : OPEN_HEADER content CLOSE_HEADER  content handle_fig handle_header
                     | OPEN_HEADER content CLOSE_HEADER   handle_fig content  handle_header
                     | OPEN_HEADER content CLOSE_HEADER  content handle_header
                     | OPEN_HEADER 
                     | handle_list handle_header
                     | empty
                     '''
    global str1
    if len(p) == 7:
        p[0] = '\n' + p[2] + ': ' + p[6]
        str1 =  p[0] + str1
    if len(p) == 6:
        p[0] = '\n' + p[2] + ': ' + p[5]
        str1 =  p[0] + str1
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ''


def p_handle_fig(p):
    '''
    handle_fig : FIG_CAPTION_OPEN skip FIG_CAPTION_CLOSE handle_fig
                |
    '''


def p_skip(p):
    '''
    skip :  CONTENT skip
          | OPEN_LIST skip
          | CLOSE_LIST skip
          | empty
    '''


def p_handle_list(p):
    '''
    handle_list : OPEN_LIST content handle_list CLOSE_LIST handle_list
                 | OPEN_LIST content CLOSE_LIST handle_list
                 | content handle_list
                 | empty
    '''
    if len(p) == 6:
        p[0] = p[2] + p[3] + p[5]
    if len(p) == 3:
        p[0] = p[1] + p[2]
    if len(p) == 5:
        p[0] = p[2] + p[4]
    else: 
        p[0] = ''


def p_content(p):
    '''content :  CONTENT content
               | empty'''
    if len(p) == 3:
        if p[1] != 'edit':
            p[0] = p[1] + p[2]
        else: 
            p[0] = p[2]
    else:
        p[0] = ''


def p_table(p):
    '''table : OPEN_TABLE content CLOSE_HEADER handle_header  CLOSE_TABLE
             | OPEN_TABLE handle_header  CLOSE_TABLE
    '''


def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    pass

# DRIVER FUNCTION
def main():
    file_obj = open('news.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()
    filename = sys.argv[1]
    with open(filename, 'w') as file:
        global str1
        file.write(str1)

if __name__ == '__main__':
    main()
