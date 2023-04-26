#encoding:UTF-8
import random
import sys

def get_int():
    userdata = input("Digite um número, ou 's' para sair do programa ")
    if userdata == 's':
        print ("Tchau, nos vemos!")
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Necessito de um número para continuar: ")
        return(get_int())

while True: 
    aleatorio = random.randrange(0, 5)
    escolhePc = ""
    again = ""
    print("1)pedra")
    print("2)papel")
    print("3)tesoura")
    print("4)lagarto")
    print("5)spock")
    opcao = get_int()
    
    if opcao == 1:
        escolheUsuario = "pedra"
    elif opcao == 2:
        escolheUsuario = "papel"
    elif opcao == 3:
        escolheUsuario = "tesoura"
    elif opcao == 4:
        escolheUsuario = "lagarto"
    elif opcao == 5:
        escolheUsuario = "spock"
    else:
        print("opcao Invalida")
        continue
        
    print("Você escolhe: ", escolheUsuario)    
    if aleatorio == 0:
        escolhePc = "pedra"
    elif aleatorio == 1:
        escolhePc = "papel"
    elif aleatorio == 2:
        escolhePc = "tesoura"
    elif aleatorio == 3:
        escolhePc = "lagarto"
    elif aleatorio == 4:
        escolhePc = "spock"
    print("PC escolheu: ", escolhePc)
    print("...")
    
    if escolhePc == "pedra" and escolheUsuario == "papel":
        print("Você ganhou, papel envolve pedra")
    elif escolhePc == "papel" and escolheUsuario == "tesoura":
        print("Você ganhou, tesoura corta papel")
    elif escolhePc == "tesoura" and escolheUsuario == "pedra":
        print("Você ganhou, pedra destroi tesoura")
    elif escolhePc == "lagarto" and escolheUsuario == "pedra":
        print("Você ganhou, pedra destroi o lagarto")
    elif escolhePc == "lagarto" and escolheUsuario == "tesoura":
        print("Você ganhou, tesoura decapita o lagarto")
    elif escolhePc == "tesoura" and escolheUsuario == "spock":
        print("Você ganhou, spock quebra tesoura")
    elif escolhePc == "spock" and escolheUsuario == "lagarto":
        print("Você ganhou, lagarto envenena o spock")
    elif escolhePc == "papel" and escolheUsuario == "lagarto":
        print ("Você ganhou, lagarto devora papel")
    elif escolhePc == "spock" and escolheUsuario == "papel":
        print ("Você ganhou, papel desautoriza o spock")
    elif escolhePc == "pedra" and escolheUsuario == "spock":
        print ("Você ganhou, spock vaporiza pedra")
        
    if escolheUsuario == "pedra" and escolhePc == "papel":
        print("Você perdeu, papel envolve pedra")
    elif escolheUsuario == "papel" and escolhePc == "tesoura":
        print("Você perdeu, tesoura corta papel")
    elif escolheUsuario == "tesoura" and escolhePc == "pedra":
        print("Você perdeu, pedra destroi tesoura")
    elif escolheUsuario == "lagarto" and escolhePc == "pedra":
        print("Você perdeu, pedra destroi o lagarto")
    elif escolheUsuario == "lagarto" and escolhePc == "tesoura":
        print("Você perdeu, tesoura decapita o lagarto")
    elif escolheUsuario == "tesoura" and escolhePc == "spock":
        print("Você perdeu, spock quebra tesoura")
    elif escolheUsuario == "spock" and escolhePc == "lagarto":
        print("Você perdeu, lagarto envenena o spock")
    elif escolheUsuario == "papel" and escolhePc == "lagarto":
        print ("Você perdeu, lagarto devora papel")
    elif escolheUsuario == "spock" and escolhePc == "papel":
        print ("Você perdeu, papel desautoriza o spock")
    elif escolheUsuario == "pedra" and escolhePc == "spock":
        print ("Você perdeu, spock vaporiza pedra")
    elif escolhePc == escolheUsuario:
        print("Empate")
    while again == "":
        again = input("Jogaremos de novo? sim/nao: ")
        if 'sim' in again:
            break
        elif 'nao' in again:
            print("Tchau, nos vemos!")
            sys.exit()
        else:
            print("Valor Invalido")
            again = ""
            continue
