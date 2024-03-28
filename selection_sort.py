def selection_sort(vetor):
    """
    Ordena um vetor usando o algoritmo Selection Sort.

    Parâmetros:
    vetor (list): Lista a ser ordenada.

    Retorna:
    int: Número de trocas realizadas durante a ordenação.
    """

    n = len(vetor)
    num_comparacoes = 0

    for i in range(n):
        indice_menor = i
        for j in range(i+1, n):
            num_comparacoes += 1
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j
        vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
    return num_comparacoes
