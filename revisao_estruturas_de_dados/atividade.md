#include <stdio.h>

// Define o tamanho das matrizes: 10 linhas e 10 colunas
#define TAM 10

int main(void) {
    // Declaração das matrizes
    int A[TAM][TAM];
    int B[TAM][TAM];
    int C[TAM][TAM];

    // Variáveis usadas para percorrer as matrizes
    int i, j;

    // Valor inicial usado para preencher a matriz A
    int valor = 1;

    // Preenche a matriz A com valores de 1 até 100
    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            A[i][j] = valor;
            valor++;
        }
    }

    // Preenche a matriz B com o dobro dos valores originais de A
    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            B[i][j] = A[i][j] * 2;
        }
    }

    // Preenche a matriz C com a soma de A e B
    // Neste momento, os valores pares de A ainda não foram alterados
    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }

    // Substitui todos os valores pares da matriz A pelo número 2
    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            if (A[i][j] % 2 == 0) {
                A[i][j] = 2;
            }
        }
    }

    // Exibe a matriz A modificada
    printf("Matriz A:\n");

    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            printf("%4d ", A[i][j]);
        }

        // Pula uma linha após imprimir cada linha da matriz
        printf("\n");
    }

    // Exibe a matriz B
    printf("\nMatriz B:\n");

    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            printf("%4d ", B[i][j]);
        }

        printf("\n");
    }

    // Exibe a matriz C
    printf("\nMatriz C (A + B):\n");

    for (i = 0; i < TAM; i++) {
        for (j = 0; j < TAM; j++) {
            printf("%4d ", C[i][j]);
        }

        printf("\n");
    }

    // Indica que o programa terminou corretamente
    return 0;
}
