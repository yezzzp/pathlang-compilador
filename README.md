# PathLang · Compilador (Trabajo Parcial)

Lenguaje para declarar redes espaciales (grafos, nodos, aristas ponderadas), heurísticas y reglas de
costo por hora, y pedir la mejor ruta con A*. Esta etapa implementa los analizadores **léxico**,
**sintáctico** y **semántico** con ANTLR 4.13.1 y Python 3.

## Requisitos

- Java 11+ y `antlr-4.13.1-complete.jar` (para regenerar `gen/`)
- `pip install antlr4-python3-runtime==4.13.1`

## Uso

```bash
make                                                   # genera gen/
python3 main.py pruebas/validos/01_completo.path        # análisis completo
python3 main.py tokens pruebas/validos/01_completo.path # solo análisis léxico
python3 main.py arbol  pruebas/validos/01_completo.path # árbol sintáctico
python3 herramientas/correr_pruebas.py                  # las 27 pruebas
python3 herramientas/derivaciones.py declArista "arista A -> B : 4 min;"   # derivación más a la izquierda
```

## Estructura

| Ruta | Qué es |
|---|---|
| `PathLangLexer.g4` | analizador léxico (expresiones regulares) |
| `PathLangParser.g4` | analizador sintáctico (gramáticas en la notación del informe) |
| `semantico/tabla.py` | tabla de símbolos con pila de ámbitos |
| `semantico/visitor.py` | analizador semántico (11 errores, E1 a E11) |
| `errores.py` | mensajes de error léxicos y sintácticos en español |
| `main.py` | driver |
| `pruebas/` | `validos/` (4), `lexico/` (5), `sintactico/` (7), `semantico/` (11) |
| `herramientas/` | ejecución de pruebas, derivaciones y ejemplos del informe |
