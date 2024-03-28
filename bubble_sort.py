def bubble_sort(vetor):
    """
    Ordena um vetor usando o algoritmo Bubble Sort.

    Parâmetros:
    vetor (list): Lista a ser ordenada.

    Retorna:
    int: Número de trocas realizadas durante a ordenação.
    """

    n = len(vetor)
    num_comparacoes = 0

    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            num_comparacoes += 1
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocou = True
        if not trocou:
            break;

    return num_comparacoes