import numpy as np

def perceptron_training(training_set, learning_rate=1, max_epochs=100):
    """
    Implementa o algoritmo de treinamento do Perceptron.

    Args:
        training_set (list): Uma lista de tuplas, onde cada tupla é
                             (input_vector, desired_output).
                             input_vector deve ser um array NumPy.
                             O primeiro elemento de cada input_vector tipicamente representa o input de bias (ex: -1).
        learning_rate (float): A taxa de aprendizado (eta), controlando o tamanho do passo das atualizações de peso. Padrão é 1.
        max_epochs (int): O número máximo de épocas de treinamento (passagens completas pelos dados de treinamento).

    Returns:
        numpy.ndarray: O vetor de pesos final após a convergência ou o número máximo de épocas.
        list: Uma lista dos vetores de peso ao final de cada época.
    """

    # --- 1. Inicialização ---
    # Determina o número de features (incluindo o input de bias) a partir do primeiro exemplo de treinamento.
    num_features = training_set[0][0].shape[0]
    
    # Inicializa o vetor de pesos 'w' com todos os zeros.
    # Este vetor incluirá o peso para o termo de bias como seu primeiro elemento.
    weights = np.zeros(num_features) 
    
    print(f"Pesos iniciais (w): {weights}")
    print(f"Taxa de aprendizado (eta): {learning_rate}")
    print("-" * 50)

    # Lista para armazenar o vetor de pesos ao final de cada época para acompanhar o progresso.
    epoch_weights = [] 

    # --- 2. Loop de Treinamento (Épocas) ---
    # Itera através de um número máximo de épocas. Uma época é uma passagem completa sobre todo o conjunto de treinamento.
    for epoch in range(1, max_epochs + 1):
        print(f"\n--- Época {epoch} ---")
        misclassifications = 0 # Contador para exemplos mal classificados na época atual

        # --- 3. Iterar Através dos Exemplos de Treinamento ---
        # Para cada exemplo de treinamento (vetor de input 'x' e sua saída desejada 'd'):
        for i, (x, d) in enumerate(training_set):
            print(f"\n  Processando exemplo de treinamento x({i+1}): {x.T}, saída desejada d({i+1}): {d}")
            print(f"  Pesos atuais (w): {weights}")

            # --- 3a. Calcular a Entrada Líquida (v) ---
            # A entrada líquida 'v' é o produto escalar do vetor de pesos atual 'w' e o vetor de input 'x'.
            # v = w_0*x_0 + w_1*x_1 + ... + w_n*x_n
            v = np.dot(weights, x)
            print(f"  Entrada líquida (v) = w . x = {v:.2f}")

            # --- 3b. Calcular a Saída do Perceptron (y) ---
            # O Perceptron usa uma função de ativação degrau (função sinal).
            # Se v >= 0, a saída é 1. Se v < 0, a saída é -1.
            y = 1 if v >= 0 else -1
            print(f"  Saída do Perceptron (y) = sgn(v) = {y}")

            # --- 3c. Verificar Erro de Classificação e Atualizar Pesos ---
            # Compara a saída do Perceptron 'y' com a saída desejada 'd'.
            if y != d:
                misclassifications += 1 # Incrementa o contador se mal classificado
                
                # Calcula o termo de erro (d - y).
                # Isso será 2 se (d=1, y=-1) ou -2 se (d=-1, y=1).
                error = d - y
                
                # Calcula a mudança nos pesos (delta_w).
                # Delta w = learning_rate * error * input_vector
                delta_w = learning_rate * error * x
                
                # Armazena uma cópia dos pesos antigos para impressão clara.
                weights_old = np.copy(weights) 
                
                # Atualiza os pesos: new_weights = old_weights + delta_w
                weights = weights + delta_w
                
                print(f"  Mal classificado! Desejado: {d}, Previsto: {y}")
                print(f"  Erro (d - y) = {error}")
                print(f"  Delta w (eta * error * x) = {learning_rate} * {error} * {x.T} = {delta_w.T}")
                print(f"  Novos pesos (w) = Pesos antigos ({weights_old.T}) + Delta w ({delta_w.T}) = {weights.T}")
            else:
                # Se classificado corretamente, nenhuma atualização de peso ocorre.
                print(f"  Classificado corretamente. Nenhuma atualização de peso.")
        
        # Armazena o estado atual dos pesos ao final da época.
        epoch_weights.append(np.copy(weights)) 

        print(f"\n--- Fim da Época {epoch} ---")
        print(f"Classificações incorretas na Época {epoch}: {misclassifications}")
        print(f"Pesos ao final da Época {epoch}: {weights}")
        print("-" * 50)

        # --- 4. Verificação de Convergência ---
        # Se nenhuma classificação incorreta ocorreu em toda a época, o algoritmo convergiu.
        # Interrompe o loop, pois o perceptron aprendeu a classificar todos os padrões.
        if misclassifications == 0:
            print(f"\nPerceptron convergiu em {epoch} épocas!")
            break
    else:
        # Se o loop terminar sem interrupção (ou seja, max_epochs alcançado),
        # significa que a convergência não foi alcançada dentro das épocas especificadas.
        print(f"\nPerceptron não convergiu dentro de {max_epochs} épocas.")

    return weights, epoch_weights

