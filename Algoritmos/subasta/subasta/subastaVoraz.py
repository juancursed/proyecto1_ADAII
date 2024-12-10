import numpy as np

def subastaVoraz(A, B, ofertantes):
    
    sol = []
    ofertantes.sort(key= lambda x : x[0], reverse = True)
    costo_total = 0
    
    i = 0
    while A != 0:
        
        if ofertantes[i][2] <= A: #Si el máximo cabe en el numero total de Acciones (A)
            A -= ofertantes[i][2]
            costo_total += ofertantes[i][0] * ofertantes[i][2]
            sol.append((ofertantes[i][2], f'x{i}'))
            i+=1
            
        elif ofertantes[i][1] <= A: #Si el minimo cabe en el numero total de acciones (A)
            A -= ofertantes[i][1]
            costo_total += ofertantes[i][0] * ofertantes[i][1]
            sol.append((ofertantes[i][1], f'x{i}'))
            i+=1
                
        if i == len(ofertantes):
            sol.append((A, 'Gobierno'))
            A = 0
            break
    
    return (costo_total, sol)