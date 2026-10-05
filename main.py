# Driver de PathLang (TB1): léxico + sintáctico + semántico.
# Uso:  python3 main.py [tokens|arbol|semantico] archivo.path
import sys
from antlr4 import CommonTokenStream, FileStream, Token
from gen.PathLangLexer import PathLangLexer
from gen.PathLangParser import PathLangParser
from errores import ColectorErrores
from semantico.visitor import AnalizadorSemantico

def analizar(archivo, modo='semantico'):
    lexer = PathLangLexer(FileStream(archivo, encoding='utf-8'))
    err_lex = ColectorErrores('Léxico')
    lexer.removeErrorListeners(); lexer.addErrorListener(err_lex)
    tokens = CommonTokenStream(lexer)

    if modo == 'tokens':                                   # ① solo análisis léxico
        tokens.fill()
        for t in tokens.tokens:
            if t.type != Token.EOF:
                print(f'{t.line}:{t.column:<3} {PathLangLexer.symbolicNames[t.type]:<11} {t.text!r}')
        for e in err_lex.errores: print(e)
        return

    parser = PathLangParser(tokens)                        # ② análisis sintáctico
    err_sin = ColectorErrores('Sintáctico')
    parser.removeErrorListeners(); parser.addErrorListener(err_sin)
    arbol = parser.programa()

    if err_lex.errores or err_sin.errores:
        for e in err_lex.errores + err_sin.errores: print(e)
        print('Compilación detenida: hay errores léxicos o sintácticos.')
        return
    if modo == 'arbol':
        print(arbol.toStringTree(recog=parser))
        return

    sem = AnalizadorSemantico()                            # ③ análisis semántico
    sem.visit(arbol)
    if sem.errores:
        for e in sem.errores: print(e)
    else:
        print('Programa válido: léxico, sintáctico y semántico OK.')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        analizar(sys.argv[1])
    else:
        analizar(sys.argv[2], sys.argv[1])
