def calcular_metricas(algoritmo, configuracoes, diretorio="./vetores/"):
    """
    Calcula as métricas de um algoritmo de ordenação para diferentes tamanhos de vetores.

    Parâmetros:
    algoritmo (function): Função que representa o algoritmo de ordenação.
    configuracoes (list): Lista de tamanhos de vetores a serem testados.
    diretorio (str): Diretório onde os arquivos de vetores estão salvos.

    Retorna:
    dict: Dicionário com as métricas calculadas para cada tamanho de vetor.
    """
    metricas = {}

    for tamanho in configuracoes:
        tamanho_dir = diretorio + str(tamanho) + "/"
        quantidade = 50
        total_comparacoes = 0
        
        for i in range(quantidade):
            with open(tamanho_dir + f"vetor_{i}.txt", "r") as file:
                vetor = [int(line.strip()) for line in file]

            comparacoes = algoritmo(vetor.copy())
            total_comparacoes += comparacoes

        media_comparacoes = total_comparacoes / quantidade

        metricas[tamanho] = {
            "total_comparacoes": total_comparacoes,
            "media_comparacoes": media_comparacoes
        }

    return metricas
