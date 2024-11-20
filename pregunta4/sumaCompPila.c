#include <stdio.h>
#include <time.h>

int N, M;

// Suma los elementos de una matriz en orden Row Major
// y devuelve el tiempo transcurrido en segundos
double sumarRowMajor(int matrix[N][M], int N, int M)
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
double sumarColMajor(int matrix[N][M], int N, int M)
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
    int N, M;  //El maximo tamaño valido es de 1000x100
    printf("Ingresa el numero de filas (N): ");
    scanf("%d", &N);
    printf("Ingresa el numero de columnas (M): ");
    scanf("%d", &M);

    int matrix[N][M]; 
    
    double tiempoRowMajor = 0;
    for (int t = 0; t<3; t++){
        double tiempo = sumarRowMajor(matrix, N, M);
        printf("Tiempo Row Major %d: %f\n",t+1 , tiempo);
        tiempoRowMajor += tiempo;
    }
    tiempoRowMajor = tiempoRowMajor/3;
    printf("Promedio de tiempos RowMajor: %f\n", tiempoRowMajor);

    double tiempoColMajor = 0;
    for (int t = 0; t<3; t++){
        double tiempo = sumarColMajor(matrix, N, M);
        printf("Tiempo Col Major %d: %f\n",t+1 , tiempo);
        tiempoColMajor += tiempo;
    }
    tiempoColMajor = tiempoColMajor/3;
    printf("Promedio de tiempos ColMajor: %f\n", tiempoColMajor);
    return 0;
    
}