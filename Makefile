# Genera el lexer, el parser y el visitor de Python en gen/ (ANTLR 4.13.1, igual que los ejemplos de clase)
ANTLR = java -jar /usr/local/lib/antlr-4.13.1-complete.jar

all:
	$(ANTLR) -Dlanguage=Python3 -visitor PathLangLexer.g4 PathLangParser.g4 -o gen -Xexact-output-dir
	touch gen/__init__.py

pruebas: all
	python3 herramientas/correr_pruebas.py

clean:
	rm -rf gen/
