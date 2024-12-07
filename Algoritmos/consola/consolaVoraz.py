import time

costos = {
    'avanzar': 1,
    'borrar': 2,
    'reemplazar': 3,
    'insertar': 2,
    'kill': 4
}

def consolaVoraz(cadena_x, cadena_y, costos):
    i, j = 0, 0
    secuencia = []
    costo_total = 0

    advance_cost = costos['avanzar']
    delete_cost = costos['borrar']
    insert_cost = costos['insertar']
    replace_cost = costos['reemplazar']
    kill_cost = costos['kill']

    m = len(cadena_x)
    n = len(cadena_y)

    while i < m and j < n:
        if cadena_x[i] == cadena_y[j]:
   
            costo_total += advance_cost
            secuencia.append(f"avanzar: '{cadena_x[i]}' == '{cadena_y[j]}'")
            i += 1
            j += 1
        else:

            if replace_cost <= delete_cost + insert_cost:
                costo_total += replace_cost
                secuencia.append(f"reemplazar: '{cadena_x[i]}' -> '{cadena_y[j]}'") 
                i += 1
                j += 1
            elif delete_cost < insert_cost:
                costo_total += delete_cost
                secuencia.append(f"borrar: '{cadena_x[i]}'")  
                i += 1
            else:
                costo_total += insert_cost
                secuencia.append(f"insertar: '{cadena_y[j]}' antes de '{cadena_x[i]}'")
                j += 1

    if i < m:
        if kill_cost < delete_cost * (m - i):
            costo_total += kill_cost
            secuencia.append("kill (eliminar el resto de la cadena)")
        else:
            while i < m:
                costo_total += delete_cost
                secuencia.append(f"borrar: '{cadena_x[i]}'")  
                i += 1

    while j < n:
        costo_total += insert_cost
        secuencia.append(f"insertar: '{cadena_y[j]}' al final")  
        j += 1

    return costo_total, secuencia

def benchmark():
    test_cases = [
        ('algorithm', 'altruistic'),
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
        
        print(f"\nTransformando: {cadena_x} -> {cadena_y}")
        
        start_time = time.perf_counter()
        costo_total, secuencia = consolaVoraz(cadena_x, cadena_y, costos)
        end_time = time.perf_counter()
        
        tiempo_ejecucion = (end_time - start_time) * 1e3  
        
      
        print(f"Costo total: {costo_total}")
        print("Operaciones realizadas:")
        for paso in secuencia:
            print(f"  - {paso}")
        print(f"Tiempo de Ejecución: {tiempo_ejecucion:.3f} ms")


benchmark()
