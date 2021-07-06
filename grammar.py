''' 
VACACIONES DE JUNIO 2020
INTERPRETER SAMPLE  
'''
from os import truncate
from Instrucciones.Case import Case
from Instrucciones.MasMenos import MasMenos
from Instrucciones.Default import Default
from Instrucciones.For import For
from Nativas.ToLower import ToLower
from Nativas.ToUpper import ToUpper
from Nativas.Truncate import Truncate
from Nativas.TypeOf import TypeOf
from Nativas.Round import Round
from Nativas.Length import Length
import re
from TS.Excepcion import Excepcion

errores = []
reservadas = {
    'int'       : 'RINT',
    'float'     : 'RFLOAT',
    'char'      : 'RCHAR',
    'string'    : 'RSTRING',
    'boolean'   : 'RBOOLEAN',
    'print'     : 'RPRINT',
    'if'        : 'RIF',
    'for'       : 'RFOR',
    'else'      : 'RELSE',
    'while'     : 'RWHILE',
    'true'      : 'RTRUE',
    'false'     : 'RFALSE',
    'break'     : 'RBREAK',
    'main'      : 'RMAIN',
    'func'      : 'RFUNC',
    'return'    : 'RRETURN',
    'switch'    : 'RSWITCH',
    'continue'  : 'RCONTINUE',
    'case'      : 'RCASE',
    'default'   : 'RDEFAULT',
    'var'       : 'RVar',
    'read'      : 'RREAD',
    'new'       : 'RNEW'
}

tokens  = [
    'PUNTOCOMA',
    'DOSPUNTOS',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'CORA',
    'CORC',
    'COMA',
    'MASPLUS',
    'MENOSPLUS',
    'MAS',
    'MENOS',
    'POR',
    'DIVI',
    'MOD',
    'ELEV',
    'MENORQUE',
    'MAYORQUE',
    'IGUALIGUAL',
    'IGUALDIF',
    'MENORIGUALL',
    'MAYORIGUALL',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CHAR',
    'ID'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA     = r';'
t_DOSPUNTOS     = r':'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'{'
t_LLAVEC        = r'}'
t_CORA          = r'\['
t_CORC          = r'\]'
t_COMA          = r','
t_MASPLUS       = r'\+\+'
t_MENOSPLUS     = r'--'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVI          = r'\/'
t_MOD           = r'%'
t_ELEV          = r'\*\*'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_IGUALIGUAL    = r'=='
t_IGUALDIF      = r'=!'
t_MENORIGUALL   = r'<='
t_MAYORIGUALL   = r'>='
t_IGUAL         = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
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
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] # remuevo las comillas

    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')

    return t

def t_CHAR(t):
    r'\'(\\\'|\\"|\\t|\\n|\\\\|[^\'\\])\''
    t.value = t.value[1:-1] # remuevo las comillas
    #print
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

#Comentario multilinea //...
def t_COMENTARIO_MULTIPLE(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += 1

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

# Asociación de operadores y precedencia
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','MENORQUE','MAYORQUE', 'IGUALIGUAL','IGUALDIF','MENORIGUALL','MAYORIGUALL'),
    ('left','MAS','MENOS'),
    ('left','POR'),
    ('left','DIVI'),
    ('left','MOD'),
    ('left','ELEV'),
    ('right','UMENOS'),
    ('left', 'MASPLUS','MENOSPLUS')
    )

# Definición de la gramática

