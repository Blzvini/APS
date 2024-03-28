def counting_sort(vetor):
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