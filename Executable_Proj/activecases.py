import ply.lex as lex
import ply.yacc as yacc

env={}
###DEFINING TOKENS###
tokens = ('OPENTITLE','TITLE','XAXIS','CATEGORY','CLOSETITLE','START','NAME','OPENDATA','CLOSEDATA','STYLE','CONTENT')
t_ignore = r' \t\n '

###############Tokenizer Rules################
def t_OPENTITLE(t):
    r'(title|itle):.{'
    return t

def t_TITLE(t):
    r'(text|ext):.\'(null|Active.Cases)\''
    return t

def t_CLOSETITLE(t):
    r'},'
    return t

def t_XAXIS(t):
    r'xAxis:.{'
    return t

def t_CATEGORY(t):
    r'categories:.\['
    return t

def t_START(t):
    r'series:.\[{'    
    return t

def t_NAME(t):
    r'(name|ame):.\'Currently.Infected\','
    return t

def t_OPENDATA(t):
    r'data:.\['
    return t

def t_CLOSEDATA(t):
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

####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start_d(p):
    '''start_d : OPENTITLE TITLE CLOSETITLE skiptag'''

def p_skiptag(p):
    '''skiptag : STYLE skiptag
               | CONTENT skiptag
               | XAXIS CATEGORY getdate'''

def p_getdate(p):
    '''getdate : CONTENT CLOSEDATA CLOSETITLE skiptag1'''
    env['date']=p[1]

def p_skiptag1(p):
    '''skiptag1 : STYLE skiptag1
                | CONTENT skiptag1
                | CLOSEDATA skiptag1
                | start'''

def p_start(p):
    '''start : START NAME getdata'''

def p_getdata(p):
    '''getdata : STYLE getdata
               | OPENDATA getcontent'''
               
def p_getcontent(p):
    '''getcontent : CONTENT CLOSEDATA'''
    env['data']=p[1]

def p_error(p):
    pass

def getCurrentlyInfected():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    # for tok in lexer:
    #     print(tok)
    parser = yacc.yacc()
    try:
        parser.parse(data)
        dates=env['date'].split('"')
        dates=[i for i in dates if i!='' and i!=',']
        currentlyInfected = env['data'].split(',')
        del env['data']
        del env['date']
    except:
        currentlyInfected='N/A'
        dates='N/A'
    return dates,currentlyInfected
# dates,currentlyInfected=getCurrentlyInfected()
# for i in range(0,len(dates)):
#     print(f'{dates[i]}\t{currentlyInfected[i]}')