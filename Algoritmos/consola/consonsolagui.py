import tkinter as tk
from tkinter import ttk
import time
import matplotlib.pyplot as plt
from consolaIngenua import consolaFuerzaBruta
from consolaDinamica import consolaInteligente
from consolaVoraz import consolaVoraz


COSTOS = {
    'avanzar': 1,
    'borrar': 2,
    'reemplazar': 3,
    'insertar': 2,
    'kill': 4
}


def medir_tiempo(funcion, start, target):
    inicio = time.perf_counter() 
    resultado = funcion(start, target, COSTOS)
    fin = time.perf_counter()
    tiempo_total_ms = (fin - inicio) * 1e3  
    return tiempo_total_ms, resultado

def ingenua_solution(start, target):
    tiempo, (costo_minimo, pasos) = medir_tiempo(consolaFuerzaBruta, start, target)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo mínimo: {costo_minimo}\nPasos:\n{pasos_text}"

def dinamica_solution(start, target):
    tiempo, (costo_minimo, pasos) = medir_tiempo(consolaInteligente, start, target)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo mínimo: {costo_minimo}\nPasos:\n{pasos_text}"

def voraz_solution(start, target):
    tiempo, (costo_total, pasos) = medir_tiempo(consolaVoraz, start, target)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo total: {costo_total}\nPasos:\n{pasos_text}"


def solve():
    start = start_entry.get()
    target = target_entry.get()
    
    # Ejecutar soluciones
    ingenua_time, ingenua_steps = ingenua_solution(start, target)
    dinamica_time, dinamica_steps = dinamica_solution(start, target)
    voraz_time, voraz_steps = voraz_solution(start, target)
    
    # Mostrar resultados en la GUI
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, f"Solución ingenua:\n{ingenua_steps}\nTiempo: {ingenua_time:.3f} ms\n\n")
    results_text.insert(tk.END, f"Solución dinámica:\n{dinamica_steps}\nTiempo: {dinamica_time:.3f} ms\n\n")
    results_text.insert(tk.END, f"Solución voraz:\n{voraz_steps}\nTiempo: {voraz_time:.3f} ms\n\n")
    
#Grafiquitiqui
    times = [ingenua_time, dinamica_time, voraz_time]
    labels = ['Ingenua', 'Dinámica', 'Voraz']
    
    plt.figure(figsize=(10, 5))
    plt.bar(labels, times, color=['blue', 'green', 'red'])
    plt.ylabel('Tiempo (milisegundos)')

    plt.title('Comparación de tiempos de ejecución')
    plt.show()

#Guicita
root = tk.Tk()
root.title("Comparación de Soluciones")


ttk.Label(root, text="Cadena de inicio:").grid(column=0, row=0, padx=10, pady=10)
start_entry = ttk.Entry(root, width=30)
start_entry.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Cadena objetivo:").grid(column=0, row=1, padx=10, pady=10)
target_entry = ttk.Entry(root, width=30)
target_entry.grid(column=1, row=1, padx=10, pady=10)


solve_button = ttk.Button(root, text="Resolver", command=solve)
solve_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)


results_text = tk.Text(root, width=80, height=20)
results_text.grid(column=0, row=3, columnspan=2, padx=10, pady=10)


root.mainloop()
