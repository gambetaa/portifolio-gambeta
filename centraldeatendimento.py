import time

time.sleep(1)
nome = str(input('Digite seu nome: ')).capitalize()
print(f'{nome} seja bem-vind@ ao nosso portal de atendimento!')

opcao = 0
opcao1 = 0
opcao2 = 0
opcao3 = 0
opcao4 = 0

time.sleep(1)

while opcao != 5:
    # firt step
    print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- 
Escolha uma das opções a seguir:
[1] Atendimento Financeiro
[2] Atendimento Social
[3] Quem Somos
[4] Contatos
[5] Sair
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
    opcao = int(input('Digite sua opção: '))
    time.sleep(1)

    if opcao == 1:  # first option
        print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Seja bem-vind@ a nossa central de atendimento financeiro!
Escolha abaixo o que deseja fazer:
[1] Pagamento
[2] Pendências
[3] Faturas
[4] Empréstimos
[5] Sair
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')

        opcao1 = int(input('Digite sua opção: '))
        while opcao1 != 5:
            if opcao1 == 1:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                ''')
                time.sleep(0.5)
                opcao1 = int(input('Digite 5 para sair: '))
            elif opcao1 == 2:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                ''')
                time.sleep(0.5)
                opcao1 = int(input('Digite 5 para sair: '))
            elif opcao1 == 3:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                ''')
                time.sleep(0.5)
                opcao1 = int(input('Digite 5 para sair: '))
            elif opcao1 == 4:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                ''')
                time.sleep(0.5)
                opcao1 = int(input('Digite 5 para sair: '))
            elif opcao1 == 5:
                time.sleep(0.5)
                print('Finalizando seu atendimento financeiro...')

    elif opcao == 2:  # second option
        print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Seja bem-vind@ a nossa central de Atendimento Social!
Escolha abaixo o que deseja fazer:
[1] Direitos
[2] Dúvidas
[3] Atendimento com atendente
[4] Sair
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
        opcao2 = int(input('Digite sua opção: '))
        while opcao2 != 4:
            if opcao2 == 1:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                ''')
                opcao2 = int(input('Digite 4 para sair: '))
            elif opcao2 == 2:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                ''')
                opcao2 = int(input('Digite 4 para sair: '))
            elif opcao2 == 3:
                time.sleep(0.5)
                print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                ''')
                opcao2 = int(input('Digite 4 para sair: '))
            elif opcao2 == 4:
                time.sleep(0.5)
                print('Finalizando seu atendimento...')
            else:
                print('Digite um número válido.')

    elif opcao == 3:  # third option
        while opcao3 != 1:
            time.sleep(0.5)
            print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-
Seja bem-vind@ ao Banco Gambeta!
Nós estamos há 45 anos no mercado ajudando pessoas a conquistarem seus sonhos!
Venha fazer parte da gente!
-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')
            time.sleep(0.5)
            opcao3 = int(input('Digite 1 para sair: '))

    elif opcao == 4:  # fourth option
        while opcao4 != 1:
            time.sleep(0.5)
            print('''CONTATOS:
E-mail: luccagambeta04@gmail.com
Telefone: (13) 99604-9760
Linkedin: https://www.linkedin.com/in/lucca-gambeta-09ab4825b/
            ''')
            time.sleep(0.5)
            opcao4 = int(input('Digite 1 para sair: '))

    elif opcao == 5:
        print(f'Até mais {nome}, estamos finalizando seu atendimento!')

    else:
        print('Opção inválida, tente novamente...')