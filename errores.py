# Reporte de errores léxicos y sintácticos en español, con línea y columna.
from antlr4.error.ErrorListener import ErrorListener

class ColectorErrores(ErrorListener):
    def __init__(self, fase):
        self.fase = fase            # 'Léxico' o 'Sintáctico'
        self.errores = []

    def syntaxError(self, recognizer, simbolo, linea, columna, mensaje, e):
        self.errores.append(f'[Error {self.fase}, línea {linea}:{columna}] {mensaje}')
