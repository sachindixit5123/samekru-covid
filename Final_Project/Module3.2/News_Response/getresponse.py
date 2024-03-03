import ply.lex as lex
import ply.yacc as yacc
import sys

result_string = ""

# Tokens
tokens = ('OPEN_TABLE', 'CLOSE', 'SECTION_HEADER', 'SUBSECTION_HEADER', 'DATE', 'START', 'START2', 'CONTENT',
          'OPEN_PARAGRAPH', 'CLOSE_PARAGRAPH', 'OPEN_LINK', 'CLOSE_LINK', 'GARBAGE', 'OPEN_LIST', 'CLOSE_LIST')

# Lexical rules
def t_START(t):
    r'<h3[^>]*>'
    return t

def t_OPEN_LIST(t):
    r'<ul[^>]*>'

def t_CLOSE_LIST(t):
    r'</ul>'
    return t

def t_SECTION_HEADER(t):
    r'[0-9][0-9]?.(January|February|March|April|May|June|July|August|September|October|November|December)'
    return t

def t_START2(t):
    r'</h3[^>]*>'
    return t

def t_CLOSE(t):
    r'<h(1|2|3|4|5)[^>]*>'

def t_OPEN_PARAGRAPH(t):
    r'<p[^>]*>'
    return t

def t_OPEN_LINK(t):
    r'<a[^>]*>'

def t_CLOSE_LINK(t):
    r'</a[^>]*>'

def t_CLOSE_PARAGRAPH(t):
    r'</p[^>]*>'
    return t

def t_OPEN_STYLE(t):
    r'<style[^>]*>[^<]*</style>'

def t_CLOSE_STYLE(t):
    r'</style[^>]*>'

def t_WRONG_DATA(t):
    r'&\#91;[0-9a-zA-Z]+&\#93; | &\#160;'

def t_OPEN_ROW(t):
    r'<tr[^>]*>'

def t_CLOSE_ROW(t):
    r'</tr[^>]*>'

def t_CONTENT(t):
    r'[A-Za-z0-9,. ()\'–-]+'
    return t

def t_TITLE(t):
    r'</Title>'
    return t

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)

# Grammar rules
def p_start(p):
    '''start : parse_table'''

def p_parse_table(p):
    '''parse_table : START SECTION_HEADER parse_data START2 parse_data START
                   | START2 parse_data START'''

    global result_string
    
    if len(p) == 7:
        result_string = result_string + '\n' + p[2] + ": " + p[5]
    else:
        result_string = result_string + p[2]

def p_parse_data(p):
    '''parse_data : CONTENT
                  | parse_data CONTENT'''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    global result_string
    
    try:
        result_string = result_string + '\n' + p.value + ": "
    except:
        pass

def main():
    file_obj = open('response.html', 'r', encoding="utf-8")
    data = file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

    filename = sys.argv[1]

    def extract_date(line):
        parts = line.split(' ')
        date = int(parts[0])
        return date

    with open(filename, 'w') as file:
        global result_string
        lines = result_string.strip().split('\n')
        new_line = []

        for line in lines:
            parts = line.split(' ')
            
            try:
                date = int(parts[0])
                new_line.append(line)
            except:
                continue

        sorted_lines = sorted(new_line, key=extract_date)
        sorted_string = '\n'.join(sorted_lines)

        file.write(sorted_string)

if __name__ == '__main__':
    main()
