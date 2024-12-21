## 3193. Conte o número de inversões

Você recebe um inteiro ne uma matriz 2D requirements, onde representa o índice final e a contagem de inversão de cada requisito.requirements[i] = [endi, cnti]

Um par de índices (i, j)de uma matriz de inteiros numsé chamado de inversão se:

i < jenums[i] > nums[j]
Retorna o número de
permutações
 permde [0, 1, 2, ..., n - 1]tal forma que para todo requirements[i] , tem exatamente inversões.perm[0..endi]cnti
 Como a resposta pode ser muito grande, retorne-a módulo .109 + 7
