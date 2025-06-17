# Atribuições
numero1 <- 10
15 -> numero2
numero3 = 10

numero1
numero2
numero3

numero4 = numero2 + numero3 * numero1
numero4


# Operaadores relacionais
numero1 == numero2
numero1 == numero3
numero1 != numero2
10 > 5
10 < 5

# Operadores lógicos
10 > 5 & 10 < 7
10 > 5 & 10 < 15
10 > 5 | 10 < 7
10 < 5 | 10 > 15

# ----------------------------------------------------- #

# Strings
nome = "Will"

# ----------------------------------------------------- #

# Criação de vetor
numeros = c(10,20,30,40,50)
numeros

# Resumo dos dados - Estatística Descritiva
summary(numeros)

# ----------------------------------------------------- #

# Estrutura de decisão simples e composta
numero = 10
if (numero <= 10) {
  print(numero)
} else {
  print("Número inválido")
}

numero = 15
if (numero <= 10) {
  print(numero)
} else {
  print("Número inválido")
}

if (numero == 10) {
  print("Numero 10")
} else if(numero == 15) {
  print("Numero 15")
} else {
  print("Numero inválido")
}

# Estrutura de decisão simples e composta - print com cat
numero = 10
if (numero <= 10) {
  cat(numero)
} else {
  cat("Número inválido")
}

numero = 15
if (numero <= 10) {
  cat(numero)
} else {
  cat("Número inválido")
}

if (numero == 10) {
  cat("Numero 10")
} else if(numero == 15) {
  cat("Numero 15")
} else {
  cat("Numero inválido")
}

# Estrutura de repetição
contador = 1
while (contador <= 10) {
  print(contador)
  contador = contador + 1
}

for (i in 1:10) {
  print(i)
}

for (i in numeros) {
  print(i)
}

# Vetores
numeros = c(1,5,72,3,5,23,63,67,3,9,23,17,85,23)
numeros

i = 5
numeros[4]
numeros[i]