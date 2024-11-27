import numpy as np


costos = {
    'avanzar' : 1,
    'borrar' : 2,
    'reemplazar': 3,
    'insertar' :2,
    'kill' : 1
}
costos2 = {
    'avanzar' : 10,
    'borrar' : 0,
    'reemplazar': 10,
    'insertar' :3,
    'kill' : 2
}

cadena_x = 'pato'
cadena_y = 'ajo'



def consolaInteligente(cadena_x, cadena_y, costos):

    m_cadena_x = len(cadena_x) + 1
    n_cadena_y = len(cadena_y) + 1
    

    matriz = np.zeros((m_cadena_x , n_cadena_y ))

    #----------Estados bases ----------
    for i in range(1, m_cadena_x ):
        matriz[i][0] = costos['kill']
    for j in range(1, n_cadena_y ) :
        matriz[0][j] = j * costos['insertar']

    #----------LLenar Matriz----------

    for i in range(1, m_cadena_x ):
        for j in range(1, n_cadena_y):
            print(cadena_x[(m_cadena_x-1) - i], cadena_y[(n_cadena_y-1) - j])

            if cadena_x[(m_cadena_x-1) - i] == cadena_y[(n_cadena_y-1) - j]:
                
                matriz[i][j] = matriz[i-1][j-1] + costos['avanzar']
            else:
                insert = matriz[i][j-1] + costos['insertar']
                reemplazar = matriz[i-1][j-1] + costos['reemplazar']
                borrar = matriz[i-1][j] + costos['borrar']

                matriz[i][j] = min(insert, reemplazar, borrar)

    print(matriz)

    

consolaInteligente(cadena_x, cadena_y, costos)