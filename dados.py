import random
import time
#Jogo de dados apostas

cash = 100 #dinheiro inicial

print("jogo de dados \n")
print("-=-=-=-=-=-=-=-=-=-=- \n")
player = input("Digite seu nome: ")

while True:
    print("\n Ola " + player)
    cash = str(cash)
    print("\n Cash: " + cash)
    cash = int(cash)
    opcao = input("\n Próxima partida ? [1] Sim  [2] Não : ")

    if opcao.isnumeric():

        if opcao == '1':
            while True:
                aposta = int(input("\n Faça sua aposta: "))
                if aposta > cash:
                    print("\n você não tem essa grana!")
                else:
                    cash = cash - aposta
                    time.sleep(1)
                    print("\n 1")
                    time.sleep(1)
                    print("\n 2")
                    time.sleep(1)
                    print("\n 3")
                    time.sleep(1)
                    dado_player     = random.randint(1,6)
                    print("\n" + player + ": " + str(dado_player))
                    time.sleep(1)
                    print("\n 1")
                    time.sleep(1)
                    print("\n 2")
                    time.sleep(1)
                    print("\n 3")
                    time.sleep(1)
                    dado_machine    = random.randint(1,6)
                    print("\n Adversario: " + str(dado_machine))
                    time.sleep(1)
                    if dado_player > dado_machine:
                        print("\n Ganhou miseravel !!!")
                        ganho = aposta * 2
                        cash = cash + ganho
                        break
                    elif dado_player == dado_machine:
                        print("\n Empate")
                        cash = cash + aposta
                        break
                    else:
                        print("\n Perdeu !!!")
                        break


        elif opcao == '2':
            print("\n Até a próxima...")
            break
        else:
            print("\n Opção inválida")
    else:
        print("\n Opção inválida")