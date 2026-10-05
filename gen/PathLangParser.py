# Generated from PathLangParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,317,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,82,8,1,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,3,4,100,8,4,1,5,1,5,1,5,1,5,3,5,106,8,5,1,6,1,6,3,6,
        110,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,124,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,
        139,8,10,1,11,1,11,1,11,3,11,144,8,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,171,8,15,1,16,1,16,1,16,3,
        16,176,8,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,
        18,5,18,189,8,18,10,18,12,18,192,9,18,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,5,19,203,8,19,10,19,12,19,206,9,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,217,8,20,10,20,12,20,220,9,
        20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,229,8,21,1,22,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,3,23,240,8,23,1,24,1,24,1,24,1,
        24,1,24,3,24,247,8,24,1,25,1,25,1,25,1,26,1,26,1,26,3,26,255,8,26,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,3,29,268,
        8,29,1,30,1,30,1,30,1,30,1,30,1,30,3,30,276,8,30,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,3,34,
        306,8,34,1,35,1,35,1,35,3,35,311,8,35,1,36,1,36,1,36,1,36,1,36,0,
        3,36,38,40,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,2,2,0,5,
        5,45,45,1,0,3,4,308,0,74,1,0,0,0,2,81,1,0,0,0,4,88,1,0,0,0,6,90,
        1,0,0,0,8,99,1,0,0,0,10,105,1,0,0,0,12,109,1,0,0,0,14,111,1,0,0,
        0,16,123,1,0,0,0,18,125,1,0,0,0,20,138,1,0,0,0,22,143,1,0,0,0,24,
        145,1,0,0,0,26,158,1,0,0,0,28,162,1,0,0,0,30,170,1,0,0,0,32,175,
        1,0,0,0,34,177,1,0,0,0,36,182,1,0,0,0,38,193,1,0,0,0,40,207,1,0,
        0,0,42,228,1,0,0,0,44,230,1,0,0,0,46,239,1,0,0,0,48,246,1,0,0,0,
        50,248,1,0,0,0,52,254,1,0,0,0,54,256,1,0,0,0,56,258,1,0,0,0,58,267,
        1,0,0,0,60,275,1,0,0,0,62,277,1,0,0,0,64,285,1,0,0,0,66,287,1,0,
        0,0,68,305,1,0,0,0,70,310,1,0,0,0,72,312,1,0,0,0,74,75,3,2,1,0,75,
        76,5,0,0,1,76,1,1,0,0,0,77,78,3,4,2,0,78,79,3,2,1,0,79,82,1,0,0,
        0,80,82,1,0,0,0,81,77,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,89,3,
        6,3,0,84,89,3,24,12,0,85,89,3,26,13,0,86,89,3,66,33,0,87,89,3,72,
        36,0,88,83,1,0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,
        87,1,0,0,0,89,5,1,0,0,0,90,91,5,1,0,0,91,92,5,45,0,0,92,93,3,8,4,
        0,93,94,5,43,0,0,94,95,3,10,5,0,95,96,5,44,0,0,96,7,1,0,0,0,97,100,
        5,2,0,0,98,100,1,0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,100,9,1,0,0,0,
        101,102,3,12,6,0,102,103,3,10,5,0,103,106,1,0,0,0,104,106,1,0,0,
        0,105,101,1,0,0,0,105,104,1,0,0,0,106,11,1,0,0,0,107,110,3,14,7,
        0,108,110,3,18,9,0,109,107,1,0,0,0,109,108,1,0,0,0,110,13,1,0,0,
        0,111,112,5,3,0,0,112,113,5,45,0,0,113,114,5,41,0,0,114,115,3,16,
        8,0,115,116,5,39,0,0,116,117,3,16,8,0,117,118,5,42,0,0,118,119,5,
        38,0,0,119,15,1,0,0,0,120,121,5,34,0,0,121,124,5,29,0,0,122,124,
        5,29,0,0,123,120,1,0,0,0,123,122,1,0,0,0,124,17,1,0,0,0,125,126,
        5,4,0,0,126,127,5,45,0,0,127,128,5,30,0,0,128,129,5,45,0,0,129,130,
        5,37,0,0,130,131,3,20,10,0,131,132,5,27,0,0,132,133,3,22,11,0,133,
        134,5,38,0,0,134,19,1,0,0,0,135,136,5,34,0,0,136,139,5,29,0,0,137,
        139,5,29,0,0,138,135,1,0,0,0,138,137,1,0,0,0,139,21,1,0,0,0,140,
        141,5,5,0,0,141,144,5,45,0,0,142,144,1,0,0,0,143,140,1,0,0,0,143,
        142,1,0,0,0,144,23,1,0,0,0,145,146,5,6,0,0,146,147,5,45,0,0,147,
        148,5,41,0,0,148,149,5,45,0,0,149,150,5,39,0,0,150,151,5,45,0,0,
        151,152,5,42,0,0,152,153,5,43,0,0,153,154,5,17,0,0,154,155,3,36,
        18,0,155,156,5,38,0,0,156,157,5,44,0,0,157,25,1,0,0,0,158,159,5,
        7,0,0,159,160,5,45,0,0,160,161,3,28,14,0,161,27,1,0,0,0,162,163,
        5,43,0,0,163,164,3,30,15,0,164,165,5,44,0,0,165,29,1,0,0,0,166,167,
        3,32,16,0,167,168,3,30,15,0,168,171,1,0,0,0,169,171,1,0,0,0,170,
        166,1,0,0,0,170,169,1,0,0,0,171,31,1,0,0,0,172,176,3,56,28,0,173,
        176,3,62,31,0,174,176,3,34,17,0,175,172,1,0,0,0,175,173,1,0,0,0,
        175,174,1,0,0,0,176,33,1,0,0,0,177,178,3,50,25,0,178,179,5,31,0,
        0,179,180,3,36,18,0,180,181,5,38,0,0,181,35,1,0,0,0,182,183,6,18,
        -1,0,183,184,3,38,19,0,184,190,1,0,0,0,185,186,10,2,0,0,186,187,
        5,32,0,0,187,189,3,38,19,0,188,185,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,37,1,0,0,0,192,190,1,0,0,0,193,194,6,
        19,-1,0,194,195,3,40,20,0,195,204,1,0,0,0,196,197,10,3,0,0,197,198,
        5,33,0,0,198,203,3,40,20,0,199,200,10,2,0,0,200,201,5,34,0,0,201,
        203,3,40,20,0,202,196,1,0,0,0,202,199,1,0,0,0,203,206,1,0,0,0,204,
        202,1,0,0,0,204,205,1,0,0,0,205,39,1,0,0,0,206,204,1,0,0,0,207,208,
        6,20,-1,0,208,209,3,42,21,0,209,218,1,0,0,0,210,211,10,3,0,0,211,
        212,5,35,0,0,212,217,3,42,21,0,213,214,10,2,0,0,214,215,5,36,0,0,
        215,217,3,42,21,0,216,210,1,0,0,0,216,213,1,0,0,0,217,220,1,0,0,
        0,218,216,1,0,0,0,218,219,1,0,0,0,219,41,1,0,0,0,220,218,1,0,0,0,
        221,229,5,29,0,0,222,229,3,44,22,0,223,229,3,50,25,0,224,225,5,41,
        0,0,225,226,3,36,18,0,226,227,5,42,0,0,227,229,1,0,0,0,228,221,1,
        0,0,0,228,222,1,0,0,0,228,223,1,0,0,0,228,224,1,0,0,0,229,43,1,0,
        0,0,230,231,5,45,0,0,231,232,5,41,0,0,232,233,3,46,23,0,233,234,
        5,42,0,0,234,45,1,0,0,0,235,236,3,36,18,0,236,237,3,48,24,0,237,
        240,1,0,0,0,238,240,1,0,0,0,239,235,1,0,0,0,239,238,1,0,0,0,240,
        47,1,0,0,0,241,242,5,39,0,0,242,243,3,36,18,0,243,244,3,48,24,0,
        244,247,1,0,0,0,245,247,1,0,0,0,246,241,1,0,0,0,246,245,1,0,0,0,
        247,49,1,0,0,0,248,249,5,45,0,0,249,250,3,52,26,0,250,51,1,0,0,0,
        251,252,5,40,0,0,252,255,3,54,27,0,253,255,1,0,0,0,254,251,1,0,0,
        0,254,253,1,0,0,0,255,53,1,0,0,0,256,257,7,0,0,0,257,55,1,0,0,0,
        258,259,5,8,0,0,259,260,3,60,30,0,260,261,5,9,0,0,261,262,3,28,14,
        0,262,263,3,58,29,0,263,57,1,0,0,0,264,265,5,10,0,0,265,268,3,28,
        14,0,266,268,1,0,0,0,267,264,1,0,0,0,267,266,1,0,0,0,268,59,1,0,
        0,0,269,270,5,11,0,0,270,271,5,12,0,0,271,272,5,28,0,0,272,273,5,
        13,0,0,273,276,5,28,0,0,274,276,3,36,18,0,275,269,1,0,0,0,275,274,
        1,0,0,0,276,61,1,0,0,0,277,278,5,14,0,0,278,279,5,15,0,0,279,280,
        3,64,32,0,280,281,5,45,0,0,281,282,5,16,0,0,282,283,5,45,0,0,283,
        284,3,28,14,0,284,63,1,0,0,0,285,286,7,1,0,0,286,65,1,0,0,0,287,
        288,5,18,0,0,288,289,5,19,0,0,289,290,5,45,0,0,290,291,5,20,0,0,
        291,292,5,45,0,0,292,293,5,21,0,0,293,294,5,45,0,0,294,295,5,22,
        0,0,295,296,5,45,0,0,296,297,5,23,0,0,297,298,5,45,0,0,298,299,3,
        68,34,0,299,300,3,70,35,0,300,301,5,38,0,0,301,67,1,0,0,0,302,303,
        5,24,0,0,303,306,5,45,0,0,304,306,1,0,0,0,305,302,1,0,0,0,305,304,
        1,0,0,0,306,69,1,0,0,0,307,308,5,25,0,0,308,311,5,28,0,0,309,311,
        1,0,0,0,310,307,1,0,0,0,310,309,1,0,0,0,311,71,1,0,0,0,312,313,5,
        26,0,0,313,314,5,45,0,0,314,315,5,38,0,0,315,73,1,0,0,0,23,81,88,
        99,105,109,123,138,143,170,175,190,202,204,216,218,228,239,246,254,
        267,275,305,310
    ]

