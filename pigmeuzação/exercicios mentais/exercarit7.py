#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print("Insira o preço do produto: ")
val=float(input())
val1=(val-(5/100*val))
print(f"Seu novo valor é {val1}")
