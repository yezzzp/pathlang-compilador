# Analizador SEMÁNTICO: recorre el árbol y consulta la tabla de símbolos.
from gen.PathLangParserVisitor import PathLangParserVisitor
from .tabla import Simbolo, TablaSimbolos

ATRIBUTOS = {'arista': {'peso', 'tipo'}, 'nodo': {'lat', 'lon'}}
EDITABLES = {'arista': {'peso'}, 'nodo': set()}           # los nodos son inmutables
NOMBRE = {'grafo': 'el grafo', 'nodo': 'el nodo', 'heuristica': 'la heurística',
          'regla': 'la regla', 'ruta': 'la ruta', 'arista': 'la arista', 'variable': 'una variable'}

class AnalizadorSemantico(PathLangParserVisitor):
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.errores = []
        self.grafo_actual = None        # atributo heredado: grafo al que pertenecen los nodos

    # ---------- utilidades
    def error(self, ctx, msg):
        self.errores.append(f'[Error Semántico, línea {ctx.start.line}] {msg}')

    def declarar(self, ctx, nombre, categoria, **extra):
        previo = self.tabla.declarar(Simbolo(nombre, categoria, ctx.start.line, **extra))
        if previo:                                                     # E2: redeclaración
            self.error(ctx, f"'{nombre}' ya fue declarado en la línea {previo.linea}")

    def exigir(self, ctx, nombre, categoria):
        s = self.tabla.buscar(nombre)
        if s is None:                                                  # E1: no declarado
            self.error(ctx, f"No existe {NOMBRE[categoria]} '{nombre}'")
        elif s.categoria != categoria:                                 # E10: categoría equivocada
            self.error(ctx, f"'{nombre}' es {NOMBRE[s.categoria]}, se esperaba {NOMBRE[categoria]}")
            s = None
        return s

    # ---------- C1 · grafo, nodos y aristas
    def visitDeclGrafo(self, ctx):
        nombre = ctx.ID().getText()
        self.declarar(ctx, nombre, 'grafo')
        self.grafo_actual = nombre
        self.visit(ctx.elementos())
        self.grafo_actual = None

    def visitDeclNodo(self, ctx):
        self.declarar(ctx, ctx.ID().getText(), 'nodo', grafo=self.grafo_actual)

    def visitDeclArista(self, ctx):
        origen, destino = ctx.ID(0).getText(), ctx.ID(1).getText()
        for n in (origen, destino):
            s = self.exigir(ctx, n, 'nodo')
            if s and s.extra['grafo'] != self.grafo_actual:            # E5: pertenencia
                self.error(ctx, f"El nodo '{n}' no pertenece al grafo '{self.grafo_actual}'")
        if ctx.peso().MENOS():                                         # E3: peso negativo
            self.error(ctx, f"Peso negativo en arista {origen} -> {destino}: A* exige pesos >= 0")

    # ---------- C2 · heurísticas y C4/C5 · reglas
    def visitDeclHeuristica(self, ctx):
        self.declarar(ctx, ctx.ID(0).getText(), 'heuristica')
        self.tabla.entrar(f'heuristica {ctx.ID(0).getText()}')
        for p in (ctx.ID(1), ctx.ID(2)):                               # parámetros (n, meta)
            self.declarar(ctx, p.getText(), 'variable', de='nodo')
        self.visit(ctx.expr())
        self.tabla.salir()

    def visitDeclRegla(self, ctx):
        self.declarar(ctx, ctx.ID().getText(), 'regla')
        self.tabla.entrar(f'regla {ctx.ID().getText()}')
        self.visit(ctx.bloque())
        self.tabla.salir()

    def visitParaInstr(self, ctx):
        tipo = 'arista' if ctx.tipoElemento().ARISTA() else 'nodo'
        var, grafo = ctx.ID(0).getText(), ctx.ID(1).getText()
        self.exigir(ctx, grafo, 'grafo')
        self.tabla.entrar(f'para cada {var}')
        self.declarar(ctx, var, 'variable', de=tipo)
        self.visit(ctx.bloque())                                       # el cuerpo SIEMPRE se analiza
        self.tabla.salir()

    def visitCondicion(self, ctx):
        if ctx.HORA_KW() is None:
            return self.visit(ctx.expr())
        h1, h2 = (h.getText() for h in ctx.HORA())
        validas = True
        for h in (h1, h2):
            hh, mm = map(int, h.split(':'))
            if hh > 23 or mm > 59:                                     # E4: hora inválida
                self.error(ctx, f"Hora inválida '{h}'")
                validas = False
        if validas and h1 >= h2:
            self.error(ctx, f"Rango horario vacío: {h1} no es anterior a {h2}")

    # ---------- C3 · asignación y accesos
    def visitAsignacion(self, ctx):
        acc = ctx.acceso()
        if acc.atributoOpt().PUNTO() is None:
            self.error(ctx, f"No se puede asignar a '{acc.getText()}': solo se modifican atributos (e.peso)")
        else:
            var = self.tabla.buscar(acc.ID().getText())
            attr = acc.atributoOpt().atributo().getText()
            if var is not None and var.categoria == 'variable':
                tipo = var.extra['de']
                if attr in ATRIBUTOS[tipo] and attr not in EDITABLES[tipo]:   # E7: inmutable
                    self.error(ctx, f"'{acc.getText()}' es inmutable: {NOMBRE[tipo]} no se puede modificar")
        self.visitChildren(ctx)

    def visitAcceso(self, ctx):
        if ctx.atributoOpt().PUNTO() is None:
            return                          # 'avenida' en e.tipo == avenida es un valor, no una variable
        nombre = ctx.ID().getText()
        s = self.tabla.buscar(nombre)
        if s is None:
            self.error(ctx, f"Variable '{nombre}' no declarada")
        elif s.categoria == 'variable':
            attr = ctx.atributoOpt().atributo().getText()
            if attr not in ATRIBUTOS[s.extra['de']]:                   # E8: atributo inexistente
                self.error(ctx, f"{NOMBRE[s.extra['de']].capitalize()} '{nombre}' no tiene el atributo '{attr}'")

    # ---------- C6 · búsqueda y salida
    def visitBusqueda(self, ctx):
        ruta, origen, destino, grafo, heur = (ctx.ID(i).getText() for i in range(5))
        g = self.exigir(ctx, grafo, 'grafo')
        for n in (origen, destino):
            s = self.exigir(ctx, n, 'nodo')
            if s and g and s.extra['grafo'] != grafo:                  # E5: pertenencia
                self.error(ctx, f"El nodo '{n}' no pertenece al grafo '{grafo}'")
        self.exigir(ctx, heur, 'heuristica')                            # E6: heurística no declarada
        if ctx.conOpt().CON():
            self.exigir(ctx, ctx.conOpt().ID().getText(), 'regla')
        if ctx.horaOpt().A_LAS():
            hh, mm = map(int, ctx.horaOpt().HORA().getText().split(':'))
            if hh > 23 or mm > 59:
                self.error(ctx, f"Hora inválida '{ctx.horaOpt().HORA().getText()}'")
        self.declarar(ctx, ruta, 'ruta')

    def visitMostrar(self, ctx):
        self.exigir(ctx, ctx.ID().getText(), 'ruta')
