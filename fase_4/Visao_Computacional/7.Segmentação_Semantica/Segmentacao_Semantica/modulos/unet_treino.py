import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import os
from tqdm import tqdm_notebook as tqdm
import pandas as pd


def carregar_mapeamento_classes(csv_path):
    # Carrega o arquivo CSV contendo o mapeamento de classes e suas cores.
    # O arquivo CSV deve ter colunas 'r', 'g', 'b' para valores RGB e uma coluna 'name' para os nomes das classes.
    df = pd.read_csv(csv_path)
    
    # Extrai os valores das cores RGB das colunas 'r', 'g', 'b' do DataFrame e os armazena em uma matriz NumPy.
    # Cada linha da matriz representa uma cor RGB associada a uma classe.
    cores = df[['r', 'g', 'b']].values
    
    # Extrai os nomes das classes da coluna 'name' do DataFrame e os armazena em um array NumPy.
    # Cada elemento do array representa o nome de uma classe.
    nomes_classes = df['name'].values
    
    # Cria um dicionário de mapeamento de cores para índices de classe.
    # O dicionário é construído com tuplas de cores (RGB) como chaves e índices de classes como valores.
    # `enumerate(cores)` gera uma sequência de pares (índice, cor), onde `i` é o índice da classe e `cor` é a cor RGB.
    mapeamento_classes = {tuple(cor): i for i, cor in enumerate(cores)}
    
    # Retorna o mapeamento de classes (dicionário) e os nomes das classes (array).
    return mapeamento_classes, nomes_classes



def carregar_preproc_imagem(image_path, label_path, target_size=(224, 224), mapeamento_classes=None):
    # Carrega a imagem do caminho especificado e redimensiona para o tamanho alvo.
    # `target_size` deve ser uma tupla (altura, largura) para a imagem.
    image = keras.preprocessing.image.load_img(image_path, target_size=target_size)
    # Converte a imagem carregada em um array NumPy e normaliza os valores de pixel para o intervalo [0, 1].
    image = keras.preprocessing.image.img_to_array(image) / 255.0

    # Carrega o rótulo (label) do caminho especificado e redimensiona para o tamanho alvo.
    # Os rótulos são normalmente armazenados como imagens, onde cada pixel representa uma classe.
    label = keras.preprocessing.image.load_img(label_path, target_size=target_size)
    # Converte o rótulo carregado em um array NumPy e garante que os valores estejam no formato uint8.
    # Isso é feito para garantir que os valores dos pixels estejam no intervalo correto para operações subsequentes.
    label = keras.preprocessing.image.img_to_array(label).astype(np.uint8)

    # Se um mapeamento de classes for fornecido, converte a máscara RGB para índices inteiros de classes.
    # Isso é necessário para preparar os rótulos para treinamento de modelos que exigem índices de classes em vez de valores RGB.
    if mapeamento_classes is not None:
        label_height, label_width, _ = label.shape
        # Inicializa uma matriz de inteiros para armazenar a máscara de rótulo convertida.
        label_int = np.zeros((label_height, label_width), dtype=np.int32)

        # Itera sobre cada pixel na máscara de rótulo para converter a cor RGB em um índice de classe.
        for i in range(label_height):
            for j in range(label_width):
                cor = tuple(label[i, j])  # Obtém a cor RGB do pixel atual.
                if cor in mapeamento_classes:
                    # Se a cor estiver no mapeamento de classes, usa o índice correspondente.
                    label_int[i, j] = mapeamento_classes[cor]
                else:
                    # Se a cor não estiver no mapeamento, atribui a classe "Void" (0, 0, 0) por padrão.
                    label_int[i, j] = mapeamento_classes[tuple((0, 0, 0))]
    else:
        # Se não houver mapeamento de classes, assume que o rótulo já é um array de índices inteiros.
        # `np.squeeze` remove dimensões unitárias, se existirem, para garantir que o formato da máscara seja correto.
        label_int = np.squeeze(label).astype(np.int32)

    # Retorna a imagem normalizada e a máscara de rótulo convertida como arrays NumPy.
    return image, label_int



