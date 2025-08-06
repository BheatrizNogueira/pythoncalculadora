def somar(numero1,numero2):
    return numero1 + numero2
def subtrair(numero1, numero2):
    return numero1 - numero2
def dividir(numero1, numero2):
    if numero2 == 0:
        return "erro: divisao por zero"
    return numero1 / numero2
def multiplicar(numero1, numero2):
    return numero1 * numero2
def calculadora():
    print("operacoes disponiveis:")
    print("1 - soma")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")

    escolha = input("escolha a operacao (1/2/3/4):")

    if int(escolha) > 4:
        print("opcao invalida.")
        return

    try:
        num1 = float(input("digite o primeiro numero: "))
        num2 = float(input("digite o segundo numero: "))

    except ValueError:
        print("erro")
        return
    
    if escolha == "1":
        print(f"resultado: {somar(num1, num2)}")
    elif escolha == "2":
        print(f"resultado: {subtrair(num1,num2)}")
    elif escolha == "3":
        print(f"resultado: {multiplicar(num1,num2)}")
    elif escolha == "4":
        print(f"resultado: {dividir(num1,num2)}")


calculadora()

    
    

