def insertion_sort_bucket(vetor):
    """
    Implementação do algoritmo de ordenação Insertion Sort adaptado para ordenar baldes em um Bucket Sort.

    Args:
    vetor (list): Uma lista de números a serem ordenados.

    Returns:
    int: O número total de comparações realizadas durante o processo de ordenação.
    """

    num_comparacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0:
            num_comparacoes += 1  # Conta uma comparação
            if chave < vetor[j]:
                vetor[j + 1] = vetor[j]
                j -= 1
            else:
                break
        vetor[j + 1] = chave
    return num_comparacoes

def bucket_sort(vetor):
    """
    Implementação do algoritmo de ordenação Bucket Sort.

    Args:
    vetor (list): Uma lista de números a serem ordenados.

    Returns:
    int: O número total de comparações realizadas durante o processo de ordenação.
    """

    num_baldes = 10
    num_comparacoes = 0

    baldes = [[] for _ in range(num_baldes)]

    for num in vetor:
        num = num / 10000
        indice = min(int(num * num_baldes), num_baldes - 1)
        #indice = int(num * num_baldes)
        baldes[indice].append(num)

    for balde in baldes:
        num_comparacoes += insertion_sort_bucket(balde)

    return num_comparacoes