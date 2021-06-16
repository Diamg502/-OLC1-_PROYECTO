#Gramatica PLY prueba
#Vacaciones de Junio 2021
#201700355-DIEGO ALEJANDRO MARTINEZ GARCIA

reservadas = {
    'res_int': "Int",
    'res_double':'Double',
    'res_boolean': 'Boolean',
    'res_char':'Char',
    'res_string': 'String',
    'res_null': 'Null'
    }

tokens = (
    'PTCOMA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID'
)+list(reservadas.values())

#Tokens
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es demasiado grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )


#Definicion de la gramatica

def p_instrucciones_lista(t):
    '''
    instrucciones : instruccion instrucciones
                    | instruccion
    '''

def p_instruccion(t):
    '''
    instruccion : ROPERA CORA expresion CORC PTCOMA
    '''
    print('El resultado es: ' + str(t[3]))

def p_expresion_1(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
    '''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS
    '''
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    '''
    expresion : PARA expresion PARC
    '''
    t[0]=t[2]

def p_expresion_primitivo(t):
    '''
    expresion : ENTERO
            | DECIMAL
    '''
    t[0]=t[1]

def p_error(t):
    print('Error sintactico en %s', t.value)
    #almacenamiento de errores sintacticos

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt","r")
imput = f.read()
print(imput)
parser.parse(imput)
print("Archivo ejecutado correctamente :p")
