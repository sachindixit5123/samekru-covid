import ply.lex as lex
import ply.yacc as yacc

data_environment = {}

# DEFINING TOKENS
tokens = ('OPENTITLE', 'TITLE', 'XAXIS', 'CATEGORY', 'CLOSETITLE', 'START', 'NAME', 'OPENDATA', 'CLOSEDATA', 'STYLE', 'CONTENT')
t_ignore = r' \t\n '

# Tokenizer Rules

def t_TITLE(t):
    r'(text|ext):.\'Daily.Deaths\''
    return t

def t_CLOSETITLE(t):
    r'},'
    return t
def t_OPENDATA(t):
    r'data:.\['
    return t

def t_CLOSEDATA(t):
    r'\]'
    return t
def t_XAXIS(t):
    r'xAxis:.{'
    return t
def t_OPENTITLE(t):
    r'(title|itle):.{'
    return t

def t_CATEGORY(t):
    r'categories:.\['
    return t

def t_START(t):
    r'series:.\[{'    
    return t

def t_NAME(t):
    r'(name|ame):.\'Daily.Deaths\','
    return t





def t_STYLE(t):
    r'[A-Za-z0-9]+:.[^,]+,'
    return t
def t_CONTENT(t):
    r'[^<>\n\t\[\]]+'
    return t
def t_error(t):
    t.lexer.skip(1)

# Grammar Rules
def p_start(p):
    '''start : OPENTITLE TITLE CLOSETITLE skip_tag'''

def p_skip(p):
    '''skip : STYLE skip
                | CONTENT skip
                | XAXIS CATEGORY get_date'''

def p_date(p):
    '''date : CONTENT CLOSEDATA CLOSETITLE skipper2'''
    data_environment['date'] = p[1]
    
def p_skiper(p):
    '''skiper : STYLE skiper
                | CONTENT skiper
                | XAXIS CATEGORY get_date'''
def p_skipper2(p):
    '''skipper2 : STYLE skipper2
                 | CONTENT skipper2
                 | CLOSEDATA skipper2
                 | start'''

def p_end(p):
    '''end : START NAME get_data'''

def p_data(p):
    '''data : STYLE data
                | OPENDATA content'''

def p_content(p):
    '''content : CONTENT CLOSEDATA'''
    data_environment['data'] = p[1]

def p_error(p):
    pass

def get_daily_deaths():
    file_obj = open('webpage.html', 'r', encoding="utf-8")
    file_data = file_obj.read()
    lexer = lex.lex()
    lexer.input(file_data)
    parser = yacc.yacc()
    try:
        parser.parse(file_data)
        dates = data_environment['date'].split('"')
        dates = [i for i in dates if i != '' and i != ',']
        daily_deaths = data_environment['data'].split(',')
        del data_environment['data']
        del data_environment['date']
    except:
        daily_deaths = 'N/A'
        dates = 'N/A'
    return dates, daily_deaths

# Example usage
# dates, daily_deaths = get_daily_deaths()
# for i in range(0, len(dates)):
#     print(f'{dates[i]}\t{daily_deaths[i]}')
