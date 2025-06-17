# Dataset - É uma porção de dados brutos de uma entidade maior, sendo estes os 
# dados base para exercer operações e obter resultados estatísticos tanto 
# descritivos como inferenciais, que agregue valor à uma determinada aplicação
# dos dados processados.

# -------------------------- Script Atividade 1 ------------------------------ #

# Carregar o dataset de carros
data(mtcars)

# Apresentar lista de dados do dataset
mtcars

# Acumuladora de hp
media_hp = 0
contador = 0

for (i in 1:32) {
  if (mtcars$cyl[i] == 8) {
    media_hp = media_hp + mtcars$hp[i]
    contador = contador + 1
  }
}

print("A média de HP do total de carros de 8 cilindros é: ")
print(media_hp / contador)
