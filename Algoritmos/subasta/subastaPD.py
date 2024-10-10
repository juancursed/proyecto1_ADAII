import numpy as np

ofertantes = [(500, 1, 6),
              (450, 4, 8)]

ofertantes2 = [(500, 4, 6),
               (450, 1, 8),
               (400, 1, 4),
               (200, 1, 2)]
A = 10
B = 1




def subastaDinamica(A, B, ofertantes):
    
    n = len(ofertantes)
    
    matriz_costo = np.zeros((A+1, n+1), dtype=np.int64)    
    
    #inicializar la matriz
    
    for i in range(0, A+1):
        for j in range(0, n+1):
            
            if i == 0:
                matriz_costo[i,j] = 0
            elif j == 0:
                matriz_costo[i,j] = i * B
            elif (i >= ofertantes[j-1][1] and i <  ofertantes[j-1][2]): #si esta en el rango min o max
                matriz_costo[i,j] = max(
                    matriz_costo[i, j-1],  #no comprar acciones
                    matriz_costo[i - ofertantes[j-1][1], j-1] + ofertantes[j-1][0] * ofertantes[j-1][1], #comprar el minimo de accion 
                    matriz_costo[0, j-1] + ofertantes[j-1][0] * i  #comprar el maximo de acciones disponibles
                )
            elif i >= ofertantes[j-1][2]: #Si esta en el limite maximo
                matriz_costo[i,j] = max(
                    matriz_costo[i, j-1],  #no comprar acciones
                    matriz_costo[i - ofertantes[j-1][1], j-1] + ofertantes[j-1][0] * ofertantes[j-1][1], #comprar el minimo de accion 
                    matriz_costo[i - ofertantes[j-1][2], j-1] + ofertantes[j-1][0] * ofertantes[j-1][2]  #comprar el maximo de acciones
                )
            
    
    return matriz_costo       
                
print(subastaDinamica(10, 1, ofertantes2))                
  
                    