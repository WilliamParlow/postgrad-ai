# Processo de criação e aplicação de Redes Neurais

Este conteúdo apresenta um detalhamento de diferentes possibilidades de etapas que podem ser seguidas desde o tratamento inicial dos dados de um dataset até o processo de treinamento e aplicação de uma rede neural desenvolvida. O objetivo é fornecer uma visão abrangente das fases envolvidas, destacando alternativas e boas práticas em cada etapa do fluxo de trabalho, além de ser uma boa base de consulta para auxiliar no processo de etapas no desenvolvimento de uma rede neural.


## Etapas do Processo de Redes Neurais

### Guia 1: Simples e direto com apenas normalização dos dados do dataset, aplicando o algoritmo de redes neurais Perceptron

Esta é a maneira mais simples e direta para a criação do dataset normalizado, e utiliza-lo para o processo de treinamento e teste da rede neural.

  1. **Determinar o dataset que será utilizado:** Determinar o dataset que será utilizado para aplicar o algoritmo de redes neurais, seja ele um dataset encontrado em sites especializados, ou dados de qualquer origem útil do dia a dia ou do trabalho que seja possível trata-los como um dataset.

  2. **Separar a classe e valores dos dados do dataset:** Identificar e separar os dados de classe e valores que serão utilizados no treinamento e teste da rede neural. A classe é o rótulo ou a saída esperada, enquanto os valores são as características ou atributos que serão usados para prever essa classe.

  3. **Normalizar os dados do dataset:** Aplicar uma normalização nos dados do dataset, para que os valores estejam em uma escala adequada para o treinamento da rede neural. Isso pode incluir técnicas como Min-Max Scaling.

  4. **Pré-Processamento: Normalizar os rótulos de classe do dataset:** Aplicar uma normalização nos rótulos de classe do dataset, se necessário, para garantir que estejam em uma escala adequada para o treinamento da rede neural. Ex: Para determinar se sim ou não, pode-se utilizar 0 e 1, ou -1 e 1, dependendo do algoritmo de rede neural utilizado.

  5. **Dividir o dataset em conjuntos de treinamento e teste:** Dividir o dataset em dois conjuntos: um para treinamento da rede neural e outro para teste. Isso é importante para avaliar o desempenho do modelo em dados não vistos.

  6. **Treinar a rede neural:** Utilizar o conjunto de treinamento para treinar a rede neural, ajustando os pesos e viéses com base nos dados de entrada e saída esperada.

  7. **Testar a rede neural:** Avaliar o desempenho da rede neural utilizando o conjunto de teste, verificando sua capacidade de generalização para novos dados.

  8. **Ajustar hiperparâmetros:** Se necessário, ajustar os hiperparâmetros da rede neural, como taxa de aprendizado, número de camadas e neurônios, para melhorar o desempenho do modelo.

  9. **(Opcional) Apresentar os resultados:** Apresentar os resultados obtidos com a rede neural, como acurácia, precisão, recall e F1-score, para avaliar o desempenho do modelo.




### Guia 2: Análise dos dados do dataset, determinação dos melhores campos correlacionados e padronização dos dados, aplicando o algoritmo de redes neurais Perceptron Multi Camadas (MLP)

Este guia apresenta um processo mais detalhado e abrangente, que inclui a análise dos dados do dataset, a determinação dos melhores campos correlacionados e a padronização dos dados com StandardScaler antes de aplicar o algoritmo de redes neurais Perceptron Multi Camadas (MLP).

1. **Analisar os dados do dataset:** Realizar uma análise exploratória dos dados para entender suas características, distribuição e possíveis correlações entre os atributos. Isso pode incluir a visualização de gráficos, estatísticas descritivas e a identificação de outliers.

