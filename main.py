from Luis import *
from Vini import *

def recebe_int(texto, erro="Valor inválido!"):
    while True:
        try:
            return float(input(texto))
        except:
            print(erro)

while True:
    operacao = input("Qual operação deseja fazer?\n> ").replace('*', 'x')

    num1 = recebe_int("Digite o primeiro número\n> ")
    num2 = recebe_int("Digite o segundo número\n> ")

    match operacao:
        case "+":
            print(f"Resultado: {soma(num1, num2)}")
        case "-":
            print(f"Resultado: {subtracao(num1, num2)}")
        case "x":
            print(f"Resultado: {x(num1, num2)}")
        case "/":
            print(f"Resultado: {div(num1, num2)}")