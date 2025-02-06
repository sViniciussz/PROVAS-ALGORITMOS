import os
import time

def verificar_primo(num): 
    if num<=1:
        return False
    for i in range (2, int(num**0.5)+1):
        if num %i ==0:
            return False
    return True

def verificar_gold(n1): #verificar goldBach
    primos=0
    for i in range (2,n1):
        if verificar_primo(i) and verificar_primo(n1-i):
            primo=i
            return primo, n1-primo


cont=0
while cont<10: #quantidade de vezes do numero informado
    num=int(input("Informe um número: "))
    if num %2==0 and num>2: #verificar se é par e >2
        primo, primo1= verificar_gold(num)
        if primo !=0:
            print(f"{num} é {primo} + {primo1}")
        else:
            (f"Não foi possível encontrar para {num}")
        cont+=1
        time.sleep(3)
        os.system("cls")
    else:
        print("O número informado precisa ser par e maior que 2!")
        print()




