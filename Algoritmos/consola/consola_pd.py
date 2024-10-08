import numpy as np


costos = {
    'avanzar' : 10,
    'borrar' : 0,
    'reemplazar': 10,
    'insertar' :3,
    'kill' : 2
}


cadena_x = 'pala'

cadena_y = 'tapa'



def consolaInteligente(cadena_x, cadena_y, costos):

    m_cadena_x = len(cadena_x)+ 1
    n_cadena_y = len(cadena_y) +1

    matriz = np.zeros((m_cadena_x, n_cadena_y))

    #----------Estados bases ----------
    for i in range(1, m_cadena_x):
        matriz[i][0] = costos['kill']
    for j in range(1, n_cadena_y):
        matriz[0][j] = j * costos['insertar']

    #----------LLenar Matriz----------

    for i in range(1, m_cadena_x):
        for j in range(1, n_cadena_y):

            if cadena_x[i - m_cadena_x ] == cadena_y[j-n_cadena_y]:
                
                matriz[i][j] = matriz[i-1][j-1] + costos['avanzar']
            else:
                insert = matriz[i][j-1] + costos['insertar']
                reemplazar = matriz[i-1][j-1] + costos['reemplazar']
                borrar = matriz[i-1][j] + costos['borrar']

                matriz[i][j] = min(insert, reemplazar, borrar)

    print(matriz)

    

consolaInteligente(cadena_x, cadena_y, costos)