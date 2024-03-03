import ply.lex as lex
import ply.yacc as yacc

env = {}

# DEFINING TOKENS
tokens = ('OPEN_TITLE', 'TITLE', 'X_AXIS', 'CATEGORY', 'CLOSE_TITLE', 'START', 'NAME', 'OPEN_DATA', 'CLOSE_DATA', 'STYLE', 'CONTENT')
t_ignore = r' \t\n '

# Tokenizer Rules
def t_OPEN_TITLE(t):
    r'(title|itle):.{'
    return t

def t_TITLE(t):
    r'(text|ext):.\'Daily.Deaths\''
    return t

def t_CLOSE_TITLE(t):
    r'},'
    return t

def t_X_AXIS(t):
    r'xAxis:.{'
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

def t_OPEN_DATA(t):
    r'data:.\['
    return t

def t_CLOSE_DATA(t):
    r'\]'
    return t

def t_STYLE(t):
    r'[A-Za-z0-9]+:.[^,]+,'
    return t

def t_CONTENT(t):
    r'[^<>\n\t\[\]]+'
    return t

def t_error(t):
    t.lexer.skip(1)

# GRAMMAR RULES

def p_start_d(p):
    '''start_d : OPEN_TITLE TITLE CLOSE_TITLE skip_tag'''

def p_skip_tag(p):
    '''skip_tag : STYLE skip_tag
                | CONTENT skip_tag
                | X_AXIS CATEGORY get_date'''

def p_get_date(p):
    '''get_date : CONTENT CLOSE_DATA CLOSE_TITLE skip_tag1'''
    env['date'] = p[1]

def p_skip_tag1(p):
    '''skip_tag1 : STYLE skip_tag1
                 | CONTENT skip_tag1
                 | CLOSE_DATA skip_tag1
                 | start'''

def p_start(p):
    '''start : START NAME get_data'''

def p_get_data(p):
    '''get_data : STYLE get_data
                | OPEN_DATA get_content'''

def p_get_content(p):
    '''get_content : CONTENT CLOSE_DATA'''
    env['data'] = p[1]

def p_error(p):
    pass

def get_daily_deaths():
    file_obj = open('webpage.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()
    try:
        parser.parse(data)
        dates = env['date'].split('"')
        dates = [i for i in dates if i != '' and i != ',']
        daily_deaths = env['data'].split(',')
        del env['data']
        del env['date']
    except:
        daily_deaths = 'N/A'
        dates = 'N/A'
    return dates, daily_deaths

# Example Usage:
# dates, daily_deaths = get_daily_deaths()
# for i in range(0, len(dates)):
#     print(f'{dates[i]}\t{daily_deaths[i]}')
