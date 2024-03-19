#include <stdio.h>

int main() {
    char opcao;
    scanf("%c", &opcao);
    float media = 0, soma = 0;
    float matriz[12][12];
            for (int i = 0; i < 12; ++i) {
                for (int j = 0; j < 12; ++j) {
                    scanf("%f", &matriz[i][j]);
                }
            }

    switch (opcao) {
        case 'S': 
            for (int i = 0; i < 12; ++i) {
                for (int j = 0; j < 12; ++j) {
                    if (i < j)
                        soma += matriz[i][j];
                }
            }
            printf("%.1f\n", soma);
            break;
        case 'M':
            for (int i = 0; i < 12; ++i) {
                for (int j = 0; j < 12; ++j) {
                    if (i < j)
                        soma += matriz[i][j];
                }
            }
            media = soma / 66;
            printf("%.1f\n", media);
            break;
    }

    return 0;
}