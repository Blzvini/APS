def insertion_sort(vetor):
    """
    Ordena um vetor usando o algoritmo Insertion Sort.

    Parâmetros:
    vetor (list): Lista a ser ordenada.

    Retorna:
    int: Número de trocas realizadas durante a ordenação.
    """

    num_comparacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            num_comparacoes += 1
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return num_comparacoes