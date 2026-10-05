# Genera la derivación más a la izquierda de un fragmento, a partir del árbol de ANTLR.
# Uso:  python3 herramientas/derivaciones.py <regla> "<texto>"
#   ej: python3 herramientas/derivaciones.py declArista "arista A -> B : 4 min;"
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from antlr4 import CommonTokenStream, InputStream, ParserRuleContext
from antlr4.tree.Tree import TerminalNode
from gen.PathLangLexer import PathLangLexer
from gen.PathLangParser import PathLangParser

ESPECIALES = {'ID': 'id', 'NUM': 'num', 'HORA': 'tiempo', 'UNIDAD': 'unidad',
              'FLECHA': 'flecha', 'OPREL': 'oprel', 'A_LAS': 'a las'}

def simbolo(token_type):
    nombre = PathLangParser.symbolicNames[token_type]       # los nombres del parser están alineados con el tipo
    if nombre in ESPECIALES:
        return ESPECIALES[nombre]
    literal = PathLangParser.literalNames[token_type]
    return literal.strip("'") if literal != '<INVALID>' else nombre.lower()

def nombre_regla(ctx):
    return PathLangParser.ruleNames[ctx.getRuleIndex()]

def hijos(ctx):
    out = []
    for h in (ctx.children or []):
        if isinstance(h, TerminalNode):
            if h.symbol.type != -1:                       # se omite EOF
                out.append(simbolo(h.symbol.type))
        else:
            out.append(h)
    return out

def texto(forma):
    return ' '.join(x if isinstance(x, str) else nombre_regla(x) for x in forma) or 'ε'

# Cada fragmento se analiza dentro de su contexto real, para que el parser vea qué viene después.
CONTEXTO = {'siInstr': 'regla R_ {{ {} }}', 'paraInstr': 'regla R_ {{ {} }}',
            'asignacion': 'regla R_ {{ {} }}',
            'declNodo': 'grafo G_ {{ {} }}', 'declArista': 'grafo G_ {{ {} }}'}

def buscar_subarbol(ctx, regla):
    if isinstance(ctx, ParserRuleContext):
        if nombre_regla(ctx) == regla:
            return ctx
        for h in (ctx.children or []):
            r = buscar_subarbol(h, regla)
            if r is not None:
                return r
    return None

def derivar(regla, fuente):
    programa = CONTEXTO.get(regla, '{}').format(fuente)
    parser = PathLangParser(CommonTokenStream(PathLangLexer(InputStream(programa))))
    raiz = parser.programa()
    if parser.getNumberOfSyntaxErrors():
        raise SystemExit(f'No es válido: {fuente}')
    arbol = buscar_subarbol(raiz, regla)
    if arbol is None or arbol.getText().replace(' ', '') != fuente.replace(' ', ''):
        raise SystemExit(f'El texto no corresponde a la regla {regla}: {fuente}')
    forma, pasos = [arbol], []
    while True:
        i = next((k for k, x in enumerate(forma) if isinstance(x, ParserRuleContext)), None)
        if i is None:
            return [texto([arbol])] + pasos
        nodo = forma[i]
        forma = forma[:i] + hijos(nodo) + forma[i + 1:]
        pasos.append(texto(forma))

if __name__ == '__main__':
    pasos = derivar(sys.argv[1], sys.argv[2])
    print(pasos[0])
    for p in pasos[1:]:
        print('  ⇒lm', p)
