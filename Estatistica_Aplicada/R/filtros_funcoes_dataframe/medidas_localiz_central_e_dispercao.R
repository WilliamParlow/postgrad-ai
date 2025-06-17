
vetor = c(10,20,10,20,30,40)
summary(vetor)

# Média
mean(vetor)

# Mediana
median(vetor)

# Valor Minimo
min(vetor)

# Valor Máximo
max(vetor)

median(mtcars$hp)
mean(mtcars$hp)

##### Dispersão

# Variância
var(vetor)
# ou
# subtrair cada item do vetor pela média e dividir por n - 1
# divsão por n - 1 -> Quando amostra
# divsão por n -> Quando população
resultado = ((10 - 21.66667)^2 + (20 - 21.66667)^2 + (10 - 21.66667)^2 + (20 - 21.66667)^2 + (30 - 21.66667)^2 + (40 - 21.66667)^2) / (length(vetor) - 1)
resultado

# Desvio padrão
sd(vetor)
sqrt(sum(vetor))
