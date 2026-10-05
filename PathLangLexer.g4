// PathLang · Analizador LÉXICO
// Cada regla es una expresión regular. Orden: palabras reservadas antes que ID
// (en empate de longitud gana la regla escrita primero; si no, gana el lexema más largo).
lexer grammar PathLangLexer;

// ---------- Palabras reservadas
GRAFO      : 'grafo' ;
DIRIGIDO   : 'dirigido' ;
NODO       : 'nodo' ;
ARISTA     : 'arista' ;
TIPO       : 'tipo' ;
HEURISTICA : 'heuristica' ;
REGLA      : 'regla' ;
SI         : 'si' ;
ENTONCES   : 'entonces' ;
SINO       : 'sino' ;
HORA_KW    : 'hora' ;
ENTRE      : 'entre' ;
Y          : 'y' ;
PARA       : 'para' ;
CADA       : 'cada' ;
DE         : 'de' ;
RETORNAR   : 'retornar' ;
BUSCAR     : 'buscar' ;
RUTA       : 'ruta' ;
DESDE      : 'desde' ;
HASTA      : 'hasta' ;
EN         : 'en' ;
USANDO     : 'usando' ;
CON        : 'con' ;
A_LAS      : 'a' [ \t]+ 'las' ;          // 'a las' es UN token: gana por ser más largo que ID('a')
MOSTRAR    : 'mostrar' ;
UNIDAD     : 'min' | 'km' ;

// ---------- Literales
HORA       : [0-9][0-9] ':' [0-9][0-9] ;  // solo la forma; el rango (00:00 a 23:59) lo valida el semántico
NUM        : [0-9]+ ('.' [0-9]+)? ;      // sin signo: el "-" es un token aparte (MENOS)

// ---------- Operadores y puntuación
FLECHA     : '->' | '<->' ;
ASIGNA     : ':=' ;
OPREL      : '==' | '!=' | '<=' | '>=' | '<' | '>' ;
MAS        : '+' ;
MENOS      : '-' ;
POR        : '*' ;
DIV        : '/' ;
DOSP       : ':' ;
PUNTOYCOMA : ';' ;
COMA       : ',' ;
PUNTO      : '.' ;
PAR_A      : '(' ;
PAR_C      : ')' ;
LLAVE_A    : '{' ;
LLAVE_C    : '}' ;

// ---------- Identificadores (al final: no deben capturar palabras reservadas)
ID         : [a-zA-Z_][a-zA-Z_0-9]* ;
COMENTARIO : '//' ~[\r\n]* -> skip ;
WS         : [ \t\r\n]+ -> skip ;
