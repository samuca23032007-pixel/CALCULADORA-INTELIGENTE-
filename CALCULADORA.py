print("CALCULADORA INTELIGENTE")

while True:
    print()
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR DO SISTEMA")
    print()

    opcao = int(input("Selecione a opção: "))

    match opcao:
        case 1 | 2 | 3 | 4:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))

            match opcao:
                case 1:
                    print("Soma:", a + b)
                case 2:
                    print("Subtração:", a - b)
                case 3:
                    print("Multiplicação:", a * b)
                case 4:
                    if b == 0:
                        print("Erro: divisão por zero.")
                    else:
                        print("Divisão:", a / b)
        case 5:
            print("Saindo do sistema...")
            break
        case _:
            print("Opção inválida!")