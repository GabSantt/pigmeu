#Escreva um programa que pergunte qa quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('Qual a kilometragem percorrida: ');
km=float(input());
print('Quantos dias o carro foi alugado: ');
dia=int(input());
res1=(dia*60);
res2=(km*0.15);
res3=(res1+res2);
print(f"O preço a pagar será {res3}");
