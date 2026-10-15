# Relatório técnico

## Análise das implementações

1. **Quantidade de código.** Para este problema, Python e JavaScript permitem
   expressar somas e contagens com funções de coleção (`sum`, `reduce` e
   `filter`), enquanto C exige declarar variáveis e percorrer a lista
   explicitamente. Isso torna a implementação em C mais extensa, mas também
   deixa cada etapa de processamento visível.

2. **Declaração e uso de variáveis.** C declara os tipos (`float` e `int`)
   antes do uso e representa a turma em um vetor de tamanho fixo. Python e
   JavaScript associam valores a nomes sem declarar previamente o tipo da
   variável. Em Python, `bool` é uma subclasse de `int`, por isso a validação
   verifica e rejeita explicitamente valores booleanos.

3. **Compilação e execução.** No experimento, C exige uma etapa explícita de
   compilação com `gcc` antes da execução do programa gerado. Python é executado
   pelo interpretador e JavaScript pelo ambiente Node.js; ambos executam os
   arquivos-fonte diretamente nos comandos apresentados.

4. **Tipagem e validação.** C oferece tipos declarados em compilação, mas ainda
   precisa validar se as notas estão no intervalo permitido. Python e
   JavaScript também verificam o tipo em tempo de execução. As implementações
   rejeitam notas não finitas e valores fora de 0 a 10; Python também distingue
   booleanos de números válidos.

5. **Compreensão e manutenção.** Para uma turma pequena e uma rotina direta,
   Python é conciso e legível. C evidencia o algoritmo e a representação dos
   dados. JavaScript demonstra operações funcionais sobre coleções. Em um
   sistema acadêmico maior, a escolha dependeria também de integração,
   desempenho, equipe e ambiente de execução, e não apenas da quantidade de
   linhas.

6. **Riscos sem validação.** Valores fora da escala, texto, valores não finitos
   ou uma lista vazia poderiam produzir classificações sem sentido, erros ou
   divisões inválidas. A validação deve ocorrer antes dos cálculos e do acesso
   aos elementos.

7. **Organização com Git.** O Git registra as mudanças em commits, permitindo
   acompanhar a evolução das implementações, comparar versões e identificar
   quando cada alteração foi feita. O histórico também documenta a atividade.

8. **`git add`, `git commit` e `git push`.** `git add` prepara arquivos para o
   próximo commit; `git commit` grava essa versão no histórico local; `git push`
   envia commits locais para o repositório remoto.

9. **Salvar e enviar ao GitHub.** Salvar no Codespaces grava o arquivo no
   ambiente de trabalho. Isso não cria automaticamente um commit nem envia a
   alteração ao GitHub: para isso, é necessário preparar, registrar e enviar a
   mudança com Git.

10. **Escolha de linguagem.** Python é adequado quando produtividade,
    legibilidade e bibliotecas são prioritárias; C é apropriado quando controle
    explícito de memória e representação ou integração de baixo nível são
    relevantes; JavaScript é especialmente adequado para aplicações web e
    ambientes baseados em Node.js. A decisão real depende dos requisitos do
    sistema.

## Resultados da execução de referência

As implementações Python, C e JavaScript usam as notas
`[8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0]`. O resultado comum é:

- Quantidade: 7
- Média: 6,21
- Maior nota: 9,00
- Menor nota: 3,00
- Aprovados: 3
- Em recuperação: 2
- Reprovados: 2

Os três exemplos de paradigmas em Python usam `[8.0, 7.0, 9.0]` e calculam
média `8.0`. No estilo procedural, os comandos atualizam uma soma; no exemplo
funcional, a soma é expressa com `sum`; na versão orientada a objetos, os dados
e o método de cálculo ficam agrupados em `Turma`. A solução funcional mostrada
usa uma função de biblioteca, mas isso, por si só, não caracteriza programação
funcional pura.

As perguntas sobre a instalação efetiva das ferramentas e a experiência
individual com o Codespaces devem ser complementadas pelo estudante conforme o
ambiente e as observações da própria execução.
