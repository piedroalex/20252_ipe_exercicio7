## EXERCÍCIO 7

1. Qual será o tipo de dado da variável resultado e seu valor após a execução das seguintes linhas de código?
```
a = "5"
b = 3
resultado = int(a) + float(b)
```
2. Escreva o código usando uma f-string para produzir a seguinte saída, utilizando as variáveis fornecidas.
```
nome = "João"
saldo = 1500.758
```
* **Saída esperada: O saldo de João é R$ 1500.76.**
3. Explique por que o seguinte código resultará em um erro de TypeError e sugira a correção.
```
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
soma = num1 + num2
print(soma)
```
4. Qual será o valor e o tipo de w no final da execução?
```
a = "3.5"
b = 2
w = int(float(a)) + b + 0.5
```
5. Determine o valor final da variável check:
```
a = 10
b = 5
c = 15
check = (a > b and c < b) or not (c == 15)
```
6. Crie um programa que solicite ao usuário:
* Duas notas (como float).
* Dois pesos correspondentes (como int).
* O programa deve calcular e imprimir a média ponderada, usando a fórmula:
  - media = ((nota1 x peso1) + (nota2 x peso2)) / (peso1 + peso2)
7. Escreva um programa que receba um valor de tempo em minutos (como int) e o converta para horas e minutos. O programa deve imprimir o resultado formatado. Exemplo: Se o usuário digitar 150 minutos, a saída deve ser "2 horas e 30 minutos".
8. Crie um programa que receba o preço total da compra (float) e o valor pago pelo cliente (float). O programa deve calcular e imprimir o troco devido ao cliente, formatado com duas casas decimais. Utilize um operador aritmético para o cálculo.
9. Crie um programa que peça ao usuário para digitar seu nome, peso e altura. Calcule e imprima o nome e o IMC.
