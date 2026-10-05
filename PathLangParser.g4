// PathLang · Analizador SINTÁCTICO
// Las reglas están escritas igual que en el informe (notación de clase):
// lo opcional y lo repetido se expresa con una alternativa vacía (ε),
// así cada árbol de ANTLR corresponde exactamente a una derivación del informe.
parser grammar PathLangParser;
options { tokenVocab = PathLangLexer; }

// ---------- Programa
programa       : sentencias EOF ;
sentencias     : sentencia sentencias | ;
sentencia      : declGrafo | declHeuristica | declRegla | busqueda | mostrar ;

// ---------- C1 · Declaraciones del grafo
declGrafo      : GRAFO ID dirigidoOpt LLAVE_A elementos LLAVE_C ;
dirigidoOpt    : DIRIGIDO | ;
elementos      : elemento elementos | ;
elemento       : declNodo | declArista ;
declNodo       : NODO ID PAR_A coord COMA coord PAR_C PUNTOYCOMA ;
coord          : MENOS NUM | NUM ;
declArista     : ARISTA ID FLECHA ID DOSP peso UNIDAD tipoOpt PUNTOYCOMA ;
peso           : MENOS NUM | NUM ;
tipoOpt        : TIPO ID | ;

// ---------- C2 · Heurísticas: una fórmula que estima el costo restante de n a meta
declHeuristica : HEURISTICA ID PAR_A ID COMA ID PAR_C LLAVE_A RETORNAR expr PUNTOYCOMA LLAVE_C ;

// ---------- Bloques (comunes a C4 y C5)
declRegla      : REGLA ID bloque ;
bloque         : LLAVE_A instrucciones LLAVE_C ;
instrucciones  : instruccion instrucciones | ;
instruccion    : siInstr | paraInstr | asignacion ;

// ---------- C3 · Asignación y expresiones (un nivel por precedencia)
asignacion     : acceso ASIGNA expr PUNTOYCOMA ;
expr           : expr OPREL suma | suma ;
suma           : suma MAS termino | suma MENOS termino | termino ;
termino        : termino POR factor | termino DIV factor | factor ;
factor         : NUM | llamada | acceso | PAR_A expr PAR_C ;
llamada        : ID PAR_A argumentos PAR_C ;
argumentos     : expr masArgumentos | ;
masArgumentos  : COMA expr masArgumentos | ;
acceso         : ID atributoOpt ;
atributoOpt    : PUNTO atributo | ;
atributo       : ID | TIPO ;          // 'tipo' es palabra reservada, pero también es atributo de arista

// ---------- C4 · Selectiva con costo dinámico temporal
siInstr        : SI condicion ENTONCES bloque sinoOpt ;
sinoOpt        : SINO bloque | ;
condicion      : HORA_KW ENTRE HORA Y HORA | expr ;

// ---------- C5 · Iterativa de exploración del grafo
paraInstr      : PARA CADA tipoElemento ID DE ID bloque ;
tipoElemento   : ARISTA | NODO ;

// ---------- C6 · Búsqueda y salida
busqueda       : BUSCAR RUTA ID DESDE ID HASTA ID EN ID USANDO ID conOpt horaOpt PUNTOYCOMA ;
conOpt         : CON ID | ;
horaOpt        : A_LAS HORA | ;
mostrar        : MOSTRAR ID PUNTOYCOMA ;
