preco_total = float(input("Digite o preço total da compra: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))
troco = valor_pago - preco_total
print(f"O troco a ser devolvido é de R$ {troco:.2f}")