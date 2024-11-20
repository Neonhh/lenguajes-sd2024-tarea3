import os
import subprocess
import matplotlib.pyplot as plt

# Valores de N y M para probar
valores_N = [100, 200, 300, 400, 500]
valores_M = [100, 200, 300, 400, 500]

# Limpiar el archivo de resultados antes de comenzar
if os.path.exists("resultados.txt"):
    os.remove("resultados.txt")

# Ejecutar el programa con diferentes valores de N y M
for N in valores_N:
    for M in valores_M:
        result = subprocess.run(["./a", str(N), str(M)])
        if result.returncode != 0:
            print(f"Error con N={N}, M={M}. Terminando ejecuciones y pasando a graficar.")
            break # deja de escribir en el archivo si hay un error

# Leer los resultados del archivo
resultados = []
with open("resultados.txt", "r") as f:
    for line in f:
        N, M, tiempoRow, tiempoCol = line.split()
        resultados.append((int(N), int(M), float(tiempoRow), float(tiempoCol)))

# Generar el gráfico
Ns = [r[0] for r in resultados]
Ms = [r[1] for r in resultados]
tiemposRow = [r[2] for r in resultados]
tiemposCol = [r[3] for r in resultados]

plt.scatter(Ns, tiemposRow, label="Row Major con respecto a N")
plt.scatter(Ns, tiemposCol, label="Column Major con respecto a N", color='r')
plt.xlabel("Tamaño de N")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.title("Tiempo de ejecución vs Tamaño de N")
plt.show()

plt.scatter(Ms, tiemposRow, label="Row Major con respecto a M")
plt.scatter(Ms, tiemposCol, label="Column Major con respecto a M", color='r')
plt.xlabel("Tamaño de M")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.title("Tiempo de ejecución vs Tamaño de M")
plt.show()