
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftMENORQUEMAYORQUEIGUALIGUALleftMASMENOSleftPORrightUMENOSAND CADENA COMA DECIMAL ENTERO ID IGUAL IGUALIGUAL LLAVEA LLAVEC MAS MAYORQUE MENORQUE MENOS NOT OR PARA PARC POR PUNTOCOMA RBOOLEAN RBREAK RELSE RFALSE RFLOAT RFUNC RIF RINT RMAIN RPRINT RRETURN RSTRING RTRUE RWHILEinit            : instruccionesinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr finins\n                        | declaracion_instr finins\n                        | asignacion_instr finins\n                        | if_instr\n                        | while_instr\n                        | break_instr finins\n                        | main_instr\n                        | funcion_instr\n                        | llamada_instr finins\n                        | return_instr fininsfinins       : PUNTOCOMA\n                    | instruccion        : error PUNTOCOMAimprimir_instr     : RPRINT PARA expresion PARCdeclaracion_instr     : tipo ID IGUAL expresionasignacion_instr     : ID IGUAL expresionif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instrwhile_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVECbreak_instr     : RBREAKmain_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVECparametros     : parametros COMA parametroparametros    : parametroparametro     : tipo IDllamada_instr     : ID PARA PARCllamada_instr     : ID PARA parametros_llamada PARCparametros_llamada     : parametros_llamada COMA parametro_llamadaparametros_llamada    : parametro_llamadaparametro_llamada     : expresionreturn_instr     : RRETURN expresiontipo     : RINT\n                | RFLOAT\n                | RSTRING\n                | RBOOLEAN \n    expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion MENORQUE expresion\n            | expresion MAYORQUE expresion\n            | expresion IGUALIGUAL expresion\n            | expresion AND expresion\n            | expresion OR expresion\n    \n    expresion : MENOS expresion %prec UMENOS \n            | NOT expresion %prec UNOT \n    \n    expresion :   PARA expresion PARC \n    expresion : llamada_instrexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : RTRUEexpresion : RFALSE'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[14,14,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,14,-41,-42,-43,-44,-45,-46,-47,-48,-51,14,14,14,14,14,14,-25,14,14,-20,-23,14,-27,-26,14,-22,14,-21,]),'RPRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[15,15,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,15,-41,-42,-43,-44,-45,-46,-47,-48,-51,15,15,15,15,15,15,-25,15,15,-20,-23,15,-27,-26,15,-22,15,-21,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,45,46,47,48,49,50,51,52,53,54,55,57,58,59,67,68,69,70,71,72,73,74,75,76,78,79,80,81,84,88,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[17,17,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,38,-24,44,50,-37,-38,-39,-40,-2,-4,-14,-5,-6,-9,-12,-13,-16,50,50,50,50,50,-36,50,50,50,-52,-53,-54,-55,-56,-57,-58,50,-19,-31,50,50,50,50,50,50,50,50,-49,-50,-17,-18,-32,50,17,105,-41,-42,-43,-44,-45,-46,-47,-48,-51,17,17,17,17,17,17,-25,17,17,-20,-23,17,-27,-26,17,-22,17,-21,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,],[18,18,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,18,-41,-42,-43,-44,-45,-46,-47,-48,-51,18,18,18,18,18,18,-25,18,18,-20,-23,18,-27,18,-26,18,-22,18,-21,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[19,19,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,19,-41,-42,-43,-44,-45,-46,-47,-48,-51,19,19,19,19,19,19,-25,19,19,-20,-23,19,-27,-26,19,-22,19,-21,]),'RBREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[20,20,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,20,-41,-42,-43,-44,-45,-46,-47,-48,-51,20,20,20,20,20,20,-25,20,20,-20,-23,20,-27,-26,20,-22,20,-21,]),'RMAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[21,21,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,21,-41,-42,-43,-44,-45,-46,-47,-48,-51,21,21,21,21,21,21,-25,21,21,-20,-23,21,-27,-26,21,-22,21,-21,]),'RFUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[22,22,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,22,-41,-42,-43,-44,-45,-46,-47,-48,-51,22,22,22,22,22,22,-25,22,22,-20,-23,22,-27,-26,22,-22,22,-21,]),'RRETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[23,23,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,23,-41,-42,-43,-44,-45,-46,-47,-48,-51,23,23,23,23,23,23,-25,23,23,-20,-23,23,-27,-26,23,-22,23,-21,]),'RINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,66,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,103,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[24,24,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,24,-49,-50,-17,-18,-32,24,-41,-42,-43,-44,-45,-46,-47,-48,-51,24,24,24,24,24,24,24,-25,24,24,-20,-23,24,-27,-26,24,-22,24,-21,]),'RFLOAT':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,66,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,103,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[25,25,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,25,-49,-50,-17,-18,-32,25,-41,-42,-43,-44,-45,-46,-47,-48,-51,25,25,25,25,25,25,25,-25,25,25,-20,-23,25,-27,-26,25,-22,25,-21,]),'RSTRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,66,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,103,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[26,26,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,26,-49,-50,-17,-18,-32,26,-41,-42,-43,-44,-45,-46,-47,-48,-51,26,26,26,26,26,26,26,-25,26,26,-20,-23,26,-27,-26,26,-22,26,-21,]),'RBOOLEAN':([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,66,75,76,78,79,80,84,89,90,91,92,93,94,95,96,97,99,100,101,103,104,106,107,108,109,111,112,113,114,115,117,118,119,120,121,],[27,27,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,27,-49,-50,-17,-18,-32,27,-41,-42,-43,-44,-45,-46,-47,-48,-51,27,27,27,27,27,27,27,-25,27,27,-20,-23,27,-27,-26,27,-22,27,-21,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,89,90,91,92,93,94,95,96,97,108,112,113,115,117,119,121,],[0,-1,-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,-41,-42,-43,-44,-45,-46,-47,-48,-51,-25,-20,-23,-27,-26,-22,-21,]),'LLAVEC':([3,4,5,6,7,8,9,10,11,12,13,20,28,29,30,31,32,33,34,35,36,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,89,90,91,92,93,94,95,96,97,101,106,107,108,111,112,113,114,115,117,119,120,121,],[-3,-15,-15,-15,-7,-8,-15,-10,-11,-15,-15,-24,-2,-4,-14,-5,-6,-9,-12,-13,-16,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,-41,-42,-43,-44,-45,-46,-47,-48,-51,108,112,113,-25,115,-20,-23,117,-27,-26,-22,121,-21,]),'PUNTOCOMA':([4,5,6,9,12,13,14,20,45,49,50,51,52,53,54,55,58,59,75,76,78,79,80,89,90,91,92,93,94,95,96,97,],[30,30,30,30,30,30,36,-24,-36,-52,-53,-54,-55,-56,-57,-58,-19,-31,-49,-50,-17,-18,-32,-41,-42,-43,-44,-45,-46,-47,-48,-51,]),'PARA':([15,17,18,19,21,23,37,39,40,41,42,44,46,47,48,50,57,67,68,69,70,71,72,73,74,81,],[37,40,41,42,43,48,48,48,48,48,48,66,48,48,48,40,48,48,48,48,48,48,48,48,48,48,]),'IGUAL':([17,38,],[39,57,]),'MENOS':([23,37,39,40,41,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,63,64,67,68,69,70,71,72,73,74,75,76,77,79,80,81,89,90,91,92,93,94,95,96,97,],[46,46,46,46,46,46,68,46,46,46,-52,-53,-54,-55,-56,-57,-58,68,46,68,-31,68,68,68,46,46,46,46,46,46,46,46,-49,68,68,68,-32,46,-41,-42,-43,68,68,68,68,68,-51,]),'NOT':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'ENTERO':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'DECIMAL':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'CADENA':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'RTRUE':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'RFALSE':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'PARC':([40,43,49,50,51,52,53,54,55,56,59,60,61,62,63,64,66,75,76,77,80,85,87,89,90,91,92,93,94,95,96,97,98,105,110,],[59,65,-52,-53,-54,-55,-56,-57,-58,78,-31,80,-34,-35,82,83,86,-49,-50,97,-32,102,-29,-41,-42,-43,-44,-45,-46,-47,-48,-51,-33,-30,-28,]),'MAS':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[67,-52,-53,-54,-55,-56,-57,-58,67,67,-31,67,67,67,-49,67,67,67,-32,-41,-42,-43,67,67,67,67,67,-51,]),'POR':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[69,-52,-53,-54,-55,-56,-57,-58,69,69,-31,69,69,69,-49,69,69,69,-32,69,69,-43,69,69,69,69,69,-51,]),'MENORQUE':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[70,-52,-53,-54,-55,-56,-57,-58,70,70,-31,70,70,70,-49,70,70,70,-32,-41,-42,-43,-44,-45,-46,70,70,-51,]),'MAYORQUE':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[71,-52,-53,-54,-55,-56,-57,-58,71,71,-31,71,71,71,-49,71,71,71,-32,-41,-42,-43,-44,-45,-46,71,71,-51,]),'IGUALIGUAL':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[72,-52,-53,-54,-55,-56,-57,-58,72,72,-31,72,72,72,-49,72,72,72,-32,-41,-42,-43,-44,-45,-46,72,72,-51,]),'AND':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[73,-52,-53,-54,-55,-56,-57,-58,73,73,-31,73,73,73,-49,-50,73,73,-32,-41,-42,-43,-44,-45,-46,-47,73,-51,]),'OR':([45,49,50,51,52,53,54,55,56,58,59,62,63,64,75,76,77,79,80,89,90,91,92,93,94,95,96,97,],[74,-52,-53,-54,-55,-56,-57,-58,74,74,-31,74,74,74,-49,-50,74,74,-32,-41,-42,-43,-44,-45,-46,-47,-48,-51,]),'COMA':([49,50,51,52,53,54,55,59,60,61,62,75,76,80,85,87,89,90,91,92,93,94,95,96,97,98,105,110,],[-52,-53,-54,-55,-56,-57,-58,-31,81,-34,-35,-49,-50,-32,103,-29,-41,-42,-43,-44,-45,-46,-47,-48,-51,-33,-30,-28,]),'LLAVEA':([65,82,83,86,102,116,],[84,99,100,104,109,118,]),'RELSE':([112,],[116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,84,99,100,104,109,118,],[2,101,106,107,111,114,120,]),'instruccion':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[3,28,3,3,3,28,3,28,28,3,28,28,3,28,]),'imprimir_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'if_instr':([0,2,84,99,100,101,104,106,107,109,111,114,116,118,120,],[7,7,7,7,7,7,7,7,7,7,7,7,119,7,7,]),'while_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'break_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'main_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'funcion_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'llamada_instr':([0,2,23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,84,99,100,101,104,106,107,109,111,114,118,120,],[12,12,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,12,12,12,12,12,12,12,12,12,12,12,12,]),'return_instr':([0,2,84,99,100,101,104,106,107,109,111,114,118,120,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'tipo':([0,2,66,84,99,100,101,103,104,106,107,109,111,114,118,120,],[16,16,88,16,16,16,16,88,16,16,16,16,16,16,16,16,]),'finins':([4,5,6,9,12,13,],[29,31,32,33,34,35,]),'expresion':([23,37,39,40,41,42,46,47,48,57,67,68,69,70,71,72,73,74,81,],[45,56,58,62,63,64,75,76,77,79,89,90,91,92,93,94,95,96,62,]),'parametros_llamada':([40,],[60,]),'parametro_llamada':([40,81,],[61,98,]),'parametros':([66,],[85,]),'parametro':([66,103,],[87,110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',158),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',162),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',170),
  ('instruccion -> imprimir_instr finins','instruccion',2,'p_instruccion','grammar.py',179),
  ('instruccion -> declaracion_instr finins','instruccion',2,'p_instruccion','grammar.py',180),
  ('instruccion -> asignacion_instr finins','instruccion',2,'p_instruccion','grammar.py',181),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',182),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','grammar.py',183),
  ('instruccion -> break_instr finins','instruccion',2,'p_instruccion','grammar.py',184),
  ('instruccion -> main_instr','instruccion',1,'p_instruccion','grammar.py',185),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','grammar.py',186),
  ('instruccion -> llamada_instr finins','instruccion',2,'p_instruccion','grammar.py',187),
  ('instruccion -> return_instr finins','instruccion',2,'p_instruccion','grammar.py',188),
  ('finins -> PUNTOCOMA','finins',1,'p_finins','grammar.py',192),
  ('finins -> <empty>','finins',0,'p_finins','grammar.py',193),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',197),
  ('imprimir_instr -> RPRINT PARA expresion PARC','imprimir_instr',4,'p_imprimir','grammar.py',203),
  ('declaracion_instr -> tipo ID IGUAL expresion','declaracion_instr',4,'p_declaracion','grammar.py',209),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion','grammar.py',215),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC','if_instr',7,'p_if1','grammar.py',221),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC','if_instr',11,'p_if2','grammar.py',225),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr','if_instr',9,'p_if3','grammar.py',229),
  ('while_instr -> RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC','while_instr',7,'p_while','grammar.py',235),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',241),
  ('main_instr -> RMAIN PARA PARC LLAVEA instrucciones LLAVEC','main_instr',6,'p_main','grammar.py',247),
  ('funcion_instr -> RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC','funcion_instr',8,'p_funcion_1','grammar.py',253),
  ('funcion_instr -> RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC','funcion_instr',7,'p_funcion_2','grammar.py',257),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros_1','grammar.py',263),
  ('parametros -> parametro','parametros',1,'p_parametros_2','grammar.py',268),
  ('parametro -> tipo ID','parametro',2,'p_parametro','grammar.py',274),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada1','grammar.py',280),
  ('llamada_instr -> ID PARA parametros_llamada PARC','llamada_instr',4,'p_llamada2','grammar.py',284),
  ('parametros_llamada -> parametros_llamada COMA parametro_llamada','parametros_llamada',3,'p_parametrosLL_1','grammar.py',290),
  ('parametros_llamada -> parametro_llamada','parametros_llamada',1,'p_parametrosLL_2','grammar.py',295),
  ('parametro_llamada -> expresion','parametro_llamada',1,'p_parametroLL','grammar.py',301),
  ('return_instr -> RRETURN expresion','return_instr',2,'p_return','grammar.py',307),
  ('tipo -> RINT','tipo',1,'p_tipo','grammar.py',313),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','grammar.py',314),
  ('tipo -> RSTRING','tipo',1,'p_tipo','grammar.py',315),
  ('tipo -> RBOOLEAN','tipo',1,'p_tipo','grammar.py',316),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',330),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',331),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',332),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',333),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',334),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',335),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',336),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',337),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',358),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',359),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',368),
  ('expresion -> llamada_instr','expresion',1,'p_expresion_llamada','grammar.py',373),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',377),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',381),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','grammar.py',385),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',389),
  ('expresion -> RTRUE','expresion',1,'p_expresion_true','grammar.py',393),
  ('expresion -> RFALSE','expresion',1,'p_expresion_false','grammar.py',397),
]
