import tkinter as tk
from tkinter import ttk
import time
import matplotlib.pyplot as plt
from SubastaIngenua import subastaFuerzaBruta
from subastaPD import subastaDinamica
from subastaVoraz import subastaVoraz


def medir_tiempo(funcion, *args):
    """Mide el tiempo de ejecución de una función."""
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()
    tiempo_total_ms = (fin - inicio) * 1e3  # Tiempo en milisegundos
    return tiempo_total_ms, resultado


def ingenua_solution(A, B, ofertantes):
    tiempo, (costo, asignacion) = medir_tiempo(subastaFuerzaBruta, A, B, ofertantes)
    asignacion_text = "\n".join(f"- Ofertante {i + 1}: {acciones} acciones" for i, acciones in enumerate(asignacion[:-1]))
    return tiempo, f"Costo total: {costo}\nAsignaciones:\n{asignacion_text}\n- Gobierno: {asignacion[-1]} acciones"


def dinamica_solution(A, B, ofertantes):
    tiempo, (matriz, asignaciones) = medir_tiempo(subastaDinamica, A, B, ofertantes)
    costo_maximo = matriz[A, len(ofertantes)]  # Costo máximo en la celda final

    # Crear una descripción de las asignaciones
    asignaciones_text = "\n".join(
        f"- Ofertante {i + 1}: {acciones} acciones"
        for i, acciones in enumerate(asignaciones[:-1])
    )
    asignaciones_text += f"\n- Gobierno: {asignaciones[-1]} acciones"

    return tiempo, f"Costo total máximo: {costo_maximo}\nAsignaciones:\n{asignaciones_text}"



def voraz_solution(A, B, ofertantes):
    tiempo, (costo, asignacion) = medir_tiempo(subastaVoraz, A, B, ofertantes)
    asignaciones_text = "\n".join(f"Ofertante {i + 1}: {acciones[0]} acciones" for i, acciones in enumerate(asignacion[:-1]))
    acciones_gobierno = asignacion[-1]  # Última entrada es el número de acciones del gobierno
    return tiempo, f"Asignaciones:\n{asignaciones_text}\nGobierno: {acciones_gobierno[0]} acciones"


def solve():
    try:
        # Obtener datos de la GUI
        A = int(actions_entry.get())
        B = int(government_price_entry.get())
        ofertantes_texto = ofertantes_text.get("1.0", tk.END).strip()
        
        ofertantes = []
        for linea in ofertantes_texto.split("\n"):
            precio, minimo, maximo = map(int, linea.split(","))
            ofertantes.append((precio, minimo, maximo))
        
        # Ejecutar cada algoritmo y medir tiempos
        ingenua_time, ingenua_result = ingenua_solution(A, B, ofertantes)
        dinamica_time, dinamica_result = dinamica_solution(A, B, ofertantes)
        voraz_time, voraz_result = voraz_solution(A, B, ofertantes)
        
        # Mostrar resultados en la caja de texto
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"=== Solución Ingenua ===\n{ingenua_result}\nTiempo: {ingenua_time:.3f} ms\n\n")
        results_text.insert(tk.END, f"=== Solución Dinámica ===\n{dinamica_result}\nTiempo: {dinamica_time:.3f} ms\n\n")
        results_text.insert(tk.END, f"=== Solución Voraz ===\n{voraz_result}\nTiempo: {voraz_time:.3f} ms\n\n")
        
        # Graficar comparación de tiempos
        times = [ingenua_time, dinamica_time, voraz_time]
        labels = ["Ingenua", "Dinámica", "Voraz"]
        
        plt.figure(figsize=(10, 5))
        plt.bar(labels, times, color=["blue", "green", "red"])
        plt.ylabel("Tiempo (milisegundos)")
        plt.title("Comparación de tiempos de ejecución")
        plt.show()
    
    except Exception as e:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, f"Error al procesar la entrada: {e}")


# Crear la ventana principal
root = tk.Tk()
root.title("Benchmark de Algoritmos de Subasta")

# Datos de entrada
ttk.Label(root, text="Número de acciones disponibles (A):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
actions_entry = ttk.Entry(root, width=30)
actions_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Precio del gobierno (B):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
government_price_entry = ttk.Entry(root, width=30)
government_price_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Ofertantes (precio,min,max por línea):").grid(row=2, column=0, padx=10, pady=5, sticky="nw")
ofertantes_text = tk.Text(root, width=40, height=10)
ofertantes_text.grid(row=2, column=1, padx=10, pady=5)

# Botón para ejecutar la solución
solve_button = ttk.Button(root, text="Ejecutar Benchmark", command=solve)
solve_button.grid(row=3, column=0, columnspan=2, pady=10)

# Caja de resultados
results_text = tk.Text(root, width=80, height=20)
results_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
