
#Vetor
vetor <- c(10, 15, 11, 13)
vetor[2]

#Lista
lista <- list(vetor, 'a', 8)
lista[[1]][2]

#Soma de dois números
numero1 <- 2
numero2 <- 3
resultado <- numero1 + numero2
resultado
#Caso de teste
#Entradas:
#numero1: 2
#numero2: 3
#Saída esperada: 5
#Pré-condições: -
#Procedimento de execução: ordem das entradas (2 e 3)

#Atividade da fixação da Semana 01
#Cálculo da média de hp dos carros com 8 cilindros do mtcars
head(mtcars)
numeroregistros <- nrow(mtcars)
somahp <- 0
quantidadecarros <- 0
#Acessar todos os registros, um por vez
for (indice in 1:numeroregistros){
  #Carros com 8 cilindors
  if (mtcars$cyl[indice] == 8){
    somahp <- somahp + mtcars$hp[indice]
    quantidadecarros <- quantidadecarros + 1
  }
}
mediahp <- somahp/quantidadecarros
mediahp

#Moda para a quantidade de cilindros do mtcars
#Matriz de 2 linhas e 32 colunas
numero_registros <- nrow(mtcars)
matriz <- matrix(Inf, 2, numero_registros)
cilindros <- mtcars$cyl
coluna <- 0
for (i in 1:numero_registros){
  if (cilindros[i] != Inf){
    valor <- cilindros[i]
    linha <- 1
    coluna <- coluna + 1
    matriz[linha,coluna] <- valor
    matriz[(linha + 1),coluna] <- 0
    for (j in i:numero_registros){
      if (cilindros[j] == valor){
        matriz[(linha + 1),coluna] <- matriz[(linha + 1),coluna] + 1
        cilindros[j] <- Inf
      }
    }
  }
}

#Verificar a maior quantidade de elementos
maior <- matriz[2,1]
for (i in 2:numero_registros){
  if ((matriz[2,i] > maior) & (matriz[2,i] != Inf)){
    maior <- matriz[2,i]
  }
}

print(matriz)

#Exibir o elemento ou os elementos que mais aparecem
for (i in 1:numero_registros){
  if (matriz[2,i] == maior){
    print(matriz[1,i])
  }
}

#Moda para a quantidade de cilindros do mtcars
valores <- mtcars$cyl
valores_unicos <- unique(valores)
contagem <- tabulate(match(valores,valores_unicos))
valores_unicos[contagem == max(contagem)]

