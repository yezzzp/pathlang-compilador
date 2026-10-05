# Generated from PathLangParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PathLangParser import PathLangParser
else:
    from PathLangParser import PathLangParser

# This class defines a complete generic visitor for a parse tree produced by PathLangParser.

class PathLangParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PathLangParser#programa.
    def visitPrograma(self, ctx:PathLangParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#sentencias.
    def visitSentencias(self, ctx:PathLangParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#sentencia.
    def visitSentencia(self, ctx:PathLangParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#declGrafo.
    def visitDeclGrafo(self, ctx:PathLangParser.DeclGrafoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#dirigidoOpt.
    def visitDirigidoOpt(self, ctx:PathLangParser.DirigidoOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#elementos.
    def visitElementos(self, ctx:PathLangParser.ElementosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#elemento.
    def visitElemento(self, ctx:PathLangParser.ElementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#declNodo.
    def visitDeclNodo(self, ctx:PathLangParser.DeclNodoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#coord.
    def visitCoord(self, ctx:PathLangParser.CoordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#declArista.
    def visitDeclArista(self, ctx:PathLangParser.DeclAristaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#peso.
    def visitPeso(self, ctx:PathLangParser.PesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#tipoOpt.
    def visitTipoOpt(self, ctx:PathLangParser.TipoOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#declHeuristica.
    def visitDeclHeuristica(self, ctx:PathLangParser.DeclHeuristicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#declRegla.
    def visitDeclRegla(self, ctx:PathLangParser.DeclReglaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#bloque.
    def visitBloque(self, ctx:PathLangParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#instrucciones.
    def visitInstrucciones(self, ctx:PathLangParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#instruccion.
    def visitInstruccion(self, ctx:PathLangParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#asignacion.
    def visitAsignacion(self, ctx:PathLangParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#expr.
    def visitExpr(self, ctx:PathLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#suma.
    def visitSuma(self, ctx:PathLangParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#termino.
    def visitTermino(self, ctx:PathLangParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#factor.
    def visitFactor(self, ctx:PathLangParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#llamada.
    def visitLlamada(self, ctx:PathLangParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#argumentos.
    def visitArgumentos(self, ctx:PathLangParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#masArgumentos.
    def visitMasArgumentos(self, ctx:PathLangParser.MasArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#acceso.
    def visitAcceso(self, ctx:PathLangParser.AccesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#atributoOpt.
    def visitAtributoOpt(self, ctx:PathLangParser.AtributoOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#atributo.
    def visitAtributo(self, ctx:PathLangParser.AtributoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#siInstr.
    def visitSiInstr(self, ctx:PathLangParser.SiInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#sinoOpt.
    def visitSinoOpt(self, ctx:PathLangParser.SinoOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#condicion.
    def visitCondicion(self, ctx:PathLangParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#paraInstr.
    def visitParaInstr(self, ctx:PathLangParser.ParaInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#tipoElemento.
    def visitTipoElemento(self, ctx:PathLangParser.TipoElementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#busqueda.
    def visitBusqueda(self, ctx:PathLangParser.BusquedaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#conOpt.
    def visitConOpt(self, ctx:PathLangParser.ConOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#horaOpt.
    def visitHoraOpt(self, ctx:PathLangParser.HoraOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PathLangParser#mostrar.
    def visitMostrar(self, ctx:PathLangParser.MostrarContext):
        return self.visitChildren(ctx)



del PathLangParser