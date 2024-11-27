import numpy as np

ofertantes = [(500, 100, 600),
              (450, 400, 800)]

ofertantes2 = [(500, 400, 600),
               (450, 100, 800),
               (400, 100, 400),
               (200, 50, 200)]
A = 1000
B = 100




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
                
print(subastaDinamica(A, B, ofertantes2))                
  
                    