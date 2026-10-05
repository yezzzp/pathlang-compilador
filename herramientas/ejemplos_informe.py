# Ejemplos del informe: 5 por construcción (verificados con el parser)
# y las 4 derivaciones más a la izquierda de cada gramática.
# Uso: python3 herramientas/ejemplos_informe.py  [--json]
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from herramientas.derivaciones import derivar

CONSTRUCCIONES = [
  ('C1', 'Declaración del grafo, nodos y aristas', [
    ('declGrafo',  'grafo Vacio { }', True),
    ('declNodo',   'nodo A (-12.046, -77.042);', True),
    ('declArista', 'arista A -> B : 4 min;', True),
    ('declArista', 'arista A <-> C : 2.5 km tipo avenida;', True),
    ('declGrafo',  'grafo Lima dirigido { nodo A (-12.046, -77.042); nodo B (-12.050, -77.030); arista A -> B : 4 min; }', False),
  ]),
  ('C2', 'Funciones heurísticas', [
    ('declHeuristica', 'heuristica Cero(n, meta) { retornar 0; }', True),
    ('declHeuristica', 'heuristica Latitud(n, meta) { retornar meta.lat - n.lat; }', True),
    ('declHeuristica', 'heuristica Escalada(n, meta) { retornar n.lat * 2; }', True),
    ('declHeuristica', 'heuristica Escala(n, meta) { retornar n.lon / 10; }', True),
    ('declHeuristica', 'heuristica Recta(n, meta) { retornar distancia(n, meta) / 40.0; }', False),
  ]),
  ('C3', 'Asignación y expresiones aritméticas', [
    ('asignacion', 'e.peso := 0;', True),
    ('asignacion', 'e.peso := e.peso * 2.0;', True),
    ('asignacion', 'e.peso := e.peso + 1;', True),
    ('asignacion', 'e.peso := e.peso / 2;', True),
    ('asignacion', 'e.peso := (e.peso + 1) * 1.5 - recargo(e) / 2;', False),
  ]),
  ('C4', 'Selectiva con costo dinámico temporal', [
    ('siInstr', 'si hora entre 17:00 y 20:00 entonces { }', True),
    ('siInstr', 'si hora entre 22:00 y 23:59 entonces { } sino { }', True),
    ('siInstr', 'si e.tipo == avenida entonces { }', True),
    ('siInstr', 'si e.peso > 10 entonces { }', True),
    ('declRegla', 'regla HoraPunta { si hora entre 17:00 y 20:00 entonces { e.peso := e.peso * 2.0; } sino { e.peso := e.peso * 0.8; } }', False),
  ]),
  ('C5', 'Iterativa de exploración del grafo', [
    ('paraInstr', 'para cada arista e de Lima { }', True),
    ('paraInstr', 'para cada nodo n de Lima { }', True),
    ('paraInstr', 'para cada arista e de Lima { e.peso := 0; }', True),
    ('paraInstr', 'para cada nodo n de Lima { para cada arista e de Lima { } }', True),
    ('paraInstr', 'para cada arista e de Lima { si e.tipo == avenida entonces { e.peso := e.peso * 2.0; } }', False),
  ]),
  ('C6', 'Búsqueda de ruta y salida', [
    ('busqueda', 'buscar ruta r desde A hasta D en Lima usando Recta;', True),
    ('busqueda', 'buscar ruta r desde A hasta D en Lima usando Recta con HoraPunta;', True),
    ('busqueda', 'buscar ruta r desde A hasta D en Lima usando Recta a las 18:30;', True),
    ('mostrar',  'mostrar r;', True),
    ('busqueda', 'buscar ruta r desde A hasta D en Lima usando Recta con HoraPunta a las 18:30;', False),
  ]),
]

datos = []
for clave, titulo, ejemplos in CONSTRUCCIONES:
    items = []
    for regla, texto, derivar_si in ejemplos:
        pasos = derivar(regla, texto)        # falla si el ejemplo no es válido
        items.append({'regla': regla, 'texto': texto, 'derivacion': pasos if derivar_si else None})
    assert sum(1 for i in items if i['derivacion']) == 4, clave
    datos.append({'clave': clave, 'titulo': titulo, 'ejemplos': items})

if __name__ == '__main__' and '--json' in sys.argv:
    print(json.dumps(datos, ensure_ascii=False, indent=1))
elif __name__ == '__main__':
    for c in datos:
        print(f"\n## {c['clave']} · {c['titulo']}")
        for e in c['ejemplos']:
            print(' -', e['texto'])
            if e['derivacion']:
                print('     ', ' ⇒ '.join(e['derivacion']))
