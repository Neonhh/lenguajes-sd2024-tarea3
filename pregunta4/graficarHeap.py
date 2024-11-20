import os
import subprocess
import matplotlib.pyplot as plt

# Valores de N y M para probar
valores_N = [100, 1000, 10000, 100000, 1000000]
valores_M = [100, 1000, 10000, 100000, 1000000]

# Limpiar el archivo de resultados antes de comenzar
if os.path.exists("resultados.txt"):
    os.remove("resultados.txt")

subprocess.run(["gcc", "sumaCompHeap.c","-o", "a", "-lm"])
# Ejecutar el programa con diferentes valores de N y M
for N in valores_N:
    for M in valores_M:
        print(f"\nEjecutando para N={N}, M={M}.")
        result = subprocess.run(["./a", str(N), str(M)])
        if result.returncode != 0:
            print(f"Error con N={N}, M={M}. Continuando.")
            break # deja de escribir en el archivo si hay un error

# Leer los resultados del archivo
resultados = []
with open("resultados.txt", "r") as f:
    for line in f:
        N, M, tiempoRow, tiempoCol = line.split()
        resultados.append((int(N), int(M), float(tiempoRow), float(tiempoCol)))

# Dividimos los datos en varios graficos para legibilidad
graficas = [resultados[0:5],resultados[5:10],resultados[10:]]

# Crear una figura con 3 subgráficas
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

for i, g in enumerate(graficas):
    # Separar datos
    NM = [f"({r[0]},{r[1]})" for r in g]
    tiemposRow = [r[2] for r in g]
    tiemposCol = [r[3] for r in g]

    axs[i].scatter(NM, tiemposRow, label="Row Major con respecto a (N, M)", color='b', marker='o')
    axs[i].scatter(NM, tiemposCol, label="Column Major con respecto a (N, M)", color='r', marker='x')
    axs[i].set_xlabel("Tamaño de (N, M)")
    axs[i].set_ylabel("Tiempo (segundos)")
    axs[i].legend()
    if i == 0:
        axs[i].set_title(f"Tiempo de ejecución vs Tamaño de (N, M)")
    axs[i].grid(True)
    axs[i].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()