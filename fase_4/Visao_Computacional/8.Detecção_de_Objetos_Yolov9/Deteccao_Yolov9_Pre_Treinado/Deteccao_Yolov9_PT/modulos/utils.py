import os
import torch
import subprocess


def verificar_gpu():
    # Verificar a disponibilidade de GPU
    if torch.cuda.is_available():
        dispositivo = '0'
        print(f"GPU selecionada: {torch.cuda.get_device_name(0)}")
    else:
        dispositivo = 'cpu'
        print("GPU não está disponível. CPU selecionada para o processamento.")
    return dispositivo
    

def clonar_yolov9(caminho_origem, caminho_destino):
    # Verifica se o diretório existe e se está vazio
    if not os.path.exists(caminho_destino) or not os.listdir(caminho_destino):
        # Comando para executar a clonagem da yolov9
        command = ['git', 'clone', caminho_origem, caminho_destino]
        try:
            # Para executar o comando git diretamente de um script Python 
            # fora de um notebook, pode usar o módulo subprocess para chamar 
            # comandos do sistema
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            # Exibe a saída do comando
            print(result.stdout)
            print(f"Repositório Yolov9 clonado em {caminho_destino}")
        except subprocess.CalledProcessError as e:
            # Captura o erro se o comando retornar um código de erro
            print(f"Erro ao executar o comando: {e}")
            print(f"Saída do erro: {e.stderr}")
    else:
        print(f"O diretório {caminho_destino} já existe e não está vazio.")


def baixar_modelo_yolov9_treinado(caminho_origem, caminho_destino):
    # Obtém o nome do modelo que será baixado do caminho de origem
    nome_modelo = caminho_origem.split('/')[-1]
    # Constrói o caminho completo do arquivo de destino
    caminho_modelo_destino = os.path.join(caminho_destino, nome_modelo)
    # Verifica se o diretório existe e se está vazio
    if not os.path.exists(caminho_modelo_destino):
        # Comando para executar baixar o modelo
        command = ['wget', '-P', caminho_destino, caminho_origem]
        try:
            # Para executar o comando git diretamente de um script Python 
            # fora de um notebook, pode usar o módulo subprocess para chamar 
            # comandos do sistema
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            # Exibe a saída do comando
            print(result.stdout)
            print(f"Modelo pré-treinado {nome_modelo} foi salvo em {caminho_destino}")
        except subprocess.CalledProcessError as e:
            # Captura o erro se o comando retornar um código de erro
            print(f"Erro ao executar o comando: {e}")
            print(f"Saída do erro: {e.stderr}")
    else:
        print(f"O modelo pré-treinado {nome_modelo} já existe em {caminho_destino}.")







