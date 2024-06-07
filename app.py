import os

jogos = []

def exibir_nome_do_programa():
    print("""
    █▀▀ █▀█ █░░ █▀▀ █▀▀ ▄▀█ █▀█   █▀▄ █▀▀   ░░█ █▀█ █▀▀ █▀█ █▀
    █▄▄ █▄█ █▄▄ ██▄ █▄▄ █▀█ █▄█   █▄▀ ██▄   █▄█ █▄█ █▄█ █▄█ ▄█
    """)

def exibir_opcoes():
    print('1. Cadastrar jogo')
    print('2. Listar jogos')
    print('3. Ativar jogo')
    print('4. sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando programa')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para reiniciar: ')
    main()

def cadastrar_novo_jogo():
    os.system('cls')
    print('Cadastrar novo jogo\n')
    nome_jogo = input('Digite o nome do Jogo: ')
    jogos.append(nome_jogo)
    print(jogos)
    input('Digite uma tecla para reiniciar: ')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_jogo()
        elif opcao_escolhida == 2:
            print('Listar jogos')
        elif opcao_escolhida == 3:
            print('Ativar jogo')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()