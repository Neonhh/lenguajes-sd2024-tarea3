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

int main() {

    int N, M;
    
    printf("Ingresa el numero de filas (N): ");
    scanf("%d", &N);
    printf("Ingresa el numero de columnas (M): ");
    scanf("%d", &M);

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
    
    //double tiempoRowMajor = sumarRowMajor(matrix, N, M);
    double tiempoRowMajor = sumarRowMajor(matrix, N, M);
    printf("Tiempo Row Major: %f\n", tiempoRowMajor);

    //double tiempoColMajor = sumarColMajor(matrix, N, M);
    double tiempoColMajor = sumarColMajor(matrix, N, M);
    printf("Tiempo Col Major: %f\n", tiempoColMajor);

    return 0;
    
}