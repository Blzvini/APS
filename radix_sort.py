def counting_sort_radix(vetor, exp1):
    """
    Implementação do algoritmo de ordenação Counting Sort para ser usado como parte do Radix Sort.

    Args:
    vetor (list): Uma lista de inteiros a serem ordenados.
    exp1 (int): O expoente a ser usado na ordenação.

    Returns:
    int: O número total de operações realizadas.
    """

    n = len(vetor)
    output = [0] * n
    count = [0] * 10
    num_operacoes = 0

    for i in range(n):
        index = (vetor[i] // exp1)
        count[(index) % 10] += 1
        num_operacoes += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
        num_operacoes += 1

    i = n - 1
    while i >= 0:
        index = (vetor[i] // exp1)
        output[count[(index) % 10] - 1] = vetor[i]
        count[(index) % 10] -= 1
        i -= 1
        num_operacoes += 1

    i = 0
    for i in range(len(vetor)):
        vetor[i] = output[i]
        num_operacoes += 1

    return num_operacoes

def radix_sort(vetor):
    """
    Implementação do algoritmo de ordenação Radix Sort.

    Args:
    vetor (list): Uma lista de inteiros a serem ordenados.

    Returns:
    int: O número total de operações realizadas.
    """

    max1 = max(vetor)
    exp = 1
    num_operacoes = 0
    while max1 / exp > 0:
        num_operacoes += counting_sort_radix(vetor, exp)
        exp *= 10
    return num_operacoes