def test_perceptron(weights, test_set):
    """
    Testa o modelo Perceptron treinado em um dado conjunto de teste.

    Args:
        weights (numpy.ndarray): O vetor de pesos treinado do Perceptron.
        test_set (list): Uma lista de tuplas, onde cada tupla é
                         (input_vector, desired_output) para teste.

    Returns:
        float: A acurácia do Perceptron no conjunto de teste.
    """
    print("\n" + "="*50)
    print("--- Testando o Modelo Perceptron ---")
    print(f"Usando pesos finais: {weights}")
    
    correct_predictions = 0
    total_predictions = len(test_set)

    for i, (x, d) in enumerate(test_set):
        # 1. Calcular Entrada Líquida
        v = np.dot(weights, x)
        
        # 2. Calcular Saída do Perceptron
        y = 1 if v >= 0 else -1

        print(f"  Exemplo de Teste x({i+1}): {x.T}")
        print(f"    Saída Desejada: {d}, Saída Prevista: {y}")

        if y == d:
            print("    -> Correto!")
            correct_predictions += 1
        else:
            print("    -> Incorreto!")
    
    accuracy = (correct_predictions / total_predictions) * 100
    print(f"\n--- Resultados do Teste ---")
    print(f"Total de Exemplos de Teste: {total_predictions}")
    print(f"Previsões Corretas: {correct_predictions}")
    print(f"Acurácia: {accuracy:.2f}%")
    print("="*50)
    
    return accuracy

# --- Definir o Conjunto de Treinamento ---
# Cada vetor de input 'x' é um array NumPy.
# O primeiro elemento de 'x' é o input de bias (geralmente -1 ou 1, dependendo da convenção).
training_data = [
    (np.array([-1, 0.1, 0.4, 0.7]), 1),   # x(1) com saída desejada d(1) = 1
    (np.array([-1, 0.3, 0.7, 0.2]), -1),  # x(2) com saída desejada d(2) = -1
    (np.array([-1, 0.6, 0.9, 0.8]), -1),  # x(3) com saída desejada d(3) = -1
    (np.array([-1, 0.5, 0.7, 0.1]), 1)    # x(4) com saída desejada d(4) = 1
]

# --- Definir um Conjunto de Teste com Valores Diferentes ---
# É crucial que estes valores não tenham sido usados no treinamento para avaliar a generalização.
test_data = [
    (np.array([-1, 0.0, 0.3, 0.8]), 1),   # Novo ponto que esperamos ser classificado como 1
    (np.array([-1, 0.4, 0.6, 0.3]), -1),  # Novo ponto que esperamos ser classificado como -1
    (np.array([-1, 0.7, 0.8, 0.9]), -1),  # Novo ponto
    (np.array([-1, 0.2, 0.5, 0.0]), 1)    # Novo ponto
]


# --- Executar o Treinamento do Perceptron ---
# A variável 'final_weights' conterá os pesos obtidos ao final do treinamento.
final_weights, all_epoch_weights = perceptron_training(training_data, learning_rate=1)

# --- Testar o Perceptron com o Conjunto de Teste Diferente ---
test_perceptron(final_weights, test_data)

# Opcional: Você pode querer testar também com os dados de treinamento para ver a acurácia de treinamento
# test_perceptron(final_weights, training_data)