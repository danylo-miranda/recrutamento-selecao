class Recrutamento():
    candidatos = [['joao',4,4,8,8],['ana',2,2,8,8],['silvia',2,2,4,4],['jade',2,2,4,4],['jackeline',6,6,9,9]]
    candidatos_aprovados = []
    
#MÉTODO QUE BUSCA O CANDIDATO DE ACORDO COM AS ENTRADAS DO USUÁRIO
    def listar_resultados(self, entrevista, teorico, pratica, soft, candidatos):
        
        for lista_candidato in candidatos: #estrutura de repetição para percorrer a lista_candidatos
            if lista_candidato[1] >= entrevista and lista_candidato[2] >= teorico and lista_candidato[3] >= pratica and lista_candidato[4] >= soft: #condições que comparam as entradas do usuário com as notas que tem na lista_candidato
                self.candidatos_aprovados.append(lista_candidato) #adiciona os itens que cumprem as condições a lista candidatos_aprovados
        return self.candidatos_aprovados
    
    def questoes(self):
        while True:
            try: #utilizei Try e Except para evitar o erro de digitar um caractere ao invés de um numero inteiro
                entrevista = int(input('Insira o valor da nota da entrevista: '))
                teorico = int(input('Insira o valor da nota do teste teórico: '))
                pratica = int(input('Insira o valor da nota da prova prática: '))
                soft = int(input('Insira o nivél de soft skill do candidato: '))
                aprovados = self.listar_resultados(entrevista, teorico, pratica, soft, self.candidatos)
                print('\nCandidatos aprovados e suas respectivas notas: ')
                print(self.juntar(aprovados))
                print('\nObrigado por utilizar nosso sistema')
                break 
            except ValueError:
                print('Insira um número válido')

    #MÉTODO PARA FORMATAR OS RESULTADOS
    def juntar (self,candidato):
        resultados = [] #função com apenas 1 argumento que será posicionado com a lista de aprovados
        for candidato in self.candidatos_aprovados: # .format() utilizado para formatar os resultados de acordo com o posicionamento de cada iten da lista
            resultado = '{}-e{}_t{}_p{}_s{}'.format(candidato[0],candidato[1], candidato[2], candidato[3], candidato[4]) 
            resultados.append(resultado)
        return ' '.join(resultados) #.join() utilizado para adicionar '_' entre os itens da lista
    

      
