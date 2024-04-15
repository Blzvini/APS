def counting_sort(vetor):
    """
    Ordena um vetor de números inteiros não negativos usando o algoritmo Counting Sort.

    Args:
    vetor (list[int]): O vetor a ser ordenado.

    Returns:
    int: O número total de operações realizadas durante a ordenação.
    """
    
    valor_maximo = max(vetor)
    count = [0] * (valor_maximo + 1)
    num_operacoes = 0

    for num in vetor:
        count[num] += 1
        num_operacoes += 1

    vetor_ordenado = [0] * len(vetor)

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        num_operacoes += 1

    for num in reversed(vetor):
        index = count[num] - 1
        vetor_ordenado[index] = num
        count[num] -= 1
        num_operacoes += 1

    return num_operacoes