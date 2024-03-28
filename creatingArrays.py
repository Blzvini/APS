import os
import random

def criar_vetor(tamanho, diretorio="./vetores/"):
    """
    Cria um vetor de inteiros aleatórios dentro do intervalo de 0 a 100000 e salva em um arquivo.

    Parâmetros:
    tamanho (int): Tamanho do vetor a ser criado.
    diretorio (str): Diretório onde os arquivos serão salvos.

    Retorna:
    None
    """
    tamanho_dir = diretorio + str(tamanho) + "/"
    os.makedirs(tamanho_dir, exist_ok=True)
    
    quantidade = 50
    
    for i in range(quantidade):
        vetor = [random.randint(0, 100000) for _ in range(tamanho)]
        
        with open(tamanho_dir + f"vetor_{i}.txt", "w") as file:
            file.write("\n".join(map(str, vetor)))