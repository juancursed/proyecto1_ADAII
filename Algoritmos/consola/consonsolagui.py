import tkinter as tk
from tkinter import ttk
import time
import matplotlib.pyplot as plt
from consolaIngenua import consolaFuerzaBruta
from consolaDinamica import consolaInteligente
from consolaVoraz import consolaVoraz


def medir_tiempo(funcion, start, target, costos):
    inicio = time.perf_counter() 
    resultado = funcion(start, target, costos)
    fin = time.perf_counter()
    tiempo_total_ms = (fin - inicio) * 1e3  
    return tiempo_total_ms, resultado

def ingenua_solution(start, target, costos):
    tiempo, (costo_minimo, pasos) = medir_tiempo(consolaFuerzaBruta, start, target, costos)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo mínimo: {costo_minimo}\nPasos:\n{pasos_text}"

def dinamica_solution(start, target, costos):
    tiempo, (costo_minimo, pasos) = medir_tiempo(consolaInteligente, start, target, costos)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo mínimo: {costo_minimo}\nPasos:\n{pasos_text}"

def voraz_solution(start, target, costos):
    tiempo, (costo_total, pasos) = medir_tiempo(consolaVoraz, start, target, costos)
    pasos_text = "\n".join(f"- {paso}" for paso in pasos)
    return tiempo, f"Costo total: {costo_total}\nPasos:\n{pasos_text}"

def solve():
    start = start_entry.get()
    target = target_entry.get()
    
    # Obtener los costos ingresados por el usuario
    costos = {
        'avanzar': float(avanzar_entry.get() or 1),
        'borrar': float(borrar_entry.get() or 2),
        'reemplazar': float(reemplazar_entry.get() or 3),
        'insertar': float(insertar_entry.get() or 2),
        'kill': float(kill_entry.get() or 4)
    }
    
    # Ejecutar soluciones
    ingenua_time, ingenua_steps = ingenua_solution(start, target, costos)
    dinamica_time, dinamica_steps = dinamica_solution(start, target, costos)
    voraz_time, voraz_steps = voraz_solution(start, target, costos)
    
    # Mostrar resultados en la GUI
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, f"Solución ingenua:\n{ingenua_steps}\nTiempo: {ingenua_time:.3f} ms\n\n")
    results_text.insert(tk.END, f"Solución dinámica:\n{dinamica_steps}\nTiempo: {dinamica_time:.3f} ms\n\n")
    results_text.insert(tk.END, f"Solución voraz:\n{voraz_steps}\nTiempo: {voraz_time:.3f} ms\n\n")
    
    # Grafiquitiqui
    times = [ingenua_time, dinamica_time, voraz_time]
    labels = ['Ingenua', 'Dinámica', 'Voraz']
    
    plt.figure(figsize=(10, 5))
    plt.bar(labels, times, color=['blue', 'green', 'red'])
    plt.ylabel('Tiempo (milisegundos)')
    plt.title('Comparación de tiempos de ejecución')
    plt.show()

# Guicita
root = tk.Tk()
root.title("Comparación de Soluciones")

# Entrada para la cadena de inicio
ttk.Label(root, text="Cadena de inicio:").grid(column=0, row=0, padx=10, pady=10)
start_entry = ttk.Entry(root, width=30)
start_entry.grid(column=1, row=0, padx=10, pady=10)

# Entrada para la cadena objetivo
ttk.Label(root, text="Cadena objetivo:").grid(column=0, row=1, padx=10, pady=10)
target_entry = ttk.Entry(root, width=30)
target_entry.grid(column=1, row=1, padx=10, pady=10)

# Entrada para los costos
ttk.Label(root, text="Costo de avanzar:").grid(column=0, row=2, padx=10, pady=10)
avanzar_entry = ttk.Entry(root, width=30)
avanzar_entry.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(root, text="Costo de borrar:").grid(column=0, row=3, padx=10, pady=10)
borrar_entry = ttk.Entry(root, width=30)
borrar_entry.grid(column=1, row=3, padx=10, pady=10)

ttk.Label(root, text="Costo de reemplazar:").grid(column=0, row=4, padx=10, pady=10)
reemplazar_entry = ttk.Entry(root, width=30)
reemplazar_entry.grid(column=1, row=4, padx=10, pady=10)

ttk.Label(root, text="Costo de insertar:").grid(column=0, row=5, padx=10, pady=10)
insertar_entry = ttk.Entry(root, width=30)
insertar_entry.grid(column=1, row=5, padx=10, pady=10)

ttk.Label(root, text="Costo de kill:").grid(column=0, row=6, padx=10, pady=10)
kill_entry = ttk.Entry(root, width=30)
kill_entry.grid(column=1, row=6, padx=10, pady=10)

# Botón para ejecutar la resolución
solve_button = ttk.Button(root, text="Resolver", command=solve)
solve_button.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

# Cuadro de texto para mostrar los resultados
results_text = tk.Text(root, width=80, height=20)
results_text.grid(column=0, row=8, columnspan=2, padx=10, pady=10)

root.mainloop()
