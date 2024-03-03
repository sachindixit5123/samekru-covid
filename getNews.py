import ply.lex as lex
import ply.yacc as yacc

import sys 


### DEFINING TOKENS###
tokens = ('BEGINTABLE', 'ENDTABLE',
'OPENHEADER', 'CLOSEHEADER','OPENPARA','CLOSEPARA','OPENLIST','CLOSELIST',
'CONTENT',  'OPENSPAN', 'CLOSESPAN','GARBAGE','WRONGDATA','FIGCAPTIONOPEN','FIGCAPTIONCLOSE')

t_ignore = '\t'

str1 = ""


############### Tokenizer Rules################


def t_BEGINTABLE(t):
    r'Pandemic.chronology</span>'
    return t


def t_ENDTABLE(t):
    r'Summary</span>'
    return t

def t_FIGCAPTIONOPEN(t):
    r'<figure[^>]*>'
    return t
def t_FIGCAPTIONCLOSE(t):
     r'</figure[^>]*>'
     return t

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'


def t_OPENHEADER(t):
    r'<h[^>]*>'
    return t 

def t_CLOSEHEADER(t):
    r'</h[^>]*>'
    return t

def t_OPENPARA(t):
    r'<p[^>]*>'
  

def t_CLOSEPARA(t):
    r'</p[^>]*>'
def t_OPENLIST(t):
    r'<li[^>]*>'
    return t
  
def t_CLOSELIST(t):
    r'</li[^>]*>'
    return t


def t_GARBAGE(t):
    r'<[^>]*>'

def t_WRONGDATA(t):
    r'&\#91;[0-9a-zA-Z]+&\#93; | &\#160;'

def t_CONTENT(t):
    r'[A-Za-z0-9,. ()\'–-]+'
    return t


def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
 


def p_start(p):
    '''start : table'''
    p[0] = p[1]


def p_skip(p):
    '''skip : CONTENT skip
               | empty'''


def p_handleheader(p):
    '''handleheader : OPENHEADER content CLOSEHEADER  content handlefig handleheader
                    | OPENHEADER content CLOSEHEADER   handlefig content  handleheader
                    | OPENHEADER content CLOSEHEADER  content handleheader
                    | OPENHEADER 
                    | handlelist handleheader
                  | empty
                  '''
    global str1
    if len(p) == 7:
        p[0] ='\n' + p[2] +': ' + p[6]
        str1 =  p[0] + str1
    if len(p) == 6:
        p[0] ='\n' + p[2] +': ' + p[5]
        
        str1 =  p[0] + str1
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0]=''
    
def p_handlefig(p):
    '''
    handlefig : FIGCAPTIONOPEN skip FIGCAPTIONCLOSE handlefig
            |
    '''


def p_handlelist(p):
    '''
    handlelist : OPENLIST content handlelist CLOSELIST handlelist
            | OPENLIST content CLOSELIST handlelist
            | content handlelist
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
    '''table : BEGINTABLE content CLOSEHEADER handleheader  ENDTABLE
             | BEGINTABLE handleheader  ENDTABLE
    '''
   
def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
   
    pass

######### DRIVER FUNCTION#######


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
