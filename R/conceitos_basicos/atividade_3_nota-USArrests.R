data(USArrests)

# Vetores auxiliares para ordenação
aux_max = c(-1,-1,-1,-1,-1)
aux_min = c(-1,-1,-1,-1,-1)

# Estrutura de repetição para efetuar a ordenação das cidades mais populosas e
# menos populosas
for (i1 in 1:5) {
  for (i2 in 1:50) {
    if (USArrests$UrbanPop[i2] != 0 & aux_min[i1] == -1) {
      aux_min[i1] = i2
    } else if (USArrests$UrbanPop[i2] != 0 & USArrests$UrbanPop[aux_min[i1]] > USArrests$UrbanPop[i2]) {
      aux_min[i1] = i2
    }
    if (USArrests$UrbanPop[i2] != 0 & aux_max[i1] == -1) {
      aux_max[i1] = i2
    } else if (USArrests$UrbanPop[aux_max[i1]] < USArrests$UrbanPop[i2]) {
      aux_max[i1] = i2
    }
  }
  USArrests$UrbanPop[aux_min[i1]] = 0
  USArrests$UrbanPop[aux_max[i1]] = 0
}

# Realiza o print das médias de assassinatos, assalto e estupro para as cidades 
# de maior população
assassinato = 0
assalto = 0
estupro = 0
print ("Média para cidades com MAIOR população: ")
for (i in aux_max) {
  assassinato = assassinato + USArrests$Murder[i]
  assalto = assalto + USArrests$Assault[i]
  estupro = estupro + USArrests$Rape[i]
}

cat("Assassinato: ", assassinato / 5)
cat("Assalto: ", assalto / 5)
cat("Estupro: ", estupro / 5)

# Realiza o print das médias de assassinatos, assalto e estupro para as cidades 
# de menor população
assassinato = 0
assalto = 0
estupro = 0
print ("Média para cidades com MENOR população: ")
for (i in aux_min) {
  assassinato = assassinato + USArrests$Murder[i]
  assalto = assalto + USArrests$Assault[i]
  estupro = estupro + USArrests$Rape[i]
}

cat("Assassinato: ", assassinato / 5)
cat("Assalto: ", assalto / 5)
cat("Estupro: ", estupro / 5)