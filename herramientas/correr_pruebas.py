"""Ejecuta y verifica los casos de pruebas/; sale distinto de cero si alguno falla."""
import contextlib
import io
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from main import analizar

RAIZ = pathlib.Path(__file__).resolve().parent.parent / 'pruebas'
CASOS = (
    ('validos', 'Programa válido: léxico, sintáctico y semántico OK.'),
    ('lexico', '[Error Léxico,'),
    ('sintactico', '[Error Sintáctico,'),
    ('semantico', '[Error Semántico,'),
)

fallas = []
conteo = 0
correctas = 0
for carpeta, esperado in CASOS:
    archivos = sorted((RAIZ / carpeta).glob('*.path'))
    if not archivos:
        fallas.append(f'{carpeta}: no hay archivos .path')
        continue
    print(f'\n========== {carpeta.upper()} ({len(archivos)}) ==========')
    for archivo in archivos:
        conteo += 1
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida):
            analizar(str(archivo))
        texto = salida.getvalue()
        ok = esperado in texto
        if ok:
            correctas += 1
        print(f'{"OK" if ok else "FALLO"} {archivo.name}')
        if not ok:
            resumen = texto.strip().replace('\n', ' | ') or '<sin salida>'
            fallas.append(f'{archivo.relative_to(RAIZ)}: se esperaba {esperado!r}; salida: {resumen}')

if conteo != 27:
    fallas.append(f'se esperaban 27 casos en total; se encontraron {conteo}')

print(f'\nResultado: {correctas}/{conteo} comprobaciones correctas.')
if fallas:
    print('Fallos:')
    for falla in fallas:
        print(f' - {falla}')
    sys.exit(1)
