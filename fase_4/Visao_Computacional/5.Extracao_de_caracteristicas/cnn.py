import cv2
import numpy as np
from tensorflow import keras
from tqdm.notebook import tqdm  
import logging
import os
# Define o nível de log da Tensorflow para 3 e ignora os demais níveis
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 (INFO), 1 (WARNING), 2 (ERROR), 3 (FATAL)

def ajustar_canais_imagem(imagem):
    """
    Ajusta o número de canais de uma imagem para garantir que tenha 3 canais (RGB) para ser usada como entrada em uma CNN.
    
    Parâmetros:
    - imagem (np.ndarray): A imagem que pode ter 1, 3 ou 4 canais.
    
    Retorno:
    - imagem_rgb (np.ndarray): A imagem ajustada para ter 3 canais (RGB).
    """
    # Verifica o número de canais
    if len(imagem.shape) == 2:
        # Imagem em escala de cinza, converte para 3 canais RGB
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_GRAY2RGB)
    elif len(imagem.shape) == 3 and imagem.shape[2] == 4:
        # Imagem com 4 canais (BGRA), converte para 3 canais RGB
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGRA2RGB)
    elif len(imagem.shape) == 3 and imagem.shape[2] == 3:
        # Imagem já tem 3 canais RGB
        imagem_rgb = imagem
    else:
        # Número inesperado de canais
        raise ValueError(f"Número inesperado de canais: {imagem.shape[2]}")
    
    return imagem_rgb


def preprocessar_imagens(imagens_memoria, target_size=(224, 224)):
    """
    Pré-processa uma lista de imagens carregadas em memória, ajustando-as ao formato necessário para a MobileNet.

    Parâmetros:
    - imagens_memoria (list): Lista contendo as imagens carregadas em memória.
    - target_size (tuple): Tamanho alvo das imagens para o modelo (default: (224, 224)).

    Retorno:
    - imagens_preprocessadas (list): Lista contendo as imagens pré-processadas.
    """
    # Lista para armazenar as imagens pré-processadas
    imagens_preprocessadas = []  
    
    # Barra de progresso para monitorar o pré-processamento
    for imagem in tqdm(imagens_memoria, desc="Pré-processando imagens", unit="imagem"):
        # Ajusta o número de canais da imagem
        imagem_rgb = ajustar_canais_imagem(imagem)
        # Redimensiona a imagem para o tamanho alvo
        imagem_redimensionada = cv2.resize(imagem_rgb, target_size)
        
        # Converte a imagem para um array do tipo float32, pois posterioremente,
        # os valores dos pixels serão convertidos de para o intervalo [-1,1]
        img_array = np.array(imagem_redimensionada, dtype=np.float32)
        
        # Adiciona uma nova dimensão (batch size)
        # Isso é feito porque os modelos da Keras esperam que as entradas estejam
        # no formato de lotes (batch), mesmo que seja apenas uma única imagem.
        # A dimensão adicionada representa o número de amostras no lote 
        # axis=0 indica que a nova dimensão será adicionada no início do array
        # Forma Original: (224, 224, 3)
        # Forma após expansão: (1, 224, 224, 3)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Aplica o pré-processamento necessário para o MobileNet V2
        # A função preprocess_input normaliza os valores dos pixels da imagem
        # para o intervalo esperado pelo MobileNet V2, geralmente ajustando os valores 
        # para o intervalo [-1, 1], que é compatível com os pesos pré-treinados do modelo.
        preproc_img = keras.applications.mobilenet_v2.preprocess_input(img_array)

        
        # Armazena a imagem pré-processada
        imagens_preprocessadas.append(preproc_img)
    # Converte a lista para um único array e retorna
    return np.vstack(imagens_preprocessadas)


def obter_modelo_cnn():
    # Define a forma da imagem de entrada, que deve ser 
    # 224x224 pixels com 3 canais (RGB)
    forma_img = (224,224,3)
    
    # Carrega o modelo MobileNetV2 pré-treinado com os pesos do ImageNet
    # include_top=False significa que a camada de classificação final (dense) 
    # não será incluída e a saída será a camada anterior à camada densa. 
    # Na MobileNetV2 a saída será a camada 'global_average_pooling2d'
    modelo_base = keras.applications.MobileNetV2(input_shape=forma_img,
                                                 weights='imagenet',
                                                 include_top=False)
    
    # Exibe um resumo do modelo base para visualizar a arquitetura
    modelo_base.summary()
    
    # Seleciona a última camada do modelo base. Neste caso, como foi utilizado 
    # include_top=False a última camada do modelo base é a camada 
    # 'global_average_pooling2d'. 
    # Saída da camada: um vetor de características globais da imagem de 
    # tamanho 1280. A forma da saída é (None, 1280), 
    # As CNNs processam as imagens em lotes (conjuntos de amostras)
    # None: indica um tamanho de lote flexível
    camada_saida = modelo_base.output

    # Cria um novo modelo que começa com as entradas do MobileNetV2 original
    # e termina na camada anterior à  camada densa para a 
    # extração de características.
    modelo = keras.Model(inputs=modelo_base.input, outputs=camada_saida)
    
    # Exibe um resumo do modelo modificado para verificar a nova estrutura
    modelo.summary()
    
    # Retorna o modelo que agora pode ser usado para extrair características das imagens
    return modelo


def extrair_caracteristicas_cnn(imagens, modelo_cnn):
    """
    Extrai características das imagens usando um modelo instanciado previamente através da função obter_modelo_cnn.
    Assim, o mesmo modelo utilizado para extrair características do conjunto de treinamento será utilizado para extrair características do conjunto  de teste.

    Parâmetros:
    - imagens (list): Lista contendo as imagens pré-processadas.
    - modelo (keras.Model): O modelo CNN usado para extrair características.

    Retorno:
    - caracteristicas_cnn (np.ndarray): Características extraídas das imagens.
    """
    # Pré-processa as imagens para adequá-las à entrada do modelo MobileNetV2
    imagens_preprocessadas = preprocessar_imagens(imagens)
    
    
    # Usa o modelo CNN para prever (ou extrair) as características das imagens pré-processadas
    # As características são extraídas em lotes (batch_size=32) para eficiência
    caracteristicas_cnn = modelo_cnn.predict(imagens_preprocessadas, batch_size=32)
    
    # Converte as características extraídas em um array NumPy e as retorna
    return np.array(caracteristicas_cnn)




