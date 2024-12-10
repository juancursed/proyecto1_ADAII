def subastaFuerzaBruta(cantidad_total, precio_gobierno, ofertas):
    num_ofertas = len(ofertas)
    mejor_valor = 0
    mejor_distribucion = []

    def evaluar_opciones(posicion, distribucion_actual, acciones_disponibles):
        nonlocal mejor_valor, mejor_distribucion


        if posicion == num_ofertas:
            valor_actual = sum(distribucion_actual[i] * ofertas[i][0] for i in range(num_ofertas))
            valor_actual += acciones_disponibles * precio_gobierno  

            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_distribucion = distribucion_actual[:]
            return


        precio, minimo, maximo = ofertas[posicion]

        for asignadas in range(minimo, min(maximo, acciones_disponibles) + 1):
            distribucion_actual[posicion] = asignadas
            evaluar_opciones(posicion + 1, distribucion_actual, acciones_disponibles - asignadas)


        distribucion_actual[posicion] = 0
        evaluar_opciones(posicion + 1, distribucion_actual, acciones_disponibles)

    evaluacion_inicial = [0] * num_ofertas
    evaluar_opciones(0, evaluacion_inicial, cantidad_total)


    sobrante = cantidad_total - sum(mejor_distribucion)
    mejor_distribucion.append(sobrante)

    return mejor_valor, mejor_distribucion
