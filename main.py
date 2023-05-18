from funcoes import listar_resultados

#FUNÇÃO PARA FORMATAR OS RESULTADOS
def juntar (candidato):
    resultados = [] #função com apenas 1 argumento que será posicionado com a variavel 'aprovados'
    for candidato in aprovados: # .format() utilizado para formatar os resultados de acordo com o posicionamento de cada iten da lista
        resultado = '{}-e{}_t{}_p{}_s{}'.format(candidato[0],candidato[1], candidato[2], candidato[3], candidato[4]) 
        resultados.append(resultado)
    return ' '.join(resultados) #.join() utilizado para adicionar '_' entre os itens da lista
# não consegui relacionar a variavel aprovados no arquivo de funções, por isso, fui obrigado a colocar essa função no arquivo principal

candidatos = [['joao',4,4,8,8],['ana',2,2,8,8],['silvia',2,2,4,4],['jade',2,2,4,4],['jackeline',6,6,9,9]]

while True:
    try: #utilizei Try e Except para evitar o erro de digitar um caractere ao invés de um numero inteiro
        entrevista = int(input('Insira o valor da nota da entrevista: '))
        teorico = int(input('Insira o valor da nota do teste teórico: '))
        pratica = int(input('Insira o valor da nota da prova prática: '))
        soft = int(input('Insira o nivél de soft skill do candidato: '))
        aprovados = listar_resultados(entrevista, teorico, pratica, soft, candidatos)
        print('\nCandidatos aprovados e suas respectivas notas: ')
        print(juntar(aprovados))
        print('\nObrigado por utilizar nosso sistema')
        break 
    except ValueError:
        print('Insira um número válido')    



