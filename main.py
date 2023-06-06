from funcoes import *

recrutamento = Recrutamento() 
recrutamento.questoes()
while True:
    try:
        salvar = str(input('\nDigite *sim* para salvar os dados em um arquivo ou *não* para encerrar o sistema: '))#oferece para o usuario a opção de salvar o arquivo
        if salvar == 'sim':
            recrutamento.save_csv(input('\nDigite o nome do arquivo a ser salvo: '))#oferece a opção de escolher o nome do arquivo
            print('\nObrigado por utilizar nosso sistema')
            break
        else:
            print('\nObrigado por utilizar nosso sistema')
            exit()
    except TypeError:
        print('Digite *sim* para salvar ou *não* para encerrar o sistema ')        