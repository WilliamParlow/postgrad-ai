# Utilizando os packages do R - mtcars

# Carrega o Dataset
data(mtcars)

# Mostra todos os dados
mtcars

# Lista os 6 primeiros
head(mtcars)

# Obtem o valor da coluna mpg do primeiro item da lista
mtcars$mpg[1]

for (i in 1:32) {
  if (mtcars$mpg[i] > 20) {
    print(mtcars$hp[i])
  }
}
