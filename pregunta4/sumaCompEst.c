#include <stdio.h>
#include <time.h>

#define N 1000
#define M 1000

int matrix[N][M]; 

// Suma los elementos de una matriz en orden Row Major
// y devuelve el tiempo transcurrido en segundos
double sumarRowMajor(int matrix[N][M])
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
double sumarColMajor(int matrix[N][M])
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
    
    //double tiempoRowMajor = sumarRowMajor(matrix, N, M);
    double tiempoRowMajor = sumarRowMajor(matrix);
    printf("Tiempo Row Major: %f\n", tiempoRowMajor);

    //double tiempoColMajor = sumarColMajor(matrix, N, M);
    double tiempoColMajor = sumarColMajor(matrix);
    printf("Tiempo Col Major: %f\n", tiempoColMajor);

    return 0;
    
}