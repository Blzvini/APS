def quicksort(vetor, inicio=0, fim=None):
    """
    Ordena um vetor utilizando o algoritmo QuickSort e retorna o número de trocas realizadas.

    Args:
        vetor (list): A lista a ser ordenada.
        inicio (int, optional): O índice inicial do vetor (padrão é 0).
        fim (int, optional): O índice final do vetor (padrão é o comprimento do vetor - 1).

    Returns:
        int: O número de trocas realizadas durante a ordenação.
    """

    if fim is None:
        fim = len(vetor) - 1

    num_comparacoes = [0]

    def _quicksort(vetor, inicio, fim):
        if inicio < fim:
            pivo, comparacoes = particao(vetor, inicio, fim)
            num_comparacoes[0] += comparacoes
            _quicksort(vetor, inicio, pivo - 1)
            _quicksort(vetor, pivo + 1, fim)

    _quicksort(vetor, inicio, fim)
    return num_comparacoes[0]

def particao(vetor, inicio, fim):
    """
    Realiza a partição de um vetor para o algoritmo QuickSort.

    Args:
        vetor (list): O vetor a ser particionado.
        inicio (int): O índice inicial da partição.
        fim (int): O índice final da partição.

    Returns:
        tuple: Uma tupla contendo o índice do pivo e o número de trocas realizadas durante a partição.
    """
    pivo = vetor[fim]
    index = inicio
    num_comparacoes = 0
    for j in range(inicio, fim):
        num_comparacoes += 1
        if vetor[j] <= pivo:
            vetor[j], vetor[index] = vetor[index], vetor[j]
            index += 1
    vetor[index], vetor[fim] = vetor[fim], vetor[index]
    return index, num_comparacoes