#Abstract
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.Break import Break
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Instrucciones.Return import Return
from Instrucciones.For import For
from Instrucciones.Switch import Switch
from Expresiones.Read import Read
from Expresiones.Casteo import Casteo
from Instrucciones.DeclaracionArr1 import DeclaracionArr1
from Expresiones.AccesoArreglo import AccesoArreglo
from Instrucciones.ModificarArreglo import ModificarArreglo
from Instrucciones.Continue import Continue

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t) :
    '''instruccion      : imprimir_instr finins
                        | declaracion_instr finins
                        | asignacion_instr finins
                        | if_instr
                        | while_instr
                        | break_instr finins
                        | for_instr
                        | switch_instr
                        | main_instr
                        | funcion_instr
                        | llamada_instr finins
                        | inc_decre_instr finins
                        | return_instr finins
                        | declArr_instr finins
                        | continue_instr finins
                        | modArr_instr finins'''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    | '''
    t[0] = None

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""
#///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t) :
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////DECLARACION//////////////////////////////////////////////////

def p_declaracion(t) :
    'declaracion_instr     : RVar ID IGUAL expresion'                              
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

def p_declaracion2(t) :
    'declaracion_instr     : RVar ID'                              
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]))


#///////////////////////////////////////DECLARACION ARREGLO//////////////////////////////////////////////////

def p_declArr(t) :
    '''declArr_instr     : tipo1'''
    t[0] = t[1]

def p_tipo1(t) :
    '''tipo1     : tipo lista_Dim ID IGUAL RNEW tipo lista_expresiones'''
    t[0] = DeclaracionArr1(t[1], t[2], t[3], t[6], t[7], t.lineno(3), find_column(input, t.slice[3]))

def p_lista_Dim1(t) :
    'lista_Dim     : lista_Dim CORA CORC'
    t[0] = t[1] + 1
    
def p_lista_Dim2(t) :
    'lista_Dim    : CORA CORC'
    t[0] = 1

def p_lista_expresiones_1(t) :
    'lista_expresiones     : lista_expresiones CORA expresion CORC'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_lista_expresiones_2(t) :
    'lista_expresiones    : CORA expresion CORC'
    t[0] = [t[2]]

#///////////////////////////////////////MODIFICACION ARREGLOS//////////////////////////////////////////////////


def p_modArr(t) :
    '''modArr_instr     :  ID lista_expresiones IGUAL expresion'''
    t[0] = ModificarArreglo(t[1], t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////ASIGNACION//////////////////////////////////////////////////

def p_asignacion(t) :
    'asignacion_instr     : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////IF//////////////////////////////////////////////////

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_continue(t) :
    'continue_instr     : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////FOR//////////////////////////////////////////////////

def p_for(t) :          #for (       var i = 0       ;      i<3       ;       i++            )    {       instruccion       }    
    'for_instr       : RFOR PARA inicializacion_inst PUNTOCOMA expresion PUNTOCOMA avance_inst PARC   LLAVEA instrucciones LLAVEC'
    t[0] = For(t[5], t[10], t[7],t[3], t.lineno(1), find_column(input, t.slice[1]))


#/////////////////////////////////////////////////////////INICIALIZACION//////////////////////////
def p_inicializacion(t):
    '''inicializacion_inst    :  declaracion_instr
                              |  asignacion_instr
       '''
    t[0]=t[1]
#//////////////////////////////////////////////////////////////AVANCE////////////////////////////////
def p_avance(t):
    '''avance_inst          :   asignacion_instr
                            |   inc_decre_instr
    '''       
    t[0]=t[1]

#///////////////////////////////////////////////////SWITCH///////////////////////////////////////////////////////////////
def p_switch3(t):
     '''switch_instr    : RSWITCH PARA expresion PARC LLAVEA default_instr LLAVEC
     '''
     t[0]= Switch(t[3],None,t[7],t.lineno(1), find_column(input, t.slice[1]))

def p_switch2(t):
    '''switch_instr    : RSWITCH PARA expresion PARC LLAVEA casos_casos_instr LLAVEC
    '''
    t[0]= Switch(t[3],t[6],None,t.lineno(1), find_column(input, t.slice[1]))

def p_switch(t):
    '''switch_instr    : RSWITCH PARA expresion PARC LLAVEA casos_casos_instr default_instr LLAVEC
     '''
    t[0]= Switch(t[3],t[6],t[7],t.lineno(1), find_column(input, t.slice[1]))


#//////////////////////////////////////////////////////CASE///////////////////////////////////////////////////////////////

def p_casoes_casos_caso(t) :
    'casos_casos_instr    : casos_casos_instr caso_str'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_casos_caso(t) :
    'casos_casos_instr    : caso_str'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

def p_instruccion_caso(t) :
    '''caso_str         : RCASE expresion DOSPUNTOS instrucciones'''
    t[0] = Case(t[2],t[4],t.lineno(1), find_column(input, t.slice[1]))


#/////////////////////////////////////////////////////DEFAULT//////////////////////////////////////////////////////////////
def p_default(t):
    'default_instr   : RDEFAULT DOSPUNTOS instrucciones'
    t[0] = t[3]


#///////////////////////////////////////MAIN//////////////////////////////////////////////////

def p_main(t) :
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FUNCION//////////////////////////////////////////////////

def p_funcion_1(t) :
    'funcion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_2(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS//////////////////////////////////////////////////

def p_parametros_1(t) :
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametros_2(t) :
    'parametros    : parametro'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO//////////////////////////////////////////////////

def p_parametro(t) :
    'parametro     : tipo ID'
    t[0] = {'tipo':t[1],'identificador':t[2]}

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada1(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada2(t) :
    'llamada_instr     : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametrosLL_1(t) :
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametrosLL_2(t) :
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t) :
    'parametro_llamada     : expresion'
    t[0] = t[1]

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_return(t) :
    'return_instr     : RRETURN expresion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RFLOAT
                | RSTRING
                | RCHAR
                | RBOOLEAN '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'float':
        t[0] = TIPO.DECIMAL
    elif t[1].lower() == 'string':
        t[0] = TIPO.CADENA
    elif t[1].lower() == 'boolean':
        t[0] = TIPO.BOOLEANO
    elif t[1].lower() == 'char':
        t[0] = TIPO.CHARACTER


#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIVI expresion
            | expresion MOD expresion
            | expresion ELEV expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion IGUALIGUAL expresion
            | expresion IGUALDIF expresion
            | expresion MENORIGUALL expresion
            | expresion MAYORIGUALL expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS 
            | NOT expresion %prec UNOT 
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_incremento_decre(t):
    '''
    inc_decre_instr  :  ID MASPLUS
                     |  ID MENOSPLUS

    '''
    if t[2] == '++':
        t[0] = MasMenos(OperadorAritmetico.INC,Identificador(t[1],t.lineno(1),find_column(input,t.slice[1])),t.lineno(1),find_column(input,t.slice[1]))
    elif t[2] == '--':
        t[0] = MasMenos(OperadorAritmetico.DEC,Identificador(t[1],t.lineno(1),find_column(input,t.slice[1])),t.lineno(1),find_column(input,t.slice[1]))

def p_expresion_unaria_der(t):
    '''
    expresion : expresion MASPLUS
              | expresion MENOSPLUS
    '''
    if t[2] == '++':
        t[0] = Aritmetica(OperadorAritmetico.INC,t[1],None,t.lineno(2),find_column(input,t.slice[2]))
    elif t[2] == '--':
        t[0] = Aritmetica(OperadorAritmetico.DEC,t[1],None,t.lineno(2),find_column(input,t.slice[2]))


def p_expresion_agrupacion(t):
    '''
    expresion :   PARA expresion PARC 
    '''
    t[0] = t[2]

def p_expresion_llamada(t):
    '''expresion : llamada_instr'''
    t[0] = t[1]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_char(t):
    '''expresion : CHAR'''
    t[0] = Primitivos(TIPO.CHARACTER, str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_read(t):
    '''expresion : RREAD PARA PARC'''
    t[0] = Read(t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cast(t):
    '''expresion : PARA tipo PARC expresion'''
    t[0] = Casteo(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_Arreglo(t):
    '''expresion : ID lista_expresiones'''
    t[0] = AccesoArreglo(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

def crearNativas(ast):          # CREACION Y DECLARACION DE LAS FUNCIONES NATIVAS
    nombre = "toupper"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toUpper##Param1'}]
    instrucciones = []
    toUpper = ToUpper(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toUpper)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    
    nombre = "tolower"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'toLower##Param1'}]
    instrucciones = []
    toLower = ToLower(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(toLower)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "truncate"
    parametros = [{'tipo':TIPO.DECIMAL,'identificador':'truncate##Param1'}]
    instrucciones = []
    truncate = Truncate(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(truncate)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "typeof"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'typeof##Param1'}]
    instrucciones = []
    typeof = TypeOf(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(typeof)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "round"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'round##Param1'}]
    instrucciones = []
    round = Round(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(round)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)

    nombre = "length"
    parametros = [{'tipo':TIPO.CADENA,'identificador':'length##Param1'}]
    instrucciones = []
    length = Length(nombre, parametros, instrucciones, -1, -1)
    ast.addFuncion(length)     # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)