def carregar_dataset(images_dir, labels_dir, target_size=(224, 224, 3), mapeamento_classes=None, max_images=None):
    # Obtém a lista de arquivos de imagem e rótulo das diretórias fornecidas e ordena-os.
    # Presume-se que os arquivos estejam ordenados de forma correspondente (a imagem e o rótulo devem ser pares).
    image_files = sorted(os.listdir(images_dir))
    label_files = sorted(os.listdir(labels_dir))

    # Verifica se o número de imagens corresponde ao número de rótulos.
    # Se houver uma discrepância, imprime uma mensagem de alerta.
    if len(image_files) != len(label_files):
        print(f'Número de imagens ({len(image_files)}) não corresponde ao número de rótulos ({len(label_files)})')

    # Se um limite máximo de imagens for fornecido, ajusta as listas de arquivos para incluir apenas o número especificado.
    # Isso é útil para testar com um subconjunto do dataset ou para economizar memória.
    if max_images is not None:
        image_files = image_files[:max_images]
        label_files = label_files[:max_images]

    # Inicializa listas para armazenar as imagens e rótulos processados.
    images = []
    labels = []

    # Itera sobre os pares de arquivos de imagem e rótulo.
    # `tqdm` é usado para exibir uma barra de progresso durante o carregamento.
    for img_file, lbl_file in tqdm(zip(image_files, label_files), total=len(image_files), desc="Carregando dataset"):
        # Constrói os caminhos completos para as imagens e rótulos.
        img_path = os.path.join(images_dir, img_file)
        lbl_path = os.path.join(labels_dir, lbl_file)
        
        # Carrega e pré-processa a imagem e o rótulo usando a função `carregar_preproc_imagem`.
        # `target_size[:2]` ajusta o tamanho da imagem e rótulo para as dimensões desejadas.
        # `mapeamento_classes` é usado para converter a máscara de rótulo RGB em índices de classe.
        img, lbl = carregar_preproc_imagem(img_path, lbl_path, target_size[:2], mapeamento_classes)
        
        # Verifica se o número de canais da imagem corresponde ao esperado.
        # Se não corresponder, levanta um erro com uma mensagem apropriada.
        if img.shape[-1] != target_size[-1]:
            raise ValueError(f"Imagem com canais inesperados: {img.shape[-1]}, esperado: {target_size[-1]}")
        
        # Adiciona a imagem e o rótulo às listas.
        images.append(img)
        labels.append(lbl)
    
    # Converte as listas de imagens e rótulos em arrays NumPy e retorna.
    # Isso é útil para passar os dados para modelos de treinamento e avaliação.
    return np.array(images), np.array(labels)


def obter_modelo_unet(input_shape, num_classes):
    # Define a entrada do modelo com a forma especificada
    inputs = keras.Input(shape=input_shape, name="input_image")

    # **Encoder:**
    # Carrega o MobileNetV2 pré-treinado como encoder, utilizando a entrada definida acima
    # O MobileNetV2 é usado para extrair características da imagem e reduzir sua resolução.
    # A opção include_top=False significa que não carregamos a parte final da rede (classificador),
    # apenas as camadas convolucionais que realizam a extração de características.
    encoder = keras.applications.MobileNetV2(input_tensor=inputs, weights="imagenet", include_top=False)
    
    # Congela as camadas do encoder para que seus pesos não sejam ajustados durante o treinamento
    for layer in encoder.layers:
        layer.trainable = False
    
    # Obtém a saída do encoder, que será usada como entrada para o decoder
    encoder_output = encoder.output
    
    # Define o número de camadas UpSampling necessárias para restaurar a resolução original
    # O MobileNetV2 reduz a resolução da imagem original em 32 vezes.
    # Para restaurar a resolução original (224x224), aplicamos 5 camadas de UpSampling2D.
    upsampling_layers = 5
    x = encoder_output

    # **Decoder:**
    # Aplica UpSampling2D e convoluções para aumentar a resolução da imagem gradualmente
    for _ in range(upsampling_layers):
        # Aumenta a resolução da imagem pela multiplicação por 2 nas dimensões espaciais
        x = keras.layers.UpSampling2D((2, 2))(x)
        # Aplica uma convolução para refinar as características
        x = keras.layers.Conv2D(64, (3, 3), padding="same")(x)
        # Normaliza a saída da convolução para acelerar o treinamento e melhorar a estabilidade
        x = keras.layers.BatchNormalization()(x)
        # Aplica a função de ativação ReLU para introduzir não-linearidades
        x = keras.layers.Activation("relu")(x)

    # Camada de saída:
    # Aplica uma convolução com 1x1 para obter as previsões finais para cada classe
    # A camada de ativação softmax é usada para obter probabilidades de classe para cada pixel
    x = keras.layers.Conv2D(num_classes, (1, 1), padding="same")(x)
    x = keras.layers.Activation("softmax")(x)

    # Cria o modelo final com a entrada definida e a saída gerada
    model = keras.Model(inputs, x)

    # Exibe um resumo do modelo para ver a arquitetura e os parâmetros
    model.summary()
    return model



