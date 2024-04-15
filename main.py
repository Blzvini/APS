#%%
import matplotlib.pyplot as plt
import creatingArrays
import bubble_sort
import selection_sort
import insertion_sort
import heap_sort
import merge_sort
import quick_sort
import counting_sort
import bucket_sort
import radix_sort
import metrics


configuracoes = [5, 10, 50, 100, 1000, 10000]

for tamanho in configuracoes:
    creatingArrays.criar_vetor(tamanho)

algoritmos = {
    "Bubble Sort": bubble_sort.bubble_sort,
    "Selection Sort": selection_sort.selection_sort,
    "Insertion Sort": insertion_sort.insertion_sort,
    "Heap Sort": heap_sort.heap_sort,
    "Merge Sort": merge_sort.merge_sort,
    "Quick Sort": quick_sort.quicksort,
    "Counting Sort": counting_sort.counting_sort,
    "Bucket Sort": bucket_sort.bucket_sort,
    "Radix Sort": radix_sort.radix_sort
}

#%%
metricas = {nome: metrics.calcular_metricas(funcao, configuracoes) for nome, funcao in algoritmos.items()}

medias_por_tamanho = {tamanho: [] for tamanho in configuracoes}

for nome, metrica in metricas.items():
    for tamanho in configuracoes:
        medias_por_tamanho[tamanho].append(metrica[tamanho]['media_comparacoes'])

#%%
# Criando os gráficos de barras
for tamanho, medias in medias_por_tamanho.items():
    plt.figure(figsize=(12, 6))
    bars = plt.bar(algoritmos.keys(), medias, color='skyblue')
    plt.title(f'Médias para o vetor de tamanho {tamanho}')
    plt.xlabel('Algoritmo de Ordenação')
    plt.ylabel('Média de Comparações')
    plt.xticks(rotation=45, ha='right')
    
    for bar, media in zip(bars, medias):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{media:.2f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