2. **Determinar os melhores campos correlacionados:** Com base na análise dos dados, identificar quais atributos têm maior correlação com a variável alvo. Isso pode ajudar a reduzir a dimensionalidade do dataset e melhorar o desempenho do modelo. Desta maneira, pode-se remover as colunas que não possuem correlação com a variável alvo, criando um novo dataframe com apenas os atributos mais relevantes que serão utilizados no treinamento e teste da rede neural.

3. **Separar a classe e valores dos dados do dataset:** Identificar e separar os dados de classe e valores que serão utilizados no treinamento e teste da rede neural. A classe é o rótulo ou a saída esperada, enquanto os valores são as características ou atributos que serão usados para prever essa classe.

4. **Pré-Processamento: Padronizar os dados do dataset:** Utilizar o StandardScaler para padronizar os dados do dataset, garantindo que todos os atributos tenham média zero e desvio padrão um. Isso é importante para que a rede neural aprenda de forma eficiente, especialmente quando os atributos têm escalas diferentes.

5. **Pré-Processamento: Normalizar os rótulos de classe do dataset:** Aplicar uma normalização nos rótulos de classe do dataset, se necessário, para garantir que estejam em uma escala adequada para o treinamento da rede neural. Ex: Para determinar se sim ou não, pode-se utilizar 0 e 1, ou -1 e 1, dependendo do algoritmo de rede neural utilizado.

6. **Dividir o dataset em conjuntos de treinamento e teste:** Dividir o dataset em dois conjuntos: um para treinamento da rede neural e outro para teste. Isso é importante para avaliar o desempenho do modelo em dados não vistos.

7. **Treinar a rede neural:** Utilizar o conjunto de treinamento para treinar a rede neural Perceptron Multi Camadas (MLP), ajustando os pesos e viéses com base nos dados de entrada e saída esperada. O MLP é uma arquitetura de rede neural que pode capturar relações não lineares entre os atributos.

8. **Testar a rede neural:** Avaliar o desempenho da rede neural utilizando o conjunto de teste, verificando sua capacidade de generalização para novos dados.

9. **Ajustar hiperparâmetros:** Se necessário, ajustar os hiperparâmetros da rede neural, como taxa de aprendizado, número de camadas e neurônios, para melhorar o desempenho do modelo.

10. **(Opcional) Apresentar os resultados:** Apresentar os resultados obtidos com a rede neural, como acurácia, precisão, recall e F1-score, para avaliar o desempenho do modelo.




### Guia 3: Análise dos dados do dataset, determinação dos melhores campos correlacionados e padronização dos dados, aplicando o algoritmo de redes neurais Regressor Perceptron Multi Camadas para previsão de valores

Este guia apresenta um processo mais detalhado e abrangente, que inclui a análise dos dados do dataset, a determinação dos melhores campos correlacionados e a padronização dos dados com StandardScaler antes de aplicar o algoritmo de redes neurais Regressor Perceptron Multi Camadas (MLPRegressor).

1. **Analisar os dados do dataset:** Realizar uma análise exploratória dos dados para entender suas características, distribuição e possíveis correlações entre os atributos. Isso pode incluir a visualização de gráficos, estatísticas descritivas e a identificação de outliers.

2. **Determinar os melhores campos correlacionados:** Com base na análise dos dados, identificar quais atributos têm maior correlação com a variável alvo. Isso pode ajudar a reduzir a dimensionalidade do dataset e melhorar o desempenho do modelo. Desta maneira, pode-se remover as colunas que não possuem correlação com a variável alvo, criando um novo dataframe com apenas os atributos mais relevantes que serão utilizados no treinamento e teste da rede neural.

3. **Separar a classe e valores dos dados do dataset:** Identificar e separar os dados de classe e valores que serão utilizados no treinamento e teste da rede neural. A classe é o rótulo ou a saída esperada, enquanto os valores são as características ou atributos que serão usados para prever essa classe.

4. **Pré-Processamento: Padronizar os dados do dataset:** Utilizar o StandardScaler para padronizar os dados do dataset, garantindo que todos os atributos tenham média zero e desvio padrão um. Isso é importante para que a rede neural aprenda de forma eficiente, especialmente quando os atributos têm escalas diferentes.