def compilar_modelo_unet(modelo, metrica, learning_rate, num_classes):
    # Define o otimizador Adam para ser usado durante o treinamento.
    # O parâmetro `learning_rate` define a taxa de aprendizado para ajustar os pesos do modelo.
    otimizador = keras.optimizers.Adam(learning_rate=learning_rate)

    # Define a função de perda (loss) com base no número de classes.
    # A função de perda é usada para calcular o erro entre as previsões do modelo e os rótulos verdadeiros.
    if num_classes > 1:
        # Para problemas de classificação com múltiplas classes (classificação multiclasses):
        # Usa SparseCategoricalCrossentropy, que é adequada quando as classes são representadas por índices inteiros.
        # `from_logits=True` indica que as previsões do modelo são logits e devem ser convertidas para probabilidades.
        loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    else:
        # Para problemas de classificação binária (apenas duas classes):
        # Usa BinaryCrossentropy, que é adequada para classificações binárias.
        # `from_logits=True` indica que as previsões do modelo são logits e devem ser convertidas para probabilidades.
        loss = keras.losses.BinaryCrossentropy(from_logits=True)

    # Compila o modelo especificando o otimizador, a função de perda e as métricas para avaliação.
    # `metrics` é uma lista de métricas para monitorar durante o treinamento e a avaliação do modelo.
    modelo.compile(optimizer=otimizador, loss=loss, metrics=[metrica])
    
    return modelo


def treinar_modelo_unet(modelo, imagens_treino, labels_treino, imagens_validacao, labels_validacao, num_epocas, caminho_checkpoints, lista_callbacks, batch_size=32):
    # Treinamento do modelo utilizando os dados de treinamento para o aprendizado
    # e os dados de validação para auxiliar no cálculo dos pesos do modelo a cada época.
    # A função também executa as funções presentes na lista de callbacks.
    historico = modelo.fit(
        imagens_treino, labels_treino,
        batch_size=batch_size,
        epochs=num_epocas,
        verbose=1,
        validation_data=(imagens_validacao, labels_validacao),
        callbacks=lista_callbacks
    )
    
    # Carrega os melhores pesos armazenados nos checkpoints
    modelo.load_weights(caminho_checkpoints)
    
    return modelo, historico


def plot_historico(historico, metrica, caminho_resultados):
    # plota a evolução da acurácia e loss ao longo das épocas de treinamento
    plt.figure(1)
    # accuracy
    plt.subplot(211)
    plt.plot(historico.history[metrica])
    plt.plot(historico.history['val_'+metrica])
    plt.title('Acurácia do Modelo')
    plt.ylabel('Acurácia')
    plt.xlabel('Época')
    plt.legend(['Treinamento', 'Validação'], loc='lower right')
    # loss
    plt.subplot(212)
    plt.plot(historico.history['loss'])
    plt.plot(historico.history['val_loss'])
    plt.title('Perda do Modelo')
    plt.ylabel('Perda')
    plt.xlabel('Época')
    plt.legend(['Treinamento', 'Validação'], loc='upper right')
    plt.tight_layout()
    plt.savefig(caminho_resultados+'Historico_Treinamento', dpi=300)
    print(f'\nHistórico salvo na pasta: {caminho_resultados}\n')
    plt.show()


def salvar_modelo(modelo, caminho_dest_modelo):
    modelo.save(caminho_dest_modelo)
    print(f'\nO modelo treinado foi salvo na pasta {caminho_dest_modelo}\n')


def obter_checkpoint_callback(caminho_checkpoints, metrica='val_accuracy'):
    # Criação do callback para pontos de verificação
    checkpoint_callback = keras.callbacks.ModelCheckpoint(
        filepath=caminho_checkpoints,
        save_weights_only=True,
        monitor=metrica,
        mode='max',
        save_best_only=True)
    return checkpoint_callback

def obter_log_callback(caminho_log):
    # Criação do callback para log dos valores de acurácia e loss a cada época
    log_callback = keras.callbacks.CSVLogger(caminho_log, separator=',', append=False)
    return log_callback


def obter_reduce_lr_callback():
    # Reduz a tx de aprend se a mudança for menor do q o factor em val_los
    reduce_lr_callback = keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=1, #quantidade de épocas que espera para reduzir a tx de aprend
        verbose=1
    )
    return reduce_lr_callback

def obter_early_stop_callback():
    # Para o treinamento se val_loss parar de diminuir por 3 épocas consecutivas
    early_stop = keras.callbacks.EarlyStopping(monitor = 'val_loss',
                                                    mode = 'auto',
                                                    patience = 5,
                                                    verbose = 1,
                                                    restore_best_weights = True)
    return early_stop