class PathLangParser ( Parser ):

    grammarFileName = "PathLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'grafo'", "'dirigido'", "'nodo'", "'arista'", 
                     "'tipo'", "'heuristica'", "'regla'", "'si'", "'entonces'", 
                     "'sino'", "'hora'", "'entre'", "'y'", "'para'", "'cada'", 
                     "'de'", "'retornar'", "'buscar'", "'ruta'", "'desde'", 
                     "'hasta'", "'en'", "'usando'", "'con'", "<INVALID>", 
                     "'mostrar'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "':='", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "':'", "';'", "','", "'.'", "'('", "')'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "GRAFO", "DIRIGIDO", "NODO", "ARISTA", 
                      "TIPO", "HEURISTICA", "REGLA", "SI", "ENTONCES", "SINO", 
                      "HORA_KW", "ENTRE", "Y", "PARA", "CADA", "DE", "RETORNAR", 
                      "BUSCAR", "RUTA", "DESDE", "HASTA", "EN", "USANDO", 
                      "CON", "A_LAS", "MOSTRAR", "UNIDAD", "HORA", "NUM", 
                      "FLECHA", "ASIGNA", "OPREL", "MAS", "MENOS", "POR", 
                      "DIV", "DOSP", "PUNTOYCOMA", "COMA", "PUNTO", "PAR_A", 
                      "PAR_C", "LLAVE_A", "LLAVE_C", "ID", "COMENTARIO", 
                      "WS" ]

    RULE_programa = 0
    RULE_sentencias = 1
    RULE_sentencia = 2
    RULE_declGrafo = 3
    RULE_dirigidoOpt = 4
    RULE_elementos = 5
    RULE_elemento = 6
    RULE_declNodo = 7
    RULE_coord = 8
    RULE_declArista = 9
    RULE_peso = 10
    RULE_tipoOpt = 11
    RULE_declHeuristica = 12
    RULE_declRegla = 13
    RULE_bloque = 14
    RULE_instrucciones = 15
    RULE_instruccion = 16
    RULE_asignacion = 17
    RULE_expr = 18
    RULE_suma = 19
    RULE_termino = 20
    RULE_factor = 21
    RULE_llamada = 22
    RULE_argumentos = 23
    RULE_masArgumentos = 24
    RULE_acceso = 25
    RULE_atributoOpt = 26
    RULE_atributo = 27
    RULE_siInstr = 28
    RULE_sinoOpt = 29
    RULE_condicion = 30
    RULE_paraInstr = 31
    RULE_tipoElemento = 32
    RULE_busqueda = 33
    RULE_conOpt = 34
    RULE_horaOpt = 35
    RULE_mostrar = 36

    ruleNames =  [ "programa", "sentencias", "sentencia", "declGrafo", "dirigidoOpt", 
                   "elementos", "elemento", "declNodo", "coord", "declArista", 
                   "peso", "tipoOpt", "declHeuristica", "declRegla", "bloque", 
                   "instrucciones", "instruccion", "asignacion", "expr", 
                   "suma", "termino", "factor", "llamada", "argumentos", 
                   "masArgumentos", "acceso", "atributoOpt", "atributo", 
                   "siInstr", "sinoOpt", "condicion", "paraInstr", "tipoElemento", 
                   "busqueda", "conOpt", "horaOpt", "mostrar" ]

    EOF = Token.EOF
    GRAFO=1
    DIRIGIDO=2
    NODO=3
    ARISTA=4
    TIPO=5
    HEURISTICA=6
    REGLA=7
    SI=8
    ENTONCES=9
    SINO=10
    HORA_KW=11
    ENTRE=12
    Y=13
    PARA=14
    CADA=15
    DE=16
    RETORNAR=17
    BUSCAR=18
    RUTA=19
    DESDE=20
    HASTA=21
    EN=22
    USANDO=23
    CON=24
    A_LAS=25
    MOSTRAR=26
    UNIDAD=27
    HORA=28
    NUM=29
    FLECHA=30
    ASIGNA=31
    OPREL=32
    MAS=33
    MENOS=34
    POR=35
    DIV=36
    DOSP=37
    PUNTOYCOMA=38
    COMA=39
    PUNTO=40
    PAR_A=41
    PAR_C=42
    LLAVE_A=43
    LLAVE_C=44
    ID=45
    COMENTARIO=46
    WS=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencias(self):
            return self.getTypedRuleContext(PathLangParser.SentenciasContext,0)


        def EOF(self):
            return self.getToken(PathLangParser.EOF, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = PathLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.sentencias()
            self.state = 75
            self.match(PathLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self):
            return self.getTypedRuleContext(PathLangParser.SentenciaContext,0)


        def sentencias(self):
            return self.getTypedRuleContext(PathLangParser.SentenciasContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_sentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencias" ):
                listener.enterSentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencias" ):
                listener.exitSentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencias" ):
                return visitor.visitSentencias(self)
            else:
                return visitor.visitChildren(self)




    def sentencias(self):

        localctx = PathLangParser.SentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencias)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 7, 18, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.sentencia()
                self.state = 78
                self.sentencias()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declGrafo(self):
            return self.getTypedRuleContext(PathLangParser.DeclGrafoContext,0)


        def declHeuristica(self):
            return self.getTypedRuleContext(PathLangParser.DeclHeuristicaContext,0)


        def declRegla(self):
            return self.getTypedRuleContext(PathLangParser.DeclReglaContext,0)


        def busqueda(self):
            return self.getTypedRuleContext(PathLangParser.BusquedaContext,0)


        def mostrar(self):
            return self.getTypedRuleContext(PathLangParser.MostrarContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = PathLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declGrafo()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.declHeuristica()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.declRegla()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.busqueda()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.mostrar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclGrafoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAFO(self):
            return self.getToken(PathLangParser.GRAFO, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def dirigidoOpt(self):
            return self.getTypedRuleContext(PathLangParser.DirigidoOptContext,0)


        def LLAVE_A(self):
            return self.getToken(PathLangParser.LLAVE_A, 0)

        def elementos(self):
            return self.getTypedRuleContext(PathLangParser.ElementosContext,0)


        def LLAVE_C(self):
            return self.getToken(PathLangParser.LLAVE_C, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_declGrafo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclGrafo" ):
                listener.enterDeclGrafo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclGrafo" ):
                listener.exitDeclGrafo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclGrafo" ):
                return visitor.visitDeclGrafo(self)
            else:
                return visitor.visitChildren(self)




    def declGrafo(self):

        localctx = PathLangParser.DeclGrafoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declGrafo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PathLangParser.GRAFO)
            self.state = 91
            self.match(PathLangParser.ID)
            self.state = 92
            self.dirigidoOpt()
            self.state = 93
            self.match(PathLangParser.LLAVE_A)
            self.state = 94
            self.elementos()
            self.state = 95
            self.match(PathLangParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirigidoOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRIGIDO(self):
            return self.getToken(PathLangParser.DIRIGIDO, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_dirigidoOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirigidoOpt" ):
                listener.enterDirigidoOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirigidoOpt" ):
                listener.exitDirigidoOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirigidoOpt" ):
                return visitor.visitDirigidoOpt(self)
            else:
                return visitor.visitChildren(self)




    def dirigidoOpt(self):

        localctx = PathLangParser.DirigidoOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dirigidoOpt)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(PathLangParser.DIRIGIDO)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elemento(self):
            return self.getTypedRuleContext(PathLangParser.ElementoContext,0)


        def elementos(self):
            return self.getTypedRuleContext(PathLangParser.ElementosContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_elementos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementos" ):
                listener.enterElementos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementos" ):
                listener.exitElementos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementos" ):
                return visitor.visitElementos(self)
            else:
                return visitor.visitChildren(self)




    def elementos(self):

        localctx = PathLangParser.ElementosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elementos)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.elemento()
                self.state = 102
                self.elementos()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declNodo(self):
            return self.getTypedRuleContext(PathLangParser.DeclNodoContext,0)


        def declArista(self):
            return self.getTypedRuleContext(PathLangParser.DeclAristaContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_elemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemento" ):
                listener.enterElemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemento" ):
                listener.exitElemento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemento" ):
                return visitor.visitElemento(self)
            else:
                return visitor.visitChildren(self)




    def elemento(self):

        localctx = PathLangParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elemento)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.declNodo()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.declArista()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclNodoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODO(self):
            return self.getToken(PathLangParser.NODO, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def PAR_A(self):
            return self.getToken(PathLangParser.PAR_A, 0)

        def coord(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PathLangParser.CoordContext)
            else:
                return self.getTypedRuleContext(PathLangParser.CoordContext,i)


        def COMA(self):
            return self.getToken(PathLangParser.COMA, 0)

        def PAR_C(self):
            return self.getToken(PathLangParser.PAR_C, 0)

        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_declNodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclNodo" ):
                listener.enterDeclNodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclNodo" ):
                listener.exitDeclNodo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclNodo" ):
                return visitor.visitDeclNodo(self)
            else:
                return visitor.visitChildren(self)




    def declNodo(self):

        localctx = PathLangParser.DeclNodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_declNodo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(PathLangParser.NODO)
            self.state = 112
            self.match(PathLangParser.ID)
            self.state = 113
            self.match(PathLangParser.PAR_A)
            self.state = 114
            self.coord()
            self.state = 115
            self.match(PathLangParser.COMA)
            self.state = 116
            self.coord()
            self.state = 117
            self.match(PathLangParser.PAR_C)
            self.state = 118
            self.match(PathLangParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(PathLangParser.MENOS, 0)

        def NUM(self):
            return self.getToken(PathLangParser.NUM, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_coord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoord" ):
                listener.enterCoord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoord" ):
                listener.exitCoord(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoord" ):
                return visitor.visitCoord(self)
            else:
                return visitor.visitChildren(self)




    def coord(self):

        localctx = PathLangParser.CoordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coord)
        try:
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(PathLangParser.MENOS)
                self.state = 121
                self.match(PathLangParser.NUM)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.match(PathLangParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclAristaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARISTA(self):
            return self.getToken(PathLangParser.ARISTA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PathLangParser.ID)
            else:
                return self.getToken(PathLangParser.ID, i)

        def FLECHA(self):
            return self.getToken(PathLangParser.FLECHA, 0)

        def DOSP(self):
            return self.getToken(PathLangParser.DOSP, 0)

        def peso(self):
            return self.getTypedRuleContext(PathLangParser.PesoContext,0)


        def UNIDAD(self):
            return self.getToken(PathLangParser.UNIDAD, 0)

        def tipoOpt(self):
            return self.getTypedRuleContext(PathLangParser.TipoOptContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_declArista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclArista" ):
                listener.enterDeclArista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclArista" ):
                listener.exitDeclArista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclArista" ):
                return visitor.visitDeclArista(self)
            else:
                return visitor.visitChildren(self)




    def declArista(self):

        localctx = PathLangParser.DeclAristaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declArista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(PathLangParser.ARISTA)
            self.state = 126
            self.match(PathLangParser.ID)
            self.state = 127
            self.match(PathLangParser.FLECHA)
            self.state = 128
            self.match(PathLangParser.ID)
            self.state = 129
            self.match(PathLangParser.DOSP)
            self.state = 130
            self.peso()
            self.state = 131
            self.match(PathLangParser.UNIDAD)
            self.state = 132
            self.tipoOpt()
            self.state = 133
            self.match(PathLangParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(PathLangParser.MENOS, 0)

        def NUM(self):
            return self.getToken(PathLangParser.NUM, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_peso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPeso" ):
                listener.enterPeso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPeso" ):
                listener.exitPeso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPeso" ):
                return visitor.visitPeso(self)
            else:
                return visitor.visitChildren(self)




    def peso(self):

        localctx = PathLangParser.PesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_peso)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(PathLangParser.MENOS)
                self.state = 136
                self.match(PathLangParser.NUM)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(PathLangParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(PathLangParser.TIPO, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_tipoOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoOpt" ):
                listener.enterTipoOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoOpt" ):
                listener.exitTipoOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoOpt" ):
                return visitor.visitTipoOpt(self)
            else:
                return visitor.visitChildren(self)




    def tipoOpt(self):

        localctx = PathLangParser.TipoOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipoOpt)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(PathLangParser.TIPO)
                self.state = 141
                self.match(PathLangParser.ID)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclHeuristicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEURISTICA(self):
            return self.getToken(PathLangParser.HEURISTICA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PathLangParser.ID)
            else:
                return self.getToken(PathLangParser.ID, i)

        def PAR_A(self):
            return self.getToken(PathLangParser.PAR_A, 0)

        def COMA(self):
            return self.getToken(PathLangParser.COMA, 0)

        def PAR_C(self):
            return self.getToken(PathLangParser.PAR_C, 0)

        def LLAVE_A(self):
            return self.getToken(PathLangParser.LLAVE_A, 0)

        def RETORNAR(self):
            return self.getToken(PathLangParser.RETORNAR, 0)

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def LLAVE_C(self):
            return self.getToken(PathLangParser.LLAVE_C, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_declHeuristica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclHeuristica" ):
                listener.enterDeclHeuristica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclHeuristica" ):
                listener.exitDeclHeuristica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclHeuristica" ):
                return visitor.visitDeclHeuristica(self)
            else:
                return visitor.visitChildren(self)




    def declHeuristica(self):

        localctx = PathLangParser.DeclHeuristicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declHeuristica)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(PathLangParser.HEURISTICA)
            self.state = 146
            self.match(PathLangParser.ID)
            self.state = 147
            self.match(PathLangParser.PAR_A)
            self.state = 148
            self.match(PathLangParser.ID)
            self.state = 149
            self.match(PathLangParser.COMA)
            self.state = 150
            self.match(PathLangParser.ID)
            self.state = 151
            self.match(PathLangParser.PAR_C)
            self.state = 152
            self.match(PathLangParser.LLAVE_A)
            self.state = 153
            self.match(PathLangParser.RETORNAR)
            self.state = 154
            self.expr(0)
            self.state = 155
            self.match(PathLangParser.PUNTOYCOMA)
            self.state = 156
            self.match(PathLangParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclReglaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGLA(self):
            return self.getToken(PathLangParser.REGLA, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def bloque(self):
            return self.getTypedRuleContext(PathLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_declRegla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclRegla" ):
                listener.enterDeclRegla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclRegla" ):
                listener.exitDeclRegla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclRegla" ):
                return visitor.visitDeclRegla(self)
            else:
                return visitor.visitChildren(self)




    def declRegla(self):

        localctx = PathLangParser.DeclReglaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declRegla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(PathLangParser.REGLA)
            self.state = 159
            self.match(PathLangParser.ID)
            self.state = 160
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_A(self):
            return self.getToken(PathLangParser.LLAVE_A, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(PathLangParser.InstruccionesContext,0)


        def LLAVE_C(self):
            return self.getToken(PathLangParser.LLAVE_C, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = PathLangParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(PathLangParser.LLAVE_A)
            self.state = 163
            self.instrucciones()
            self.state = 164
            self.match(PathLangParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(PathLangParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(PathLangParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = PathLangParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instrucciones)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 14, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.instruccion()
                self.state = 167
                self.instrucciones()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def siInstr(self):
            return self.getTypedRuleContext(PathLangParser.SiInstrContext,0)


        def paraInstr(self):
            return self.getTypedRuleContext(PathLangParser.ParaInstrContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(PathLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = PathLangParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instruccion)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.siInstr()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.paraInstr()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acceso(self):
            return self.getTypedRuleContext(PathLangParser.AccesoContext,0)


        def ASIGNA(self):
            return self.getToken(PathLangParser.ASIGNA, 0)

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = PathLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.acceso()
            self.state = 178
            self.match(PathLangParser.ASIGNA)
            self.state = 179
            self.expr(0)
            self.state = 180
            self.match(PathLangParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def suma(self):
            return self.getTypedRuleContext(PathLangParser.SumaContext,0)


        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def OPREL(self):
            return self.getToken(PathLangParser.OPREL, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PathLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.suma(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PathLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    self.match(PathLangParser.OPREL)
                    self.state = 187
                    self.suma(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class SumaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(PathLangParser.TerminoContext,0)


        def suma(self):
            return self.getTypedRuleContext(PathLangParser.SumaContext,0)


        def MAS(self):
            return self.getToken(PathLangParser.MAS, 0)

        def MENOS(self):
            return self.getToken(PathLangParser.MENOS, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_suma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)



    def suma(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PathLangParser.SumaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_suma, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = PathLangParser.SumaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_suma)
                        self.state = 196
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 197
                        self.match(PathLangParser.MAS)
                        self.state = 198
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = PathLangParser.SumaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_suma)
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        self.match(PathLangParser.MENOS)
                        self.state = 201
                        self.termino(0)
                        pass

             
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(PathLangParser.FactorContext,0)


        def termino(self):
            return self.getTypedRuleContext(PathLangParser.TerminoContext,0)


        def POR(self):
            return self.getToken(PathLangParser.POR, 0)

        def DIV(self):
            return self.getToken(PathLangParser.DIV, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PathLangParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = PathLangParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 210
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 211
                        self.match(PathLangParser.POR)
                        self.state = 212
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = PathLangParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 213
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 214
                        self.match(PathLangParser.DIV)
                        self.state = 215
                        self.factor()
                        pass

             
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(PathLangParser.NUM, 0)

        def llamada(self):
            return self.getTypedRuleContext(PathLangParser.LlamadaContext,0)


        def acceso(self):
            return self.getTypedRuleContext(PathLangParser.AccesoContext,0)


        def PAR_A(self):
            return self.getToken(PathLangParser.PAR_A, 0)

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def PAR_C(self):
            return self.getToken(PathLangParser.PAR_C, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = PathLangParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(PathLangParser.NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.llamada()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.acceso()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.match(PathLangParser.PAR_A)
                self.state = 225
                self.expr(0)
                self.state = 226
                self.match(PathLangParser.PAR_C)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def PAR_A(self):
            return self.getToken(PathLangParser.PAR_A, 0)

        def argumentos(self):
            return self.getTypedRuleContext(PathLangParser.ArgumentosContext,0)


        def PAR_C(self):
            return self.getToken(PathLangParser.PAR_C, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = PathLangParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(PathLangParser.ID)
            self.state = 231
            self.match(PathLangParser.PAR_A)
            self.state = 232
            self.argumentos()
            self.state = 233
            self.match(PathLangParser.PAR_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def masArgumentos(self):
            return self.getTypedRuleContext(PathLangParser.MasArgumentosContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = PathLangParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argumentos)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 41, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.expr(0)
                self.state = 236
                self.masArgumentos()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MasArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(PathLangParser.COMA, 0)

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def masArgumentos(self):
            return self.getTypedRuleContext(PathLangParser.MasArgumentosContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_masArgumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMasArgumentos" ):
                listener.enterMasArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMasArgumentos" ):
                listener.exitMasArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMasArgumentos" ):
                return visitor.visitMasArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def masArgumentos(self):

        localctx = PathLangParser.MasArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_masArgumentos)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(PathLangParser.COMA)
                self.state = 242
                self.expr(0)
                self.state = 243
                self.masArgumentos()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def atributoOpt(self):
            return self.getTypedRuleContext(PathLangParser.AtributoOptContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_acceso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcceso" ):
                listener.enterAcceso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcceso" ):
                listener.exitAcceso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcceso" ):
                return visitor.visitAcceso(self)
            else:
                return visitor.visitChildren(self)




    def acceso(self):

        localctx = PathLangParser.AccesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_acceso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(PathLangParser.ID)
            self.state = 249
            self.atributoOpt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtributoOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(PathLangParser.PUNTO, 0)

        def atributo(self):
            return self.getTypedRuleContext(PathLangParser.AtributoContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_atributoOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtributoOpt" ):
                listener.enterAtributoOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtributoOpt" ):
                listener.exitAtributoOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtributoOpt" ):
                return visitor.visitAtributoOpt(self)
            else:
                return visitor.visitChildren(self)




    def atributoOpt(self):

        localctx = PathLangParser.AtributoOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_atributoOpt)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(PathLangParser.PUNTO)
                self.state = 252
                self.atributo()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtributoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def TIPO(self):
            return self.getToken(PathLangParser.TIPO, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_atributo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtributo" ):
                listener.enterAtributo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtributo" ):
                listener.exitAtributo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtributo" ):
                return visitor.visitAtributo(self)
            else:
                return visitor.visitChildren(self)




    def atributo(self):

        localctx = PathLangParser.AtributoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atributo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not(_la==5 or _la==45):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SiInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(PathLangParser.SI, 0)

        def condicion(self):
            return self.getTypedRuleContext(PathLangParser.CondicionContext,0)


        def ENTONCES(self):
            return self.getToken(PathLangParser.ENTONCES, 0)

        def bloque(self):
            return self.getTypedRuleContext(PathLangParser.BloqueContext,0)


        def sinoOpt(self):
            return self.getTypedRuleContext(PathLangParser.SinoOptContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_siInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSiInstr" ):
                listener.enterSiInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSiInstr" ):
                listener.exitSiInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSiInstr" ):
                return visitor.visitSiInstr(self)
            else:
                return visitor.visitChildren(self)




    def siInstr(self):

        localctx = PathLangParser.SiInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_siInstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(PathLangParser.SI)
            self.state = 259
            self.condicion()
            self.state = 260
            self.match(PathLangParser.ENTONCES)
            self.state = 261
            self.bloque()
            self.state = 262
            self.sinoOpt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinoOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(PathLangParser.SINO, 0)

        def bloque(self):
            return self.getTypedRuleContext(PathLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_sinoOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinoOpt" ):
                listener.enterSinoOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinoOpt" ):
                listener.exitSinoOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinoOpt" ):
                return visitor.visitSinoOpt(self)
            else:
                return visitor.visitChildren(self)




    def sinoOpt(self):

        localctx = PathLangParser.SinoOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_sinoOpt)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(PathLangParser.SINO)
                self.state = 265
                self.bloque()
                pass
            elif token in [8, 14, 44, 45]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HORA_KW(self):
            return self.getToken(PathLangParser.HORA_KW, 0)

        def ENTRE(self):
            return self.getToken(PathLangParser.ENTRE, 0)

        def HORA(self, i:int=None):
            if i is None:
                return self.getTokens(PathLangParser.HORA)
            else:
                return self.getToken(PathLangParser.HORA, i)

        def Y(self):
            return self.getToken(PathLangParser.Y, 0)

        def expr(self):
            return self.getTypedRuleContext(PathLangParser.ExprContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = PathLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_condicion)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(PathLangParser.HORA_KW)
                self.state = 270
                self.match(PathLangParser.ENTRE)
                self.state = 271
                self.match(PathLangParser.HORA)
                self.state = 272
                self.match(PathLangParser.Y)
                self.state = 273
                self.match(PathLangParser.HORA)
                pass
            elif token in [29, 41, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaInstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(PathLangParser.PARA, 0)

        def CADA(self):
            return self.getToken(PathLangParser.CADA, 0)

        def tipoElemento(self):
            return self.getTypedRuleContext(PathLangParser.TipoElementoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PathLangParser.ID)
            else:
                return self.getToken(PathLangParser.ID, i)

        def DE(self):
            return self.getToken(PathLangParser.DE, 0)

        def bloque(self):
            return self.getTypedRuleContext(PathLangParser.BloqueContext,0)


        def getRuleIndex(self):
            return PathLangParser.RULE_paraInstr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParaInstr" ):
                listener.enterParaInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParaInstr" ):
                listener.exitParaInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaInstr" ):
                return visitor.visitParaInstr(self)
            else:
                return visitor.visitChildren(self)




    def paraInstr(self):

        localctx = PathLangParser.ParaInstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_paraInstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(PathLangParser.PARA)
            self.state = 278
            self.match(PathLangParser.CADA)
            self.state = 279
            self.tipoElemento()
            self.state = 280
            self.match(PathLangParser.ID)
            self.state = 281
            self.match(PathLangParser.DE)
            self.state = 282
            self.match(PathLangParser.ID)
            self.state = 283
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARISTA(self):
            return self.getToken(PathLangParser.ARISTA, 0)

        def NODO(self):
            return self.getToken(PathLangParser.NODO, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_tipoElemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoElemento" ):
                listener.enterTipoElemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoElemento" ):
                listener.exitTipoElemento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoElemento" ):
                return visitor.visitTipoElemento(self)
            else:
                return visitor.visitChildren(self)




    def tipoElemento(self):

        localctx = PathLangParser.TipoElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_tipoElemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BusquedaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUSCAR(self):
            return self.getToken(PathLangParser.BUSCAR, 0)

        def RUTA(self):
            return self.getToken(PathLangParser.RUTA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PathLangParser.ID)
            else:
                return self.getToken(PathLangParser.ID, i)

        def DESDE(self):
            return self.getToken(PathLangParser.DESDE, 0)

        def HASTA(self):
            return self.getToken(PathLangParser.HASTA, 0)

        def EN(self):
            return self.getToken(PathLangParser.EN, 0)

        def USANDO(self):
            return self.getToken(PathLangParser.USANDO, 0)

        def conOpt(self):
            return self.getTypedRuleContext(PathLangParser.ConOptContext,0)


        def horaOpt(self):
            return self.getTypedRuleContext(PathLangParser.HoraOptContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_busqueda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBusqueda" ):
                listener.enterBusqueda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBusqueda" ):
                listener.exitBusqueda(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBusqueda" ):
                return visitor.visitBusqueda(self)
            else:
                return visitor.visitChildren(self)




    def busqueda(self):

        localctx = PathLangParser.BusquedaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_busqueda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(PathLangParser.BUSCAR)
            self.state = 288
            self.match(PathLangParser.RUTA)
            self.state = 289
            self.match(PathLangParser.ID)
            self.state = 290
            self.match(PathLangParser.DESDE)
            self.state = 291
            self.match(PathLangParser.ID)
            self.state = 292
            self.match(PathLangParser.HASTA)
            self.state = 293
            self.match(PathLangParser.ID)
            self.state = 294
            self.match(PathLangParser.EN)
            self.state = 295
            self.match(PathLangParser.ID)
            self.state = 296
            self.match(PathLangParser.USANDO)
            self.state = 297
            self.match(PathLangParser.ID)
            self.state = 298
            self.conOpt()
            self.state = 299
            self.horaOpt()
            self.state = 300
            self.match(PathLangParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CON(self):
            return self.getToken(PathLangParser.CON, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_conOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConOpt" ):
                listener.enterConOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConOpt" ):
                listener.exitConOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConOpt" ):
                return visitor.visitConOpt(self)
            else:
                return visitor.visitChildren(self)




    def conOpt(self):

        localctx = PathLangParser.ConOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_conOpt)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.match(PathLangParser.CON)
                self.state = 303
                self.match(PathLangParser.ID)
                pass
            elif token in [25, 38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HoraOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A_LAS(self):
            return self.getToken(PathLangParser.A_LAS, 0)

        def HORA(self):
            return self.getToken(PathLangParser.HORA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_horaOpt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHoraOpt" ):
                listener.enterHoraOpt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHoraOpt" ):
                listener.exitHoraOpt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHoraOpt" ):
                return visitor.visitHoraOpt(self)
            else:
                return visitor.visitChildren(self)




    def horaOpt(self):

        localctx = PathLangParser.HoraOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_horaOpt)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(PathLangParser.A_LAS)
                self.state = 308
                self.match(PathLangParser.HORA)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MostrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(PathLangParser.MOSTRAR, 0)

        def ID(self):
            return self.getToken(PathLangParser.ID, 0)

        def PUNTOYCOMA(self):
            return self.getToken(PathLangParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return PathLangParser.RULE_mostrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMostrar" ):
                listener.enterMostrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMostrar" ):
                listener.exitMostrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMostrar" ):
                return visitor.visitMostrar(self)
            else:
                return visitor.visitChildren(self)




    def mostrar(self):

        localctx = PathLangParser.MostrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_mostrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(PathLangParser.MOSTRAR)
            self.state = 313
            self.match(PathLangParser.ID)
            self.state = 314
            self.match(PathLangParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        self._predicates[19] = self.suma_sempred
        self._predicates[20] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def suma_sempred(self, localctx:SumaContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




