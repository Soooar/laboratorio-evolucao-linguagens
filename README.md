# Laboratório: evolução das linguagens de programação

Comparação prática entre Python, C e JavaScript por meio de um analisador de
desempenho acadêmico. O projeto também apresenta três estilos de programação em
Python: procedural, funcional e orientado a objetos.

## Estrutura

```text
.
├── c/analisador.c
├── docs/relatorio.md
├── javascript/analisador.js
├── python/
│   ├── analisador.py
│   ├── funcional.py
│   ├── objetos.py
│   └── procedural.py
└── testes/
    ├── casos-teste.md
    └── test_analisador.py
```

## Executar

Na raiz do repositório:

```sh
python3 python/analisador.py
python3 -m unittest testes.test_analisador
gcc c/analisador.c -o analisador
./analisador
node javascript/analisador.js
python3 python/procedural.py
python3 python/funcional.py
python3 python/objetos.py
```

O analisador classifica as notas de 0 a 10: aprovação a partir de 7,0;
recuperação a partir de 5,0 e abaixo de 7,0; reprovação abaixo de 5,0.
As três implementações principais usam a lista de exemplo definida no código.

Os casos e resultados esperados estão em [testes/casos-teste.md](testes/casos-teste.md);
uma análise comparativa está em [docs/relatorio.md](docs/relatorio.md).