# Casos de teste

Os casos abaixo verificam as faixas de classificação, os limites aceitos e a
rejeição de entradas inválidas. A implementação principal e o teste automatizado
em Python podem ser executados na raiz do repositório:

```sh
python3 -m unittest testes.test_analisador
```

| Caso | Entrada | Resultado esperado |
| --- | --- | --- |
| Turma de exemplo | `[8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0]` | Quantidade 7; média 6,21; maior 9; menor 3; 3 aprovados; 2 em recuperação; 2 reprovados |
| Nota mínima | `[0]` | Reprovados: 1 |
| Nota máxima | `[10]` | Aprovados: 1 |
| Limite de aprovação | `[7]` | Aprovados: 1 |
| Limite de recuperação | `[5]` | Recuperação: 1 |
| Abaixo da aprovação | `[6.9]` | Recuperação: 1 |
| Abaixo da recuperação | `[4.9]` | Reprovados: 1 |
| Lista vazia | `[]` | Erro: lista não vazia |
| Valor textual | `["8"]` | Erro: todas as notas devem ser numéricas |
| Booleano em Python | `[True]` | Erro: booleanos não são notas numéricas válidas |
| Fora do intervalo | `[-0.1]` ou `[10.1]` | Erro: nota deve estar entre 0 e 10 |
| Valor não finito | `[NaN]` ou `[Infinity]` | Erro: nota deve ser finita |

As notas são dados fixos nos exemplos em C e JavaScript. Os casos de entrada
inválida podem ser verificados adaptando a lista no código; o conjunto automatizado
exercita diretamente a função Python.
