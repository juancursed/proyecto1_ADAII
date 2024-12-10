import numpy as np


def subastaDinamica(A, B, ofertantes):
    n = len(ofertantes)
    matriz_costo = np.zeros((A + 1, n + 1), dtype=np.int64)
    rastreo = np.zeros((A + 1, n + 1), dtype=np.int64)  # Rastreo para reconstruir asignaciones

    # Inicializar la matriz
    for i in range(0, A + 1):
        for j in range(0, n + 1):
            if i == 0:
                matriz_costo[i, j] = 0
            elif j == 0:
                matriz_costo[i, j] = i * B
            else:
                precio, minimo, maximo = ofertantes[j - 1]
                opciones = [(matriz_costo[i, j - 1], 0)]  # Opción: no comprar acciones

                # Comprar el mínimo de acciones si es posible
                if i >= minimo:
                    opciones.append(
                        (matriz_costo[i - minimo, j - 1] + precio * minimo, minimo)
                    )
                
                # Comprar el máximo de acciones si es posible
                if i >= maximo:
                    opciones.append(
                        (matriz_costo[i - maximo, j - 1] + precio * maximo, maximo)
                    )

                # Elegir la mejor opción
                matriz_costo[i, j], rastreo[i, j] = max(opciones, key=lambda x: x[0])

    # Reconstrucción de asignaciones óptimas
    asignaciones = [0] * n
    acciones_restantes = A
    for j in range(n, 0, -1):
        asignaciones[j - 1] = rastreo[acciones_restantes, j]
        acciones_restantes -= asignaciones[j - 1]

    # Agregar las acciones restantes asignadas al gobierno
    asignaciones.append(acciones_restantes)

    return matriz_costo, asignaciones
