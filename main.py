import os


n = int(input("Digite um numero:"))
os.system('clear')
if(n > 0):
  print("O numero é positivo")
elif(n < 0):
  print("O número é negativo")
elif(n == 0):
  print("O número é igual a zero")