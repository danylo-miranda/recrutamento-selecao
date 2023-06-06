from funcoes import *

recrutamento = Recrutamento()
recrutamento.questoes()
while True:
    try:
        salvar = str(input('\nDigite *sim* salvar os dados em um arquivo .csv  '))
        if salvar == 'sim':
            recrutamento.save_csv(input('\nDigite o nome do arquivo a ser salvo: '))
            print('\nObrigado por utilizar nosso sistema')
            break
        else:
            exit()
    except ValueError:
        print('Digite *sim* para salvar ou *não* para encerrar o sistema ')        