import time

costos = {
    'avanzar': 1,
    'borrar': 2,
    'reemplazar': 3,
    'insertar': 2,
    'kill': 4
}

def consolaFuerzaBruta(cadena_x, cadena_y, costos):
    def calcularCosto(i, j, ruta_actual):
        if i == 0:  
            for k in range(j):
                ruta_actual.append(f"insertar '{cadena_y[k]}'")
            return j * costos['insertar']
        if j == 0:
            if i > 1:
                ruta_actual.append("kill")
                return costos['kill']
            for k in range(i):
                ruta_actual.append(f"borrar '{cadena_x[k]}'")
            return i * costos['borrar']
        
        
        if cadena_x[i - 1] == cadena_y[j - 1]:
            costo = calcularCosto(i - 1, j - 1, ruta_actual)
            ruta_actual.append(f"avanzar: '{cadena_x[i-1]}' == '{cadena_y[j-1]}'")
            return costo + costos['avanzar']

        ruta_reemplazar = ruta_actual[:]
        costo_reemplazar = calcularCosto(i - 1, j - 1, ruta_reemplazar) + costos['reemplazar']
        ruta_reemplazar.append(f"reemplazar '{cadena_x[i-1]}' con '{cadena_y[j-1]}'")

        ruta_insertar = ruta_actual[:]
        costo_insertar = calcularCosto(i, j - 1, ruta_insertar) + costos['insertar']
        ruta_insertar.append(f"insertar '{cadena_y[j-1]}'")

        ruta_borrar = ruta_actual[:]
        costo_borrar = calcularCosto(i - 1, j, ruta_borrar) + costos['borrar']
        ruta_borrar.append(f"borrar '{cadena_x[i-1]}'")

   
        if costo_reemplazar <= costo_insertar and costo_reemplazar <= costo_borrar:
            ruta_actual[:] = ruta_reemplazar
            return costo_reemplazar
        elif costo_insertar <= costo_borrar:
            ruta_actual[:] = ruta_insertar
            return costo_insertar
        else:
            ruta_actual[:] = ruta_borrar
            return costo_borrar

    operaciones = []
    costo_minimo = calcularCosto(len(cadena_x), len(cadena_y), operaciones)
    return costo_minimo, operaciones


def benchmark_fuerza_bruta():
    test_cases = [
        ('pancho', 'pinocho'),
        ('hello', 'halo'),
        ('kitten', 'sitting'),
        ('abcdef', 'azced'),
        ('', 'example'),
        ('longtextstring', 'short'),
        ('abcdehijk', 'abcde'),  # Problemita con kill
    ]
    
    for case in test_cases:
        cadena_x, cadena_y = case
        
        num_repeticiones = 1  
        for _ in range(num_repeticiones):
            start_time = time.perf_counter() 
            costo_minimo, operaciones = consolaFuerzaBruta(cadena_x, cadena_y, costos)
            end_time = time.perf_counter()
            tiempo_ejecucion = (end_time - start_time) * 1e9  
            
         
            print(f"Entrada: {cadena_x} -> {cadena_y}")
            print(f"Costo mínimo: {costo_minimo}")
            print("Procedimiento:")
            for paso in operaciones:
                print(f"  - {paso}")
            print(f"Tiempo de Ejecución: {tiempo_ejecucion:.3f} ns\n")


benchmark_fuerza_bruta()