5. **Pré-Processamento: Normalizar os rótulos de classe do dataset:** Aplicar uma normalização nos rótulos de classe do dataset, se necessário, para garantir que estejam em uma escala adequada para o treinamento da rede neural. Ex: Para prever valores contínuos, pode-se utilizar a normalização Min-Max Scaling.

6. **Dividir o dataset em conjuntos de treinamento e teste:** Dividir o dataset em dois conjuntos: um para treinamento da rede neural e outro para teste. Isso é importante para avaliar o desempenho do modelo em dados não vistos.

7. **Treinar a rede neural:** Utilizar o conjunto de treinamento para treinar a rede neural Regressor Perceptron Multi Camadas (MLPRegressor), ajustando os pesos e viéses com base nos dados de entrada e saída esperada. O MLPRegressor é uma arquitetura de rede neural que pode capturar relações não lineares entre os atributos e prever valores contínuos.

8. **Testar a rede neural:** Avaliar o desempenho da rede neural utilizando o conjunto de teste, verificando sua capacidade de generalização para novos dados.

9. **Ajustar hiperparâmetros:** Se necessário, ajustar os hiperparâmetros da rede neural, como taxa de aprendizado, número de camadas e neurônios, para melhorar o desempenho do modelo.

10. **(Opcional) Apresentar os resultados:** Apresentar os resultados obtidos com a rede neural, como erro médio absoluto, erro quadrático médio e R², para avaliar o desempenho do modelo na previsão de valores contínuos.






## Glosário

### Termos e Conceitos

- **Dataset:** Conjunto de dados estruturados que serão utilizados para treinar e testar a rede neural.
- **Classe:** Rótulo ou saída esperada que a rede neural deve prever com base nos dados de entrada.
- **Valores:** Características ou atributos dos dados que serão usados para prever a classe.
- **Normalização:** Processo de ajustar os valores dos dados para uma escala comum, facilitando o treinamento da rede neural.
- **Padronização:** Processo de ajustar os dados para que tenham média zero e desvio padrão um, melhorando a eficiência do aprendizado da rede neural.
- **StandardScaler:** Ferramenta do scikit-learn utilizada para padronizar os dados.
- **MLP (Multi-Layer Perceptron):** Arquitetura de rede neural composta por múltiplas camadas de neurônios, capaz de capturar relações não lineares entre os atributos.
- **MLPRegressor:** Algoritmo de regressão baseado em MLP, utilizado para prever valores contínuos.
- **Hiperparâmetros:** Parâmetros que controlam o comportamento do modelo, como taxa de aprendizado, número de camadas e neurônios.
- **Acurácia:** Medida de quão bem o modelo está prevendo as classes corretas.
- **Precisão:** Proporção de previsões corretas entre as previsões feitas pelo modelo.
- **Recall:** Proporção de previsões corretas entre as instâncias reais de uma classe.
- **F1-score:** Média harmônica entre precisão e recall, utilizada para avaliar o desempenho do modelo em problemas de classificação desbalanceada.
- **Outliers:** Valores que se desviam significativamente do padrão dos dados, podendo afetar o desempenho do modelo.
- **Análise Exploratória de Dados (EDA):** Processo de explorar e visualizar os dados para entender suas características, distribuição e possíveis correlações.
- **Correlação:** Medida estatística que indica a relação entre duas variáveis, podendo ser positiva, negativa ou inexistente.
- **Normalização x Padronização:** Normalização ajusta os dados para uma escala comum (0 a 1), enquanto padronização ajusta os dados para que tenham média zero (média removida) e desvio padrão a uma unidade. Modelos que não são baseados em Arvores de Decisão, como Redes Neurais, geralmente se beneficiam mais da padronização dos dados, pois isso ajuda a acelerar o processo de convergência durante o treinamento.