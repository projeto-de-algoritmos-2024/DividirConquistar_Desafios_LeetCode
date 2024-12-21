# 3193. Conte o Número de Inversões

Você recebe um inteiro `n` e uma matriz 2D `requirements`, onde `requirements[i] = [endi, cnti]` representa o índice final e a contagem de inversões de cada requisito.

Um par de índices `(i, j)` de uma matriz de inteiros `nums` é chamado de inversão se:

- `i < j` e `nums[i] > nums[j]`.

Retorne o número de **permutações** `perm` de `[0, 1, 2, ..., n - 1]` tal que, para todo `requirements[i]`, o prefixo `perm[0..endi]` tenha exatamente `cnti` inversões.

Como a resposta pode ser muito grande, retorne-a módulo \(10^9 + 7\).