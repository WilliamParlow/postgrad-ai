import os
import sys
import numpy as np
from tensorflow import keras
import pandas as pd
from tqdm import tqdm_notebook as tqdm
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Função para carregar o arquivo CSV e criar um mapeamento de cores para classes
def carregar_mapeamento_classes(csv_path):
    # Carrega o arquivo CSV para um DataFrame do pandas
    df = pd.read_csv(csv_path)
    
    # Extrai as colunas 'r', 'g', 'b' como um array numpy, representando as cores RGB
    cores = df[['r', 'g', 'b']].values
    
    # Extrai a coluna 'name', que contém os nomes das classes
    nomes_classes = df['name'].values
    
    # Cria um dicionário que mapeia as tuplas de cores (r, g, b) para um índice numérico
    # A função enumerate é usada para associar cada cor a um índice
    mapeamento_classes = {tuple(cor): i for i, cor in enumerate(cores)}
    
    # Retorna o dicionário de mapeamento de cores para índices e a lista de nomes das classes
    return mapeamento_classes, nomes_classes


def carregar_preproc_imagem(image_path, label_path, target_size=(224, 224), mapeamento_classes=None):
    # Carrega a imagem de entrada a partir do caminho especificado e redimensiona para o tamanho alvo
    image = keras.preprocessing.image.load_img(image_path, target_size=target_size)
    
    # Converte a imagem carregada em um array numpy e normaliza os valores de pixel para o intervalo [0, 1]
    image = keras.preprocessing.image.img_to_array(image) / 255.0

    # Carrega a imagem do rótulo (label) a partir do caminho especificado e redimensiona para o tamanho alvo
    label = keras.preprocessing.image.load_img(label_path, target_size=target_size)
    
    # Converte o rótulo carregado em um array numpy e o converte para o tipo uint8 para garantir compatibilidade
    label = keras.preprocessing.image.img_to_array(label).astype(np.uint8)

    # Se um mapeamento de classes for fornecido, converte a máscara RGB em inteiros correspondentes às classes
    if mapeamento_classes is not None:
        # Obtém a altura, largura e número de canais do rótulo
        label_height, label_width, _ = label.shape
        
        # Cria um array numpy para armazenar os valores inteiros das classes, inicializado com zeros
        label_int = np.zeros((label_height, label_width), dtype=np.int32)

        # Itera sobre cada pixel da máscara
        for i in range(label_height):
            for j in range(label_width):
                # Extrai a cor do pixel atual e a converte em uma tupla
                cor = tuple(label[i, j])
                
                # Verifica se a cor está no mapeamento de classes e a converte para o índice correspondente
                if cor in mapeamento_classes:
                    label_int[i, j] = mapeamento_classes[cor]
                else:
                    # Se a cor não estiver mapeada, atribui a classe "Void" (assumida como a cor preta (0, 0, 0))
                    label_int[i, j] = mapeamento_classes[tuple((0, 0, 0))]  
    else:
        # Se o mapeamento de classes não for fornecido, converte diretamente o rótulo RGB para inteiros
        label_int = np.squeeze(label).astype(np.int32)

    # Retorna a imagem processada e o rótulo convertido em inteiros
    return image, label_int



def carregar_dataset(images_dir, labels_dir, target_size=(224, 224, 3), mapeamento_classes=None, max_images=None):
    # Obtém a lista de arquivos de imagem e rótulo, e as ordena
    image_files = sorted(os.listdir(images_dir))
    label_files = sorted(os.listdir(labels_dir))

    # Verifica se o número de imagens corresponde ao número de rótulos
    if len(image_files) != len(label_files):
        print(f'Número de imagens ({len(image_files)}) não corresponde ao número de rótulos ({len(label_files)})')

    # Limita o número de imagens e rótulos a serem carregados se max_images for especificado
    if max_images is not None:
        image_files = image_files[:max_images]
        label_files = label_files[:max_images]

    # Inicializa listas para armazenar as imagens e rótulos carregados
    images = []
    labels = []

    # Itera sobre os arquivos de imagem e rótulo, carregando-os e processando-os
    for img_file, lbl_file in tqdm(zip(image_files, label_files), total=len(image_files), desc="Carregando dataset"):
        # Constrói os caminhos completos para os arquivos de imagem e rótulo
        img_path = os.path.join(images_dir, img_file)
        lbl_path = os.path.join(labels_dir, lbl_file)
        
        # Carrega e pré-processa a imagem e o rótulo
        img, lbl = carregar_preproc_imagem(img_path, lbl_path, target_size[:2], mapeamento_classes)  # Passa o mapeamento de classes
        
        # Verifica se a imagem carregada tem o número esperado de canais (3 para RGB)
        if img.shape[-1] != target_size[-1]:
            raise ValueError(f"Imagem com canais inesperados: {img.shape[-1]}, esperado: {target_size[-1]}")
        
        # Adiciona a imagem e o rótulo processados às listas
        images.append(img)
        labels.append(lbl)
    
    # Converte as listas de imagens e rótulos em arrays numpy
    return np.array(images), np.array(labels)


def carregar_modelo_unet_treinado(caminho_modelo_unet_treinado):
    # Verifica se o arquivo do modelo existe
    if not os.path.exists(caminho_modelo_unet_treinado):
        # Se o arquivo não for encontrado, imprime uma mensagem de erro e interrompe a execução do notebook
        print(f"Arquivo não encontrado: {caminho_modelo_unet_treinado}")
        sys.exit("Execução interrompida: Arquivo do modelo não encontrado.")
    
    # Carrega o modelo salvo em arquivo no formato .keras
    modelo = keras.models.load_model(caminho_modelo_unet_treinado)
    
    return modelo

def testar_modelo(modelo, imagens_teste):
    # Gera previsões usando o modelo
    previsoes_prob = modelo.predict(imagens_teste, verbose=1)
    
    # Converte as previsões de probabilidades para rótulos de classe
    previsoes = np.argmax(previsoes_prob, axis=-1)  
    
    return previsoes

def criar_colormap(mapeamento_classes):
    # Cria um colormap a partir do mapeamento de cores
    num_classes = len(mapeamento_classes)
    colors = np.zeros((num_classes, 3), dtype=np.float32)

    for color, index in mapeamento_classes.items():
        colors[index] = np.array(color) / 255.0  # Normaliza as cores

    cmap = mcolors.ListedColormap(colors)
    return cmap

def visualizar_previsao(previsao, mapeamento_classes, titulo="Previsão"):
    plt.figure(figsize=(8, 8))
    
    if previsao.ndim == 3 and previsao.shape[-1] > 1:  # Imagem com múltiplos canais
        # Converte a previsão de probabilidade para rótulos de classe
        previsao_rótulos = np.argmax(previsao, axis=-1)
        cmap = criar_colormap(mapeamento_classes)
        plt.imshow(previsao_rótulos, cmap=cmap, vmin=0, vmax=len(mapeamento_classes) - 1)
    elif previsao.ndim == 2:  # Imagem com rótulos de classe
        cmap = criar_colormap(mapeamento_classes)
        plt.imshow(previsao, cmap=cmap, vmin=0, vmax=len(mapeamento_classes) - 1)
    elif previsao.ndim == 3 and previsao.shape[-1] == 3:  # Imagem RGB
        plt.imshow(previsao)
    else:
        raise ValueError("Formato de previsão não suportado para visualização.")
    
    plt.title(titulo)
    plt.axis('off')
    plt.show()


