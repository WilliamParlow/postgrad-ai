data(USArrests)

aux_max = c(-1,-1,-1,-1,-1)
aux_min = c(-1,-1,-1,-1,-1)

for (i1 in 1:5) {
  for (i2 in 1:50) {
    if (USArrests$UrbanPop[i2] != 0 & aux_min[i1] == -1) {
      aux_min[i1] = i2
      print("----")
      print(i1)
      print(i2)
      print("----")
    } else if (USArrests$UrbanPop[i2] != 0 & USArrests$UrbanPop[aux_min[i1]] > USArrests$UrbanPop[i2]) {
      aux_min[i1] = i2
      print("----")
      print(i1)
      print(i2)
      print("----")
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