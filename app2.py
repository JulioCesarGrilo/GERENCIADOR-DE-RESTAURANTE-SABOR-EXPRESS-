def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

import os 

restaurantes = [{'nome':'Pizza Planet','categoria':'Pizzaria','ativo':False},
                {'nome':'La muce','categoria':'Italiano','ativo':True},
                {'nome':'tico rito','categoria':'Mexicano','ativo':False}]

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal!')
    main()
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
        exibir_subtitulo('Finalizando App...')

def opcao_invalida():
    print('Opção invalida!')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto)) #função de fazer a contagem de caracteres de alguma variavel
    print(linha)
    print(texto)
    print(linha)        
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrando novos restaurantes')
    nome_do_restaunte = input('Digite o nome do restaurante que deseja cadastrar:\n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaunte}: ')
    dados_do_restaurante = {'nome':nome_do_restaunte,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaunte} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes listados: \n')
    
    mensagem = f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status'  # .ljust(20) é uma função que define um espaçamento entre as strings
    linha = '-' * (len(mensagem))
    print(f'\n{mensagem}') 
    print(linha)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'->{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            #print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            #print('Listar restaurantes')
            listar_restaurantes()    
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()   
        elif opcao_escolhida == 4:
            finalizar_app()  
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_ao_menu_principal()
    if not restaurante_encontrado:  # quando o if vem seguido da condição, ele só é ativo quando acontecer a condição que esta descrita nele
        print('Restaurante não encontrado')
        voltar_ao_menu_principal()
        
def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
    
if __name__ == '__main__': # Python, se este arquivo for o programa que está sendo executado diretamente, chame a função main()
    main() # todo arquivo python gera __name__, e aqui ele diz, se o name for o "principal", execute o codigo a baixo
    #Caso outro programa importe esse arquivo, ele gera outra saida, e não __main__, e ai voce tem que chamar o main manualmente ex: programa.main()