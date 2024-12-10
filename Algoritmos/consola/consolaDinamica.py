import numpy as np
import time

costos = {
    'avanzar': 1,
    'borrar': 2,
    'reemplazar': 3,
    'insertar': 2,
    'kill': 4
}

def consolaInteligente(cadena_x, cadena_y, costos):
    m_cadena_x = len(cadena_x) + 1
    n_cadena_y = len(cadena_y) + 1

    matriz = np.zeros((m_cadena_x, n_cadena_y))
    operaciones = [["" for _ in range(n_cadena_y)] for _ in range(m_cadena_x)]

    for i in range(1, m_cadena_x):
        matriz[i][0] = costos['kill']
        operaciones[i][0] = f"kill '{cadena_x[:i]}'"
    for j in range(1, n_cadena_y):
        matriz[0][j] = j * costos['insertar']
        operaciones[0][j] = f"insertar '{cadena_y[j-1]}'"

    for i in range(1, m_cadena_x):
        for j in range(1, n_cadena_y):
            if cadena_x[i - 1] == cadena_y[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + costos['avanzar']
                operaciones[i][j] = f"avanzar '{cadena_x[i-1]}'"
            else:
                insert = matriz[i][j - 1] + costos['insertar']
                reemplazar = matriz[i - 1][j - 1] + costos['reemplazar']
                borrar = matriz[i - 1][j] + costos['borrar']

                if insert <= reemplazar and insert <= borrar:
                    matriz[i][j] = insert
                    operaciones[i][j] = f"insertar '{cadena_y[j-1]}'"
                elif reemplazar <= borrar:
                    matriz[i][j] = reemplazar
                    operaciones[i][j] = f"reemplazar '{cadena_x[i-1]}' con '{cadena_y[j-1]}'"
                else:
                    matriz[i][j] = borrar
                    operaciones[i][j] = f"borrar '{cadena_x[i-1]}'"


    pasos = []
    i, j = m_cadena_x - 1, n_cadena_y - 1
    while i > 0 or j > 0:
        
        if i > 0 and j > 0 and operaciones[i][j].startswith("avanzar"):
            pasos.append(operaciones[i][j])
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and operaciones[i][j].startswith("reemplazar"):
            pasos.append(operaciones[i][j])
            i -= 1
            j -= 1
        elif i > 0 and operaciones[i][j].startswith("borrar"):
            pasos.append(operaciones[i][j])
            i -= 1
        elif j > 0 and operaciones[i][j].startswith("insertar"):
            pasos.append(operaciones[i][j])
            j -= 1
        elif i > 0 and operaciones[i][j].startswith("kill"):
            pasos.append(operaciones[i][j])
            i = 0
            j = 0
        else:
            break
    pasos.reverse()
  
    return matriz[-1, -1], pasos

    


def benchmark_dinamica():
    test_cases = [
        ('pancho', 'pinocho'),
        ('hello', 'halo'),
        ('kitten', 'sitting'),
        ('abcdef', 'azced'),
        ('', 'example'),
        ('longtextstring', 'short'),
        ('abcde', 'abcde'), 
        ('abcdefghi', 'abcde'),
    ]

    for case in test_cases:
        cadena_x, cadena_y = case

        num_repeticiones = 1
        for _ in range(num_repeticiones):
            start_time = time.perf_counter() 
            costo_minimo, operaciones = consolaInteligente(cadena_x, cadena_y, costos)
            end_time = time.perf_counter()
            tiempo_ejecucion = (end_time - start_time) * 1e3 
            
            print(f"Entrada: {cadena_x} -> {cadena_y}")
            print(f"Costo mínimo: {costo_minimo}")
            print(f"Número de operaciones: {len(operaciones)}")
            print("Procedimiento:")
            for paso in operaciones:
                print(f"  - {paso}")
            print(f"Tiempo de Ejecución: {tiempo_ejecucion:.3f} ms\n")

benchmark_dinamica()
