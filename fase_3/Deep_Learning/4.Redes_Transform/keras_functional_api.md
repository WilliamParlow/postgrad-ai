# O que significa `()()` em Keras

Essa sintaxe é o padrão da **Keras Functional API** e envolve dois conceitos distintos:

## Primeira parte `(...)` — instancia a camada

```python
layers.Embedding(input_dim=max_features, output_dim=emb_dims)
```

Isso cria um **objeto** da camada `Embedding`, configurando seus parâmetros (tamanho do vocabulário, dimensão do embedding, etc.). A camada existe, mas ainda não processou nenhum dado.

## Segunda parte `(inputs)` — executa a camada (forward pass)

```python
...(inputs)
```

Isso **chama o objeto** recém-criado passando um tensor como entrada. Em Python, quando uma classe implementa o método `__call__`, você pode chamar instâncias dela como se fossem funções. No Keras, esse `__call__` conecta a camada ao grafo computacional e define o fluxo dos dados.

---

## Equivalente explícito

Fazendo em duas linhas separadas:

```python
# Linha 1: instancia a camada
embedding_layer = layers.Embedding(input_dim=max_features, output_dim=emb_dims)

# Linha 2: aplica sobre a entrada
token_emb = embedding_layer(inputs)
```

O `()()` é apenas um atalho que faz isso numa linha só, descartando a referência intermediária à camada — o que é comum quando você não precisa reutilizar aquela camada em outro lugar do modelo.

---

## Por que o Keras funciona assim?

Na **Functional API** do Keras, você constrói o modelo descrevendo explicitamente o fluxo de tensores entre camadas. Cada camada é um objeto que transforma tensores, então faz sentido separar a *criação* da camada da *aplicação* dela sobre os dados.

```python
inputs  = keras.Input(shape=(maxlen,))

x       = layers.Embedding(input_dim=max_features, output_dim=emb_dims)(inputs)
x       = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(1, activation='sigmoid')(x)

model = keras.Model(inputs, outputs)  # define o modelo pelo fluxo
```

Cada `()()` é essencialmente: **"crie esta camada e conecte-a a este tensor"**.

# Exemplo de código de uma implementação do \_\_call\_\_

```python
class Multiplicador:
    def __init__(self, fator):
        self.fator = fator  # configurado na instanciação

    def __call__(self, valor):
        return valor * self.fator  # executado ao "chamar" o objeto


# Usando com ()()
resultado = Multiplicador(fator=3)(10)
print(resultado)  # 30

# Equivalente explícito
camada = Multiplicador(fator=3)
resultado = camada(10)
print(resultado)  # 30
```