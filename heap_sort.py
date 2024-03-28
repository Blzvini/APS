def heapify(vetor, n, i, num_comparacoes):
    """
    Função que reorganiza o heap.

    Args:
        vetor (list): Lista a ser organizada como heap.
        n (int): Tamanho do heap.
        i (int): Índice do nó a ser heapificado.
        trocas_realizadas (int): Contador de trocas realizadas.

    Returns:
        int: Número total de trocas feitas durante o processo de heapificação.
    """

    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n:
        num_comparacoes[0] += 1
        if vetor[esquerda] > vetor[maior]:
            maior = esquerda

    if direita < n:
      num_comparacoes[0] += 1
      if vetor[esquerda] > vetor[maior]:
        maior = direita

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        heapify(vetor, n, maior, num_comparacoes)

def heap_sort(vetor):
    """
    Função que ordena uma lista usando o algoritmo Heap Sort.

    Args:
        vetor (list): Lista a ser ordenada.

    Returns:
        list: Lista ordenada.
        int: Número total de trocas feitas durante o processo de ordenação.
    """

    n = len(vetor)
    num_comparacoes = [0]

    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, n, i, num_comparacoes)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor, i, 0, num_comparacoes)

    return num_comparacoes[0]