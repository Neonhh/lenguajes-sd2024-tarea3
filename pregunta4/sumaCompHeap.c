#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Suma los elementos de una matriz en orden Row Major
// y devuelve el tiempo transcurrido en segundos
//double sumarRowMajor(int matrix[N][M], int N, int M)
double sumarRowMajor(int **matrix, long int N, long int M)
{
    clock_t inicio,final;
    double tiempo;
    inicio = clock();
    
    double sum = 0;
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            //printf("%d ", matrix[i][j]);
            sum += matrix[i][j];
        }
        //printf("\n");
    }

    final = clock();
    tiempo = (double)(final - inicio) / CLOCKS_PER_SEC;
    return tiempo;
}

// Suma los elementos de una matriz en orden Col Major
// y devuelve el tiempo transcurrido en segundos
//double sumarColMajor(int matrix[N][M], int N, int M)
double sumarColMajor(int **matrix, long int N, long int M)
{
    clock_t inicio,final;
    double tiempo;
    inicio = clock();
    
    double sum = 0;
    for(int j=0; j<M; j++)
    {
        for(int i=0; i<N; i++)
        {
            //printf("%d ", matrix[i][j]);
            sum += matrix[i][j];
        }
        //printf("\n");
    }

    final = clock();
    tiempo = (double)(final - inicio) / CLOCKS_PER_SEC;
    return tiempo;
}

int main(int argc, char *argv[]) {

    //procesa los argumentos pasados al ejecutar
    if(argc != 3)
    {
        printf("Uso: %s <N> <M>\n", argv[0]);
        return 1;
    }
    
    int N = atoi(argv[1]);
    int M = atoi(argv[2]);

    // Asignar memoria para la matriz
    
    int **matrix = (int **) malloc(N * sizeof(int *));
    if (matrix == NULL)
    {
        printf("Error al asignar memoria para las filas de la matriz.\n");
        return 1;
    }

    for (long int i = 0; i < N; i++){
        matrix[i] = (int *) malloc(M * sizeof(int));
        if (matrix[i] == NULL){
            printf("Error al asignar memoria para las columnas de la matriz.\n");
            
            // Liberar la memoria asignada previamente
            for(long int k = 0; k < i; k++)
            {
                free(matrix[k]);
            }
            
            free(matrix);
            return 1;
        }
    }
    
    double tiempoRowMajor = sumarRowMajor(matrix, N, M);
    printf("Tiempo Row Major: %f\n", tiempoRowMajor);

    double tiempoColMajor = sumarColMajor(matrix, N, M);
    printf("Tiempo Col Major: %f\n", tiempoColMajor);

    // Escribir el resultado en un archivo
    FILE *f = fopen("resultados.txt", "a");
    if (f == NULL)
    {
        printf("Error al abrir el archivo de resultados.\n");
        return 1;
    }
    fprintf(f, "%d %d %f %f\n", N, M, tiempoRowMajor, tiempoColMajor);
    fclose(f);

    // Liberar la memoria asignada
    for(int i = 0; i < N; i++)
    {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
    
}