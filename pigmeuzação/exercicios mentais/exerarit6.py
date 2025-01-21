#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
print("Insira a altura da parede:")
alt=int(input())
print("Insira a largura da parede:")
lar=int(input())
area=(alt*lar)
tinta=(area/2)
print(f"A área é igual {area}, sendo necessário {tinta} litros de Tinta")
