# Classe MedianFinder

A mediana é o valor do meio em uma lista de inteiros ordenados. Se o tamanho da lista for par, não há valor do meio, e a mediana é a média dos dois valores do meio.

Por exemplo:
- Para `arr = [2, 3, 4]`, a mediana é `3`.
- Para `arr = [2, 3]`, a mediana é `(2 + 3) / 2 = 2.5`.

## Descrição

Implemente a classe **MedianFinder**:

1. `MedianFinder()`: Inicializa o objeto `MedianFinder`.
2. `void addNum(int num)`: Adiciona o inteiro `num` à estrutura de dados.
3. `double findMedian()`: Retorna a mediana de todos os elementos até agora. Respostas com uma diferença de até \(10^{-5}\) da resposta real serão aceitas.

---

## Exemplo de Uso

### Entrada:
```plaintext
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
