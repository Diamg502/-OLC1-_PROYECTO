
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftMENORQUEMAYORQUEIGUALIGUALIGUALDIFMENORIGUALLMAYORIGUALLleftMASMENOSleftPORleftDIVIleftELEVrightUMENOSleftMASPLUSMENOSPLUSAND CADENA CHAR COMA DECIMAL DIVI DOSPUNTOS ELEV ENTERO ID IGUAL IGUALDIF IGUALIGUAL LLAVEA LLAVEC MAS MASPLUS MAYORIGUALL MAYORQUE MENORIGUALL MENORQUE MENOS MENOSPLUS NOT OR PARA PARC POR PUNTOCOMA RBOOLEAN RBREAK RCASE RDEFAULT RELSE RFALSE RFLOAT RFOR RFUNC RIF RINT RMAIN RPRINT RRETURN RSTRING RSWITCH RTRUE RVar RWHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr finins\n                        | declaracion_instr finins\n                        | asignacion_instr finins\n                        | if_instr\n                        | while_instr\n                        | break_instr finins\n                        | for_instr\n                        | switch_instr\n                        | main_instr\n                        | funcion_instr\n                        | llamada_instr finins\n                        | inc_decre_instr finins\n                        | return_instr fininsfinins       : PUNTOCOMA\n                    | instruccion        : error PUNTOCOMAimprimir_instr     : RPRINT PARA expresion PARCdeclaracion_instr     : RVar ID IGUAL expresiondeclaracion_instr     : RVar IDasignacion_instr     : ID IGUAL expresionif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instrwhile_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVECbreak_instr     : RBREAKfor_instr       : RFOR PARA inicializacion_inst PUNTOCOMA expresion PUNTOCOMA avance_inst PARC   LLAVEA instrucciones LLAVECinicializacion_inst    :  declaracion_instr\n                              |  asignacion_instr\n       avance_inst          :   asignacion_instr\n                            |   inc_decre_instr\n    switch_instr    : RSWITCH PARA expresion PARC LLAVEA default_instr LLAVEC\n     switch_instr    : RSWITCH PARA expresion PARC LLAVEA casos_casos_instr LLAVEC\n    switch_instr    : RSWITCH PARA expresion PARC LLAVEA casos_casos_instr default_instr LLAVEC\n     casos_casos_instr    : casos_casos_instr caso_strcasos_casos_instr    : caso_strcaso_str         : RCASE expresion DOSPUNTOS instruccionesdefault_instr   : RDEFAULT DOSPUNTOS instruccionesmain_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVECparametros     : parametros COMA parametroparametros    : parametroparametro     : tipo IDllamada_instr     : ID PARA PARCllamada_instr     : ID PARA parametros_llamada PARCparametros_llamada     : parametros_llamada COMA parametro_llamadaparametros_llamada    : parametro_llamadaparametro_llamada     : expresionreturn_instr     : RRETURN expresiontipo     : RINT\n                | RFLOAT\n                | RSTRING\n                | RBOOLEAN \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIVI expresion\n            | expresion ELEV expresion\n            | expresion MENORQUE expresion\n            | expresion MAYORQUE expresion\n            | expresion IGUALIGUAL expresion\n            | expresion IGUALDIF expresion\n            | expresion MENORIGUALL expresion\n            | expresion MAYORIGUALL expresion\n            | expresion AND expresion\n            | expresion OR expresion\n    \n    expresion : MENOS expresion %prec UMENOS \n            | NOT expresion %prec UNOT \n    \n    inc_decre_instr  :  ID MASPLUS\n                     |  ID MENOSPLUS\n\n    \n    expresion : expresion MASPLUS\n              | expresion MENOSPLUS\n    \n    expresion :   PARA expresion PARC \n    expresion : llamada_instrexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CHARexpresion : CADENAexpresion : RTRUEexpresion : RFALSE'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[17,17,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,17,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,17,17,17,17,17,17,-41,17,17,-24,-27,-34,-35,17,17,-43,-36,17,17,-42,17,-26,17,17,17,17,-25,-29,]),'RPRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[18,18,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,18,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,18,18,18,18,18,18,-41,18,18,-24,-27,-34,-35,18,18,-43,-36,18,18,-42,18,-26,18,18,18,18,-25,-29,]),'RVar':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,47,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[19,19,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,19,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,19,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,19,19,19,19,19,19,-41,19,19,-24,-27,-34,-35,19,19,-43,-36,19,19,-42,19,-26,19,19,19,19,-25,-29,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,103,105,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,140,145,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[20,20,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,40,-28,50,56,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,56,-22,56,56,-72,-73,56,56,75,56,-52,56,56,56,-77,-78,-79,-80,-81,-82,-83,-84,56,-23,-47,56,56,56,56,56,56,56,56,56,56,56,56,56,-74,-75,-70,-71,-20,-21,-48,56,56,20,137,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,20,20,20,20,20,20,155,56,-41,20,20,-24,-27,-34,-35,20,20,-43,-36,20,20,-42,20,-26,20,20,20,20,-25,-29,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,164,166,167,168,169,170,171,172,173,174,175,176,177,],[21,21,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,21,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,21,21,21,21,21,21,-41,21,21,-24,-27,-34,-35,21,21,-43,21,-36,21,21,-42,21,-26,21,21,21,21,-25,-29,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[22,22,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,22,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,22,22,22,22,22,22,-41,22,22,-24,-27,-34,-35,22,22,-43,-36,22,22,-42,22,-26,22,22,22,22,-25,-29,]),'RBREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[23,23,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,23,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,23,23,23,23,23,23,-41,23,23,-24,-27,-34,-35,23,23,-43,-36,23,23,-42,23,-26,23,23,23,23,-25,-29,]),'RFOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[24,24,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,24,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,24,24,24,24,24,24,-41,24,24,-24,-27,-34,-35,24,24,-43,-36,24,24,-42,24,-26,24,24,24,24,-25,-29,]),'RSWITCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[25,25,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,25,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,25,25,25,25,25,25,-41,25,25,-24,-27,-34,-35,25,25,-43,-36,25,25,-42,25,-26,25,25,25,25,-25,-29,]),'RMAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[26,26,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,26,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,26,26,26,26,26,26,-41,26,26,-24,-27,-34,-35,26,26,-43,-36,26,26,-42,26,-26,26,26,26,26,-25,-29,]),'RFUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[27,27,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,27,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,27,27,27,27,27,27,-41,27,27,-24,-27,-34,-35,27,27,-43,-36,27,27,-42,27,-26,27,27,27,27,-25,-29,]),'RRETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,105,114,115,116,117,118,119,120,121,122,123,124,125,126,127,129,130,133,136,138,139,146,147,149,150,151,156,157,160,162,163,166,167,168,169,170,171,172,173,174,175,176,177,],[28,28,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,28,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,28,28,28,28,28,28,-41,28,28,-24,-27,-34,-35,28,28,-43,-36,28,28,-42,28,-26,28,28,28,28,-25,-29,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,146,150,151,156,157,163,166,169,171,176,177,],[0,-1,-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,-41,-24,-27,-34,-35,-43,-36,-42,-26,-25,-29,]),'LLAVEC':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,133,138,139,141,142,144,146,149,150,151,156,157,158,159,162,163,166,167,169,171,173,174,175,176,177,],[-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,146,150,151,156,157,-38,-41,163,-24,-27,-34,-35,166,-37,169,-43,-36,-40,-42,-26,-39,176,177,-25,-29,]),'RDEFAULT':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,142,144,146,150,151,156,157,159,163,166,169,171,173,176,177,],[-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,143,143,-38,-41,-24,-27,-34,-35,-37,-43,-36,-42,-26,-39,-25,-29,]),'RCASE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,23,29,30,31,32,33,34,35,36,37,38,40,43,44,51,55,56,57,58,59,60,61,62,65,66,92,93,94,95,97,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,142,144,146,150,151,156,157,159,163,166,169,171,173,176,177,],[-3,-18,-18,-18,-7,-8,-18,-10,-11,-12,-13,-18,-18,-18,-28,-2,-4,-17,-5,-6,-9,-14,-15,-16,-19,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,-74,-75,-70,-71,-20,-21,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,145,145,-38,-41,-24,-27,-34,-35,-37,-43,-36,-42,-26,-39,-25,-29,]),'PUNTOCOMA':([4,5,6,9,14,15,16,17,23,40,43,44,51,55,56,57,58,59,60,61,62,65,66,72,73,74,92,93,94,95,97,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,],[31,31,31,31,31,31,31,38,-28,-22,-72,-73,-52,-77,-78,-79,-80,-81,-82,-83,-84,-23,-47,103,-30,-31,-74,-75,-70,-71,-20,-21,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,140,]),'PARA':([18,20,21,22,24,25,26,28,39,41,42,45,46,48,50,52,53,54,56,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[39,42,45,46,47,48,49,54,54,54,54,54,54,54,78,54,54,54,42,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'IGUAL':([20,40,75,155,],[41,64,41,41,]),'MASPLUS':([20,51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,155,161,],[43,92,-77,-78,-79,-80,-81,-82,-83,-84,92,92,-47,92,92,92,92,-74,-75,92,92,92,92,-48,92,92,92,92,92,92,92,92,92,92,92,92,92,-76,92,43,92,]),'MENOSPLUS':([20,51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,155,161,],[44,93,-77,-78,-79,-80,-81,-82,-83,-84,93,93,-47,93,93,93,93,-74,-75,93,93,93,93,-48,93,93,93,93,93,93,93,93,93,93,93,93,93,-76,93,44,93,]),'MENOS':([28,39,41,42,45,46,48,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,71,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,103,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,145,161,],[52,52,52,52,52,52,52,80,52,52,52,-77,-78,-79,-80,-81,-82,-83,-84,80,52,80,-47,80,80,80,80,52,52,52,52,52,52,52,52,52,52,52,52,52,-74,-75,-70,80,80,80,-48,52,52,-57,-58,-59,-60,-61,80,80,80,80,80,80,80,80,-76,80,52,80,]),'NOT':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'ENTERO':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'DECIMAL':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'CHAR':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'CADENA':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'RTRUE':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'RFALSE':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'PARC':([42,43,44,49,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,76,78,92,93,94,95,96,99,106,108,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,137,148,152,153,154,],[66,-72,-73,77,-77,-78,-79,-80,-81,-82,-83,-84,97,-23,-47,99,-50,-51,101,102,104,107,-74,-75,-70,-71,127,-48,134,-45,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,-49,-46,-44,165,-32,-33,]),'MAS':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[79,-77,-78,-79,-80,-81,-82,-83,-84,79,79,-47,79,79,79,79,-74,-75,-70,79,79,79,-48,-57,-58,-59,-60,-61,79,79,79,79,79,79,79,79,-76,79,79,]),'POR':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[81,-77,-78,-79,-80,-81,-82,-83,-84,81,81,-47,81,81,81,81,-74,-75,-70,81,81,81,-48,81,81,-59,-60,-61,81,81,81,81,81,81,81,81,-76,81,81,]),'DIVI':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[82,-77,-78,-79,-80,-81,-82,-83,-84,82,82,-47,82,82,82,82,-74,-75,-70,82,82,82,-48,82,82,82,-60,-61,82,82,82,82,82,82,82,82,-76,82,82,]),'ELEV':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[83,-77,-78,-79,-80,-81,-82,-83,-84,83,83,-47,83,83,83,83,-74,-75,-70,83,83,83,-48,83,83,83,83,-61,83,83,83,83,83,83,83,83,-76,83,83,]),'MENORQUE':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[84,-77,-78,-79,-80,-81,-82,-83,-84,84,84,-47,84,84,84,84,-74,-75,-70,84,84,84,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,84,84,-76,84,84,]),'MAYORQUE':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[85,-77,-78,-79,-80,-81,-82,-83,-84,85,85,-47,85,85,85,85,-74,-75,-70,85,85,85,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,85,85,-76,85,85,]),'IGUALIGUAL':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[86,-77,-78,-79,-80,-81,-82,-83,-84,86,86,-47,86,86,86,86,-74,-75,-70,86,86,86,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,86,86,-76,86,86,]),'IGUALDIF':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[87,-77,-78,-79,-80,-81,-82,-83,-84,87,87,-47,87,87,87,87,-74,-75,-70,87,87,87,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,87,87,-76,87,87,]),'MENORIGUALL':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[88,-77,-78,-79,-80,-81,-82,-83,-84,88,88,-47,88,88,88,88,-74,-75,-70,88,88,88,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,88,88,-76,88,88,]),'MAYORIGUALL':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[89,-77,-78,-79,-80,-81,-82,-83,-84,89,89,-47,89,89,89,89,-74,-75,-70,89,89,89,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,89,89,-76,89,89,]),'AND':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[90,-77,-78,-79,-80,-81,-82,-83,-84,90,90,-47,90,90,90,90,-74,-75,-70,-71,90,90,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,90,-76,90,90,]),'OR':([51,55,56,57,58,59,60,61,62,63,65,66,69,70,71,76,92,93,94,95,96,98,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,131,161,],[91,-77,-78,-79,-80,-81,-82,-83,-84,91,91,-47,91,91,91,91,-74,-75,-70,-71,91,91,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,91,91,]),'COMA':([55,56,57,58,59,60,61,62,66,67,68,69,92,93,94,95,99,106,108,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,137,148,],[-77,-78,-79,-80,-81,-82,-83,-84,-47,100,-50,-51,-74,-75,-70,-71,-48,135,-45,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,-49,-46,-44,]),'DOSPUNTOS':([55,56,57,58,59,60,61,62,66,92,93,94,95,99,114,115,116,117,118,119,120,121,122,123,124,125,126,127,143,161,],[-77,-78,-79,-80,-81,-82,-83,-84,-47,-74,-75,-70,-71,-48,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-76,160,168,]),'LLAVEA':([77,101,102,104,107,134,164,165,],[105,129,130,132,136,147,170,172,]),'RINT':([78,135,],[110,110,]),'RFLOAT':([78,135,],[111,111,]),'RSTRING':([78,135,],[112,112,]),'RBOOLEAN':([78,135,],[113,113,]),'RELSE':([150,],[164,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,105,129,130,136,147,160,168,170,172,],[2,133,138,139,149,162,167,173,174,175,]),'instruccion':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[3,29,3,3,3,29,3,29,29,3,29,3,29,29,3,3,3,29,29,29,]),'imprimir_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,47,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[5,5,73,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,47,105,129,130,133,136,138,139,140,147,149,160,162,167,168,170,172,173,174,175,],[6,6,74,6,6,6,6,6,6,6,153,6,6,6,6,6,6,6,6,6,6,6,]),'if_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,164,167,168,170,172,173,174,175,],[7,7,7,7,7,7,7,7,7,7,7,7,7,171,7,7,7,7,7,7,7,]),'while_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'break_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'for_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'switch_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'main_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'funcion_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'llamada_instr':([0,2,28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,105,129,130,133,136,138,139,145,147,149,160,162,167,168,170,172,173,174,175,],[14,14,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,14,14,14,14,14,14,14,55,14,14,14,14,14,14,14,14,14,14,14,]),'inc_decre_instr':([0,2,105,129,130,133,136,138,139,140,147,149,160,162,167,168,170,172,173,174,175,],[15,15,15,15,15,15,15,15,15,154,15,15,15,15,15,15,15,15,15,15,15,]),'return_instr':([0,2,105,129,130,133,136,138,139,147,149,160,162,167,168,170,172,173,174,175,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'finins':([4,5,6,9,14,15,16,],[30,32,33,34,35,36,37,]),'expresion':([28,39,41,42,45,46,48,52,53,54,64,79,80,81,82,83,84,85,86,87,88,89,90,91,100,103,145,],[51,63,65,69,70,71,76,94,95,96,98,114,115,116,117,118,119,120,121,122,123,124,125,126,69,131,161,]),'parametros_llamada':([42,],[67,]),'parametro_llamada':([42,100,],[68,128,]),'inicializacion_inst':([47,],[72,]),'parametros':([78,],[106,]),'parametro':([78,135,],[108,148,]),'tipo':([78,135,],[109,109,]),'default_instr':([132,142,],[141,158,]),'casos_casos_instr':([132,],[142,]),'caso_str':([132,142,],[144,159,]),'avance_inst':([140,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',212),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',216),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',224),
  ('instruccion -> imprimir_instr finins','instruccion',2,'p_instruccion','grammar.py',233),
  ('instruccion -> declaracion_instr finins','instruccion',2,'p_instruccion','grammar.py',234),
  ('instruccion -> asignacion_instr finins','instruccion',2,'p_instruccion','grammar.py',235),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',236),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','grammar.py',237),
  ('instruccion -> break_instr finins','instruccion',2,'p_instruccion','grammar.py',238),
  ('instruccion -> for_instr','instruccion',1,'p_instruccion','grammar.py',239),
  ('instruccion -> switch_instr','instruccion',1,'p_instruccion','grammar.py',240),
  ('instruccion -> main_instr','instruccion',1,'p_instruccion','grammar.py',241),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','grammar.py',242),
  ('instruccion -> llamada_instr finins','instruccion',2,'p_instruccion','grammar.py',243),
  ('instruccion -> inc_decre_instr finins','instruccion',2,'p_instruccion','grammar.py',244),
  ('instruccion -> return_instr finins','instruccion',2,'p_instruccion','grammar.py',245),
  ('finins -> PUNTOCOMA','finins',1,'p_finins','grammar.py',249),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',250),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',254),
  ('imprimir_instr -> RPRINT PARA expresion PARC','imprimir_instr',4,'p_imprimir','grammar.py',260),
  ('declaracion_instr -> RVar ID IGUAL expresion','declaracion_instr',4,'p_declaracion','grammar.py',266),
  ('declaracion_instr -> RVar ID','declaracion_instr',2,'p_declaracion2','grammar.py',270),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion','grammar.py',276),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC','if_instr',7,'p_if1','grammar.py',282),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC','if_instr',11,'p_if2','grammar.py',286),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr','if_instr',9,'p_if3','grammar.py',290),
  ('while_instr -> RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC','while_instr',7,'p_while','grammar.py',296),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',302),
  ('for_instr -> RFOR PARA inicializacion_inst PUNTOCOMA expresion PUNTOCOMA avance_inst PARC LLAVEA instrucciones LLAVEC','for_instr',11,'p_for','grammar.py',308),
  ('inicializacion_inst -> declaracion_instr','inicializacion_inst',1,'p_inicializacion','grammar.py',314),
  ('inicializacion_inst -> asignacion_instr','inicializacion_inst',1,'p_inicializacion','grammar.py',315),
  ('avance_inst -> asignacion_instr','avance_inst',1,'p_avance','grammar.py',320),
  ('avance_inst -> inc_decre_instr','avance_inst',1,'p_avance','grammar.py',321),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA default_instr LLAVEC','switch_instr',7,'p_switch3','grammar.py',327),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA casos_casos_instr LLAVEC','switch_instr',7,'p_switch2','grammar.py',332),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA casos_casos_instr default_instr LLAVEC','switch_instr',8,'p_switch','grammar.py',337),
  ('casos_casos_instr -> casos_casos_instr caso_str','casos_casos_instr',2,'p_casoes_casos_caso','grammar.py',345),
  ('casos_casos_instr -> caso_str','casos_casos_instr',1,'p_casos_caso','grammar.py',351),
  ('caso_str -> RCASE expresion DOSPUNTOS instrucciones','caso_str',4,'p_instruccion_caso','grammar.py',358),
  ('default_instr -> RDEFAULT DOSPUNTOS instrucciones','default_instr',3,'p_default','grammar.py',364),
  ('main_instr -> RMAIN PARA PARC LLAVEA instrucciones LLAVEC','main_instr',6,'p_main','grammar.py',371),
  ('funcion_instr -> RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC','funcion_instr',8,'p_funcion_1','grammar.py',377),
  ('funcion_instr -> RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC','funcion_instr',7,'p_funcion_2','grammar.py',381),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros_1','grammar.py',387),
  ('parametros -> parametro','parametros',1,'p_parametros_2','grammar.py',392),
  ('parametro -> tipo ID','parametro',2,'p_parametro','grammar.py',398),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada1','grammar.py',404),
  ('llamada_instr -> ID PARA parametros_llamada PARC','llamada_instr',4,'p_llamada2','grammar.py',408),
  ('parametros_llamada -> parametros_llamada COMA parametro_llamada','parametros_llamada',3,'p_parametrosLL_1','grammar.py',414),
  ('parametros_llamada -> parametro_llamada','parametros_llamada',1,'p_parametrosLL_2','grammar.py',419),
  ('parametro_llamada -> expresion','parametro_llamada',1,'p_parametroLL','grammar.py',425),
  ('return_instr -> RRETURN expresion','return_instr',2,'p_return','grammar.py',431),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',437),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','grammar.py',438),
  ('tipo -> RSTRING','tipo',1,'p_tipo','grammar.py',439),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','grammar.py',440),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',454),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',455),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',456),
  ('expresion -> expresion DIVI expresion','expresion',3,'p_expresion_binaria','grammar.py',457),
  ('expresion -> expresion ELEV expresion','expresion',3,'p_expresion_binaria','grammar.py',458),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',459),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',460),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',461),
  ('expresion -> expresion IGUALDIF expresion','expresion',3,'p_expresion_binaria','grammar.py',462),
  ('expresion -> expresion MENORIGUALL expresion','expresion',3,'p_expresion_binaria','grammar.py',463),
  ('expresion -> expresion MAYORIGUALL expresion','expresion',3,'p_expresion_binaria','grammar.py',464),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',465),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',466),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',497),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',498),
  ('inc_decre_instr -> ID MASPLUS','inc_decre_instr',2,'p_incremento_decre','grammar.py',507),
  ('inc_decre_instr -> ID MENOSPLUS','inc_decre_instr',2,'p_incremento_decre','grammar.py',508),
  ('expresion -> expresion MASPLUS','expresion',2,'p_expresion_unaria_der','grammar.py',518),
  ('expresion -> expresion MENOSPLUS','expresion',2,'p_expresion_unaria_der','grammar.py',519),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',529),
  ('expresion -> llamada_instr','expresion',1,'p_expresion_llamada','grammar.py',534),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',538),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',542),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','grammar.py',546),
  ('expresion -> CHAR','expresion',1,'p_expresion_char','grammar.py',550),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',554),
  ('expresion -> RTRUE','expresion',1,'p_expresion_true','grammar.py',558),
  ('expresion -> RFALSE','expresion',1,'p_expresion_false','grammar.py',562),
]
