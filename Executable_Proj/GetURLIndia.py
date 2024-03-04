from urllib.request import Request, urlopen
import ply.lex as lex
import ply.yacc as yacc
import re

def downloadwebpage(url):
    req = Request(url,headers ={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mydata = webpage.decode("utf8")
    f=open('webpage.html','w',encoding="utf-8")
    f.write(mydata)
    f.close

url="https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic"
downloadwebpage(url)
env={}

###DEFINING TOKENS###
tokens = ('START', 'END', 'ANCHOR', 'OPENSTYLE', 'CLOSESTYLE', 'HTAG', 'OPENTAG', 'CLOSETAG', 'OPENCLOSETAG', 'BREAK', 'CONTENT')
t_ignore = r' \t\n '

###############Tokenizer Rules################

def t_START(t):
    r'<a.href=\"\/wiki\/Timeline_of_the_COVID\-19_pandemic_in_India\".title=\"Timeline.of.the.COVID\-19.pandemic.in.India\">India<\/a>'
    return t

def t_END(t):
    r'<a.href=\"\/wiki\/Timeline_of_the_COVID\-19_pandemic_in_Kerala\"'
    return t

def t_ANCHOR(t):
    r'<a[^>]*>'
    return t

def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'<\/style[^>]*>'
    return t
  
def t_HTAG(t):
    r'<h[^>]*>'
    return t

def t_CONTENT(t):
    r'[^<>\n\t]+'
    return t

def t_BREAK(t):
    r'<br[^>]*>'
    return t

def t_OPENCLOSETAG(t):
    r'<img[^>]*>'
    return t

def t_OPENTAG(t):
    r'<(?!\/)[A-Za-z]+[^>]*>'
    return t

def t_CLOSETAG(t):
    r'<\/[A-Za-z]+[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)

####################################################################################################################################################################################################
											#GRAMMAR RULES
baseurl ='https://en.wikipedia.org/'
pattern = r'<a\s+(?:[^>]*?\s+)?href=[\"\'](.*?)[\"\']'
def p_start(p):
    '''start : START getanchor'''

def p_getanchor(p):
    '''getanchor : OPENTAG getanchor
                 | CONTENT getanchor
                 | CLOSETAG getanchor
                 | OPENCLOSETAG getanchor
                 | BREAK getanchor
                 | HTAG getanchor
                 | OPENSTYLE getanchor
                 | CLOSESTYLE getanchor
                 | ANCHOR CONTENT getanchor
                 | END'''
    if(len(p)==4):
        href = re.findall(pattern, p[1])[0]
        env[p[2]]=baseurl+href

def p_error(p):
    pass

def getUrlsIndia():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    parser = yacc.yacc()
    parser.parse(data)
    return env