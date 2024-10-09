costos = {
    'avanzar' : 1,
    'borrar' : 1,
    'reemplazar': 3,
    'insertar' :2,
    'kill' : 1
}

cadena_x = 'francesa'
cadena_y = 'ancestro'

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
        
        #----------En caso de que sea igual----------
        if cadena_x[i] == cadena_y[j]:
            
            if advance_cost < replace_cost:
                costo_total += advance_cost
                secuencia.append('avanzar')
                i+=1
                j+=1
            else:
                costo_total += advance_cost
                secuencia.append(f'reemplazar con {cadena_y[j]}')
                i+=1
                j+=1
        
        #----------En caso de que sean diferentes las cadenas----------
        else:
            
            if replace_cost <= delete_cost + insert_cost:
                costo_total += replace_cost
                secuencia.append(f'reemplazar con {cadena_y[j]}') 
                i += 1
                j += 1
            elif delete_cost < insert_cost:
                costo_total += delete_cost
                secuencia.append('borrar')  
                i += 1
            else:
                costo_total += insert_cost
                secuencia.append(f'insertar {cadena_y[j]}')
                j += 1
    #m = cadena original
    #n = cadena deseada
    if i < m:
        if kill_cost < delete_cost * (m - i):
            costo_total += kill_cost
            secuencia.append('kill') 
        else:
            while i < m:
                costo_total += delete_cost
                secuencia.append('borrar')  
                i += 1
    

    while j < n:
        costo_total += insert_cost
        secuencia.append(f'insertar {cadena_y[j]}')  
        j += 1
    
    return costo_total, secuencia

print(consolaVoraz(cadena_x, cadena_y, costos))