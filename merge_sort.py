def merge_sort(vetor, inicio=0, fim=None):
    """
    Ordena um vetor utilizando o algoritmo Merge Sort e retorna o número de trocas realizadas.

    Args:
        vetor (list): A lista a ser ordenada.
        inicio (int, optional): O índice inicial do vetor (padrão é 0).
        fim (int, optional): O índice final do vetor (padrão é o comprimento do vetor).

    Returns:
        int: O número de trocas realizadas durante a ordenação.
    """

    if fim is None:
        fim = len(vetor)

    if(fim - inicio > 1):
        meio = (fim + inicio) // 2
        num_comparacoes = 0
        num_comparacoes += merge_sort(vetor, inicio, meio)
        num_comparacoes += merge_sort(vetor, meio, fim)
        num_comparacoes += merge(vetor, inicio, meio, fim)
        return num_comparacoes
    else:
        return 0
    
def merge(vetor, inicio, meio, fim):
    """
    Mescla duas partes ordenadas de um vetor e conta o número de trocas realizadas.

    Args:
        vetor (list): O vetor contendo as duas partes a serem mescladas.
        inicio (int): O índice inicial da parte a ser mesclada.
        meio (int): O índice que divide as duas partes a serem mescladas.
        fim (int): O índice final da parte a ser mesclada.

    Returns:
        int: O número de trocas realizadas durante a mesclagem.
    """

    esquerda = vetor[inicio:meio]
    direita = vetor[meio:fim]
    topo_esquerda, topo_direita = 0, 0
    num_comparacoes = 0
    for k in range(inicio, fim):
        if topo_esquerda < len(esquerda) and (topo_direita >= len(direita) or esquerda[topo_esquerda] <= direita[topo_direita]):
            vetor[k] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            vetor[k] = direita[topo_direita]
            topo_direita += 1
            num_comparacoes += len(esquerda) - topo_esquerda

    return num_comparacoes