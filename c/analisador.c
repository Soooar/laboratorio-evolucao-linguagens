#include <math.h>
#include <stdio.h>

int main(void) {
    float notas[] = {8.5f, 6.0f, 9.0f, 4.5f, 7.0f, 5.5f, 3.0f};
    int quantidade = (int)(sizeof(notas) / sizeof(notas[0]));

    if (quantidade <= 0) {
        printf("A lista de notas nao pode estar vazia.\n");
        return 1;
    }

    float soma = 0.0f;
    float maior = notas[0];
    float menor = notas[0];
    int aprovados = 0;
    int recuperacao = 0;
    int reprovados = 0;

    for (int i = 0; i < quantidade; i++) {
        if (!isfinite(notas[i]) || notas[i] < 0.0f || notas[i] > 10.0f) {
            printf("Nota invalida: %.2f\n", notas[i]);
            return 1;
        }

        soma += notas[i];
        if (notas[i] > maior) {
            maior = notas[i];
        }
        if (notas[i] < menor) {
            menor = notas[i];
        }
        if (notas[i] >= 7.0f) {
            aprovados++;
        } else if (notas[i] >= 5.0f) {
            recuperacao++;
        } else {
            reprovados++;
        }
    }

    printf("Quantidade: %d\n", quantidade);
    printf("Media: %.2f\n", soma / quantidade);
    printf("Maior nota: %.2f\n", maior);
    printf("Menor nota: %.2f\n", menor);
    printf("Aprovados: %d\n", aprovados);
    printf("Recuperacao: %d\n", recuperacao);
    printf("Reprovados: %d\n", reprovados);
    return 0;
}
