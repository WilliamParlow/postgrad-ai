# Fator
vetor = c(10,20,30,40,50,50,20,10,20)
summary(vetor)

is.numeric((vetor))

vetor = as.factor(vetor)
summary(vetor)

is.numeric(vetor)
is.factor(vetor)

# Filtro
vogais = c("a", "e", "i", "o", "o", "u")
vogais[-3]
vogais[vogais == "o"]
vogais[vogais == "g"]

# Funções
fatorial = function(numero) {
  i = 1
  multiplicacao = 1
  while (i <= numero) {
    multiplicacao = multiplicacao * i
    i = i + 1
  }
  return(multiplicacao)
}

multiplicacao = fatorial(5)

# Dataframes
nome = c("Joao", "Rafael", "Jose","Maria")
idade = c(30,20,25,31)

df = data.frame(nome,idade)
summary(df)
df

df$nome[1]
df$idade[1]
df[1]
df[1,]
df[1:3,]
df[,1]
df[,2]

df$nova = NA
df

df$nova = NULL
df

# Filtro elabordo
df$nome[df$idade >= 30]

# Dataframe à partir de um arquivo csv
setwd("/home/will/Desktop/postgrad-ai/Estatistica_Aplicada/R/filtros_funcoes_dataframe")
df = read.csv("clima.csv")
df
