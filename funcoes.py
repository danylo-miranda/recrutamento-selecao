import csv

class Recrutamento():
    candidatos = [['joao',4,4,8,8],['ana',2,2,8,8],['silvia',2,2,4,4],['jade',2,2,4,4],['jackeline',6,6,9,9]]
    candidatos_aprovados = []
    
    #MÉTODO QUE BUSCA O CANDIDATO DE ACORDO COM AS ENTRADAS DO USUÁRIO
    def listar_resultados(self, entrevista, teorico, pratica, soft, candidatos):
        
        for nota_corte in candidatos: #estrutura de repetição para percorrer a lista de candidatos
            if nota_corte[1] >= entrevista and nota_corte[2] >= teorico and nota_corte[3] >= pratica and nota_corte[4] >= soft: 
                self.candidatos_aprovados.append(nota_corte) #adiciona os itens que cumprem as condições a lista candidatos_aprovados
        return self.candidatos_aprovados
        #condições que comparam as entradas do usuário com as notas que tem na lista de candidato partir da posição 1 da lista já que a posição 0 é uma string com o nome do candidato
    
    #MÉTODO QUE SOLICITA AS NOTAS E VERIFICA AS ENTRADAS DO USUARIO
    def questoes(self):
        while True:
            try: # impede que o usuario digite um valor menor do que 0 e maior do que 10
                entrevista = int(input('Insira o valor da nota da entrevista: '))
                if entrevista < 0 or entrevista > 10:
                    raise ValueError('Insira um número válido entre 0 e 10')
                teorico = int(input('Insira o valor da nota do teste teórico: '))
                if teorico < 0 or teorico > 10:
                    raise ValueError('Insira um número válido entre 0 e 10')
                pratica = int(input('Insira o valor da nota da prova prática: '))
                if pratica < 0 or pratica > 10:
                    raise ValueError('Insira um número válido entre 0 e 10')
                soft = int(input('Insira o nivél de soft skill do candidato: '))
                if soft < 0 or soft > 10:
                    raise ValueError('Insira um número válido entre 0 e 10')
                aprovados = self.listar_resultados(entrevista, teorico, pratica, soft, self.candidatos)#MÉTODO LISTAR_RESULTADOS
                print('\nCandidatos aprovados e suas respectivas notas: ')
                print(self.juntar(aprovados))#MÉTODO QUE FORMATA OS RESULTADOS                
                break 
            except ValueError:
                print('Insira um número válido entre 0 e 10')

    #MÉTODO PARA FORMATAR OS RESULTADOS
    def juntar (self,candidato):
        resultados = [] #função com apenas 1 argumento que será posicionado com a lista de aprovados
        for candidato in self.candidatos_aprovados: # .format() utilizado para formatar os resultados de acordo com o posicionamento de cada iten da lista
            resultado = '{}-e{}_t{}_p{}_s{}'.format(candidato[0],candidato[1], candidato[2], candidato[3], candidato[4]) 
            resultados.append(resultado)
        return ' '.join(resultados) #.join() utilizado para adicionar '_' entre os itens da lista
    
    #MÉTODO PARA SALVAR OS DADOS EM .CSV
    def save_csv(self,nome_arquivo): #metodo que salva o arquivo em .csv/ abre o arquivo CSV no modo de escrita.
        with open(f'{nome_arquivo}.csv', 'w', newline='') as arquivo_csv:#parâmetro newline='' para que não haja linhas em branco no arquivo.  
            escrever_csv = csv.writer(arquivo_csv) #cria um objeto que irá escrever no arquivo CSV. 
            escrever_csv.writerow(['*****Aprovados*****']) #cabeçalho da tabela utilizando a função writerow.
            for dados in self.candidatos_aprovados: #percorrer a lista respostas e escreve cada um dos elementos no arquivo CSV.
                escrever_csv.writerow([dados])
        print(f'\nArquivo {nome_arquivo} criado e os dados foram escritos.')
      
