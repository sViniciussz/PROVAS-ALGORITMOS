from os import system
from time import sleep


def calc_verif_estoque(prod_precos, prod_quant):
    estoque = {produto: {"preco": preco, "quantidade": quantidade} for produto, preco, quantidade in prod_precos}
    total = 0
    todos_dispo = True

    for prod_cliente, quant_cliente in prod_quant:
        if prod_cliente in estoque:
            prod_estoque = estoque[prod_cliente]
            if quant_cliente <= prod_estoque["quantidade"]:
                total += prod_estoque["preco"] * quant_cliente
            else:
                print(f"Não temos quantidade suficiente do produto: {prod_cliente}.\nDisponível: {prod_estoque['quantidade']}\nSolicitado: {quant_cliente}")
                todos_dispo = False
        else:
            print(f"Produto não encontrado no estoque: {prod_cliente}")
            todos_dispo = False
    return total, todos_dispo, estoque

def pedido():
    prod_quant = []
    while True:
        print("Teclado - R$249.99")
        print("Mouse - R$125.99")
        print("Fone - R$75.49")
        print("Monitor - R$654.29")
        print("Gabinete - R$180.00")
        produto = input("Digite o nome do produto ('0' para sair)\n:").lower()
        if produto == '0':
            break
        quantidade = int(input("Informe a quantidade de produtos\n:"))
        prod_quant.append([produto, quantidade])
        system('cls')
    return prod_quant


prod_precos = [
    ["teclado", 249.99, 4],
    ["mouse", 125.99, 7],
    ["fone", 75.49, 5],
    ["monitor", 654.29, 3],
    ["gabinete", 180.00, 3]
]


prod_quant = pedido()
total, todos_dispo, estoque = calc_verif_estoque(prod_precos, prod_quant)

print(f"Total da compra: R${total:.2f}")
print(f"Todos os produtos disponíveis: {'Sim' if todos_dispo else 'Não'}")
