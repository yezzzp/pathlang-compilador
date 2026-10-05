# Generated from PathLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PathLangParser import PathLangParser
else:
    from PathLangParser import PathLangParser

# This class defines a complete listener for a parse tree produced by PathLangParser.
class PathLangParserListener(ParseTreeListener):

    # Enter a parse tree produced by PathLangParser#programa.
    def enterPrograma(self, ctx:PathLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by PathLangParser#programa.
    def exitPrograma(self, ctx:PathLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by PathLangParser#sentencias.
    def enterSentencias(self, ctx:PathLangParser.SentenciasContext):
        pass

    # Exit a parse tree produced by PathLangParser#sentencias.
    def exitSentencias(self, ctx:PathLangParser.SentenciasContext):
        pass


    # Enter a parse tree produced by PathLangParser#sentencia.
    def enterSentencia(self, ctx:PathLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by PathLangParser#sentencia.
    def exitSentencia(self, ctx:PathLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by PathLangParser#declGrafo.
    def enterDeclGrafo(self, ctx:PathLangParser.DeclGrafoContext):
        pass

    # Exit a parse tree produced by PathLangParser#declGrafo.
    def exitDeclGrafo(self, ctx:PathLangParser.DeclGrafoContext):
        pass


    # Enter a parse tree produced by PathLangParser#dirigidoOpt.
    def enterDirigidoOpt(self, ctx:PathLangParser.DirigidoOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#dirigidoOpt.
    def exitDirigidoOpt(self, ctx:PathLangParser.DirigidoOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#elementos.
    def enterElementos(self, ctx:PathLangParser.ElementosContext):
        pass

    # Exit a parse tree produced by PathLangParser#elementos.
    def exitElementos(self, ctx:PathLangParser.ElementosContext):
        pass


    # Enter a parse tree produced by PathLangParser#elemento.
    def enterElemento(self, ctx:PathLangParser.ElementoContext):
        pass

    # Exit a parse tree produced by PathLangParser#elemento.
    def exitElemento(self, ctx:PathLangParser.ElementoContext):
        pass


    # Enter a parse tree produced by PathLangParser#declNodo.
    def enterDeclNodo(self, ctx:PathLangParser.DeclNodoContext):
        pass

    # Exit a parse tree produced by PathLangParser#declNodo.
    def exitDeclNodo(self, ctx:PathLangParser.DeclNodoContext):
        pass


    # Enter a parse tree produced by PathLangParser#coord.
    def enterCoord(self, ctx:PathLangParser.CoordContext):
        pass

    # Exit a parse tree produced by PathLangParser#coord.
    def exitCoord(self, ctx:PathLangParser.CoordContext):
        pass


    # Enter a parse tree produced by PathLangParser#declArista.
    def enterDeclArista(self, ctx:PathLangParser.DeclAristaContext):
        pass

    # Exit a parse tree produced by PathLangParser#declArista.
    def exitDeclArista(self, ctx:PathLangParser.DeclAristaContext):
        pass


    # Enter a parse tree produced by PathLangParser#peso.
    def enterPeso(self, ctx:PathLangParser.PesoContext):
        pass

    # Exit a parse tree produced by PathLangParser#peso.
    def exitPeso(self, ctx:PathLangParser.PesoContext):
        pass


    # Enter a parse tree produced by PathLangParser#tipoOpt.
    def enterTipoOpt(self, ctx:PathLangParser.TipoOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#tipoOpt.
    def exitTipoOpt(self, ctx:PathLangParser.TipoOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#declHeuristica.
    def enterDeclHeuristica(self, ctx:PathLangParser.DeclHeuristicaContext):
        pass

    # Exit a parse tree produced by PathLangParser#declHeuristica.
    def exitDeclHeuristica(self, ctx:PathLangParser.DeclHeuristicaContext):
        pass


    # Enter a parse tree produced by PathLangParser#declRegla.
    def enterDeclRegla(self, ctx:PathLangParser.DeclReglaContext):
        pass

    # Exit a parse tree produced by PathLangParser#declRegla.
    def exitDeclRegla(self, ctx:PathLangParser.DeclReglaContext):
        pass


    # Enter a parse tree produced by PathLangParser#bloque.
    def enterBloque(self, ctx:PathLangParser.BloqueContext):
        pass

    # Exit a parse tree produced by PathLangParser#bloque.
    def exitBloque(self, ctx:PathLangParser.BloqueContext):
        pass


    # Enter a parse tree produced by PathLangParser#instrucciones.
    def enterInstrucciones(self, ctx:PathLangParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by PathLangParser#instrucciones.
    def exitInstrucciones(self, ctx:PathLangParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by PathLangParser#instruccion.
    def enterInstruccion(self, ctx:PathLangParser.InstruccionContext):
        pass

    # Exit a parse tree produced by PathLangParser#instruccion.
    def exitInstruccion(self, ctx:PathLangParser.InstruccionContext):
        pass


    # Enter a parse tree produced by PathLangParser#asignacion.
    def enterAsignacion(self, ctx:PathLangParser.AsignacionContext):
        pass

    # Exit a parse tree produced by PathLangParser#asignacion.
    def exitAsignacion(self, ctx:PathLangParser.AsignacionContext):
        pass


    # Enter a parse tree produced by PathLangParser#expr.
    def enterExpr(self, ctx:PathLangParser.ExprContext):
        pass

    # Exit a parse tree produced by PathLangParser#expr.
    def exitExpr(self, ctx:PathLangParser.ExprContext):
        pass


    # Enter a parse tree produced by PathLangParser#suma.
    def enterSuma(self, ctx:PathLangParser.SumaContext):
        pass

    # Exit a parse tree produced by PathLangParser#suma.
    def exitSuma(self, ctx:PathLangParser.SumaContext):
        pass


    # Enter a parse tree produced by PathLangParser#termino.
    def enterTermino(self, ctx:PathLangParser.TerminoContext):
        pass

    # Exit a parse tree produced by PathLangParser#termino.
    def exitTermino(self, ctx:PathLangParser.TerminoContext):
        pass


    # Enter a parse tree produced by PathLangParser#factor.
    def enterFactor(self, ctx:PathLangParser.FactorContext):
        pass

    # Exit a parse tree produced by PathLangParser#factor.
    def exitFactor(self, ctx:PathLangParser.FactorContext):
        pass


    # Enter a parse tree produced by PathLangParser#llamada.
    def enterLlamada(self, ctx:PathLangParser.LlamadaContext):
        pass

    # Exit a parse tree produced by PathLangParser#llamada.
    def exitLlamada(self, ctx:PathLangParser.LlamadaContext):
        pass


    # Enter a parse tree produced by PathLangParser#argumentos.
    def enterArgumentos(self, ctx:PathLangParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by PathLangParser#argumentos.
    def exitArgumentos(self, ctx:PathLangParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by PathLangParser#masArgumentos.
    def enterMasArgumentos(self, ctx:PathLangParser.MasArgumentosContext):
        pass

    # Exit a parse tree produced by PathLangParser#masArgumentos.
    def exitMasArgumentos(self, ctx:PathLangParser.MasArgumentosContext):
        pass


    # Enter a parse tree produced by PathLangParser#acceso.
    def enterAcceso(self, ctx:PathLangParser.AccesoContext):
        pass

    # Exit a parse tree produced by PathLangParser#acceso.
    def exitAcceso(self, ctx:PathLangParser.AccesoContext):
        pass


    # Enter a parse tree produced by PathLangParser#atributoOpt.
    def enterAtributoOpt(self, ctx:PathLangParser.AtributoOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#atributoOpt.
    def exitAtributoOpt(self, ctx:PathLangParser.AtributoOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#atributo.
    def enterAtributo(self, ctx:PathLangParser.AtributoContext):
        pass

    # Exit a parse tree produced by PathLangParser#atributo.
    def exitAtributo(self, ctx:PathLangParser.AtributoContext):
        pass


    # Enter a parse tree produced by PathLangParser#siInstr.
    def enterSiInstr(self, ctx:PathLangParser.SiInstrContext):
        pass

    # Exit a parse tree produced by PathLangParser#siInstr.
    def exitSiInstr(self, ctx:PathLangParser.SiInstrContext):
        pass


    # Enter a parse tree produced by PathLangParser#sinoOpt.
    def enterSinoOpt(self, ctx:PathLangParser.SinoOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#sinoOpt.
    def exitSinoOpt(self, ctx:PathLangParser.SinoOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#condicion.
    def enterCondicion(self, ctx:PathLangParser.CondicionContext):
        pass

    # Exit a parse tree produced by PathLangParser#condicion.
    def exitCondicion(self, ctx:PathLangParser.CondicionContext):
        pass


    # Enter a parse tree produced by PathLangParser#paraInstr.
    def enterParaInstr(self, ctx:PathLangParser.ParaInstrContext):
        pass

    # Exit a parse tree produced by PathLangParser#paraInstr.
    def exitParaInstr(self, ctx:PathLangParser.ParaInstrContext):
        pass


    # Enter a parse tree produced by PathLangParser#tipoElemento.
    def enterTipoElemento(self, ctx:PathLangParser.TipoElementoContext):
        pass

    # Exit a parse tree produced by PathLangParser#tipoElemento.
    def exitTipoElemento(self, ctx:PathLangParser.TipoElementoContext):
        pass


    # Enter a parse tree produced by PathLangParser#busqueda.
    def enterBusqueda(self, ctx:PathLangParser.BusquedaContext):
        pass

    # Exit a parse tree produced by PathLangParser#busqueda.
    def exitBusqueda(self, ctx:PathLangParser.BusquedaContext):
        pass


    # Enter a parse tree produced by PathLangParser#conOpt.
    def enterConOpt(self, ctx:PathLangParser.ConOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#conOpt.
    def exitConOpt(self, ctx:PathLangParser.ConOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#horaOpt.
    def enterHoraOpt(self, ctx:PathLangParser.HoraOptContext):
        pass

    # Exit a parse tree produced by PathLangParser#horaOpt.
    def exitHoraOpt(self, ctx:PathLangParser.HoraOptContext):
        pass


    # Enter a parse tree produced by PathLangParser#mostrar.
    def enterMostrar(self, ctx:PathLangParser.MostrarContext):
        pass

    # Exit a parse tree produced by PathLangParser#mostrar.
    def exitMostrar(self, ctx:PathLangParser.MostrarContext):
        pass



del PathLangParser