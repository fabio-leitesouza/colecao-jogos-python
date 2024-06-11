import os

jogos = [{'nome':'Zelda', 'categoria':'RPG', 'ativo':False},
         {'nome':'Mario', 'categoria':'Plataforma', 'ativo':True},
         {'nome':'Metroid', 'categoria':'Plataforma', 'ativo':True}]

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

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print() 

def finalizar_app():
    os.system('cls')
    print('Encerrando programa')

def opcao_invalida():
    exibir_subtitulo('Opção inválida')
    input('Digite uma tecla para reiniciar: ')
    main()

def cadastrar_novo_jogo():
    os.system('cls')
    exibir_subtitulo('Cadastro de jogo')
    nome_jogo = input('Digite o nome do Jogo: ')
    categoria = input('Digite a categoria do jogo: ')
    dados_do_jogo = {'nome':nome_jogo, 'categoria':categoria, 'ativo':False}
    jogos.append(dados_do_jogo)
    input('Digite uma tecla para reiniciar: ')
    main()

def listar_jogos():
    os.system('cls')
    exibir_subtitulo('Listando os Jogos')
    for jogo in jogos:
        nome_do_jogo = jogo['nome']
        categoria_do_jogo = jogo['categoria']
        ativo_jogo = jogo['ativo']
        print(f' - {nome_do_jogo} | {categoria_do_jogo} | {ativo_jogo}' )

    input('Digite uma tecla para reiniciar: ')
    main()

def alternar_estado_jogo():
    exibir_subtitulo('Modificar estado do jogo')
    nome_jogo = input('Digite o nome do jogo: ')
    for jogo in jogos:
        if nome_jogo == jogo['nome']:
            jogo['ativo'] = not jogo['ativo']
            if jogo['ativo']:
               print(f'O jogo {nome_jogo} está ativado')
            else:
                print(f'O jogo {nome_jogo} está desativado')  
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_jogo()
        elif opcao_escolhida == 2:
            listar_jogos()
        elif opcao_escolhida == 3:
            alternar_estado_jogo()
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