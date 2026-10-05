# Tabla de símbolos con pila de ámbitos (mismo diseño que MiniLang).
class Simbolo:
    def __init__(self, nombre, categoria, linea, **extra):
        self.nombre = nombre
        self.categoria = categoria   # 'grafo' | 'nodo' | 'heuristica' | 'regla' | 'ruta' | 'variable'
        self.linea = linea
        self.extra = extra           # ej. nodo -> grafo al que pertenece

class TablaSimbolos:
    def __init__(self):
        self.ambitos = [('global', {})]          # pila: (nombre, {id: Simbolo})

    def entrar(self, nombre):
        self.ambitos.append((nombre, {}))

    def salir(self):
        self.ambitos.pop()

    def declarar(self, simbolo):
        """Devuelve el símbolo previo si ya existía en el ámbito ACTUAL."""
        _, tabla = self.ambitos[-1]
        previo = tabla.get(simbolo.nombre)
        if previo is None:
            tabla[simbolo.nombre] = simbolo
        return previo

    def buscar(self, nombre):
        for _, tabla in reversed(self.ambitos):  # del ámbito más interno al global
            if nombre in tabla:
                return tabla[nombre]
        return None
