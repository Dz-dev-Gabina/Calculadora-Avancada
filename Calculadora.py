import os
import math
from fractions import Fraction
os.system("cls")

while True:
    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Potenciacao")
    print("6 - Raiz Quadrada")
    print("7 - Operacoes com Pi")
    print("8 - Seno, Cosseno e Tangente")
    opc = input("Escolha uma operacao: ")

    match opc:
        case "0":
            print("Muito obrigado por usar o meu programa :)")
            break
        case "1":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            soma = n1 + n2
            print(f"Soma: {soma:.2f}")
            continue
        case "2":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            subt = n1 - n2
            print(f"Subtracao: {subt:.2f}")
            continue
        case "3":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            mult = n1 * n2
            print(f"Multiplicacao: {mult:.2f}")
            continue
        case "4":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            if n2 == 0:
                print("Erro! Nao e possivel efetuar divisoes por 0")
                continue
            else:
                div = n1 / n2
                print(f"Divisao: {div:.2f}")
            continue
        case "5":
            n1 = float(input("Digite o primeiro numero: "))
            n2 = float(input("Digite o segundo numero: "))
            pot = n1 ** n2
            print(f"Potenciacao: {pot:.2f}")
            continue
        case "6":
            n1 = float(input("Digite um numero: "))
            rq = math.sqrt(n1)
            print(f"Raiz quadrada de {n1}: {rq}")
            continue
        case "7":
            print("""
            1 - Comprimento de circunferência
            2 - Area do circulo
            3 - Volume da esfera
            4 - Area da superficie da esfera
            5 - Volume do cilindro
            """)
            opcpi = input("Escolha uma operacao: ")
            
            match opcpi:
                case "1":
                    decisaoCdC = input("Quer calcular o raio ou o comprimento: ")
                    if decisaoCdC == "raio":
                        CdC = float(input("Comprimento: "))
                        r = CdC / (2 * math.pi)
                        print(f"Raio: {r}")
                    elif decisaoCdC == "comprimento":
                        r = float(input("Raio do circulo: "))
                        CdC = 2 * math.pi * r
                        print(f"Comprimento: {CdC}")
                    else:
                        print(f"Digite 'raio' ou 'comprimento' ao inves de {decisaoCdC}")
                case "2":
                    decisaoAdC = input("Quer calcular o area ou o raio: ")
                    if decisaoAdC == "area":    
                        r = float(input("Raio do circulo: "))
                        AdC = math.pi * (r ** 2)
                        print(f"Area: {AdC}")
                    elif decisaoAdC == "raio":
                        AdC = float(input("Area do Circulo: "))
                        r = math.sqrt(AdC / math.pi)
                        print(f"Raio: {r}")
                    else:
                        print(f"Digite 'area' ou 'raio' ao inves de {decisaoAdC}")
                case "3":
                    decisaoVdE = input("Quer calcular o volume ou o raio: ")
                    if decisaoVdE == "volume":
                        r = float(input("Raio do circulo: "))
                        VdE = Fraction(4, 3) * math.pi * (r ** 3)
                        print(f"Volume: {VdE}")
                    elif decisaoVdE == "raio":
                        VdE = float(input("Volume da Esfera: "))
                        r = math.pow((3 * VdE) / (4 * math.pi), 1/3)
                        print(f"Raio: {r}")
                    else:
                        print(f"Digite 'volume' ou 'raio' ao inves de {decisaoVdC}")
                case "4":
                    decisaoASE = input("Quer calcular a area ou o raio: ")
                    if decisaoASE == "area":
                        r = float(input("Raio do circulo: "))
                        ASE = 4 * math.pi * (r ** 2)
                        print(f"Area: {ASE}")
                    elif decisaoASE == "raio":
                        ASE = input("Area da superficie da esfera: ")
                        r = math.sqrt(ASE / 4 * math.pi)
                        print(f"Raio {r}")
                    else:
                        print(f"Digite 'area' ou 'raio' ao inves de {decisaoASE}")
                case "5":
                    decisaoVdC = input("Quer calcular o volume, a altura ou o raio: ")
                    if decisaoVdC == "volume":
                        r = float(input("Raio do cilindro: "))
                        h = float(input("Altura do cilindro: "))
                        VdC = math.pi * (r ** 2) * h
                        print(f"Volume: {VdC}")
                    elif decisaoVdC == "altura":
                        r = float(input("Raio do cilindro: "))
                        VdC = float(input("Volume do Cilindro: "))
                        h = VdC / [math.pi * (r ** 2)]
                        print(f"Altura: {h}")
                    elif decisaoVdC == "raio":
                        h = float(input("Altura do cilindro: "))
                        VdC = float(input("Volume do Cilindro: "))
                        r = math.sqrt(VdC / (math.pi * h))
                        print(f"Raio: {r}")
                    else:
                        print(f"Digite 'volume' ou 'altura' ou 'raio' ao inves de {decisaoVdC}")
            continue
        case "8":
            print("""
            1 - Seno
            2 - Cosseno
            3 - Tangente   
            """)
            decisaoTrig = input("Escolha: ")

            match decisaoTrig:
                case "1":
                    angulo_graus = float(input("Valor do Angulo: "))
                    angulo_radianos = math.radians(angulo_graus)
                    sen = math.sin(angulo_radianos)
                    print(f"Seno de {angulo_graus}: {sen}")
                case "2":
                    angulo_graus = float(input("Valor do Angulo: "))
                    angulo_radianos = math.radians(angulo_graus)
                    cos = math.cos(angulo_radianos)
                    print(f"Cosseno de {angulo_graus}: {cos}")
                case "3":
                    angulo_graus = float(input("Valor do Angulo: "))
                    angulo_radianos = math.radians(angulo_graus)
                    tan = math.tan(angulo_radianos)
                    print(f"Tangente de {angulo_graus}: {tan}")
            continue
        case _:
            print("Erro! Escolha uma opcao valida!")
            continue  