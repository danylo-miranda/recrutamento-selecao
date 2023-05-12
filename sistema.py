lista_candidato = []

def listar_resultados(entrevista, teorico, pratica, soft):
    resultados = [lista_candidato]
    candidatos_aprovados = []
    for resultado in resultados:
        if resultado[1] >= entrevista and resultado[2] >= teorico and resultado[3] >= pratica and resultado[4] >= soft:
            candidatos_aprovados.append(resultado)
            
    
    return candidatos_aprovados

#ESTRUTURA DE REPETIÇÃO WHILE: o usuário posde inserir quantos candidatos quiser
while True:
        opcoes = input(
        f'\nMENU PRINCIPAL\n'
        '[1] Cadastrar Candidato\n'
        '[2] Listar resultados\n'
        '[3] Encerrar o Sistema\n'
        'Escolha uma das opções:'
    )
        
        if opcoes == '3': 
            break
        
        elif opcoes == '1':
            candidato = str(input('nome do candidato: '))
            nota_entrevista = float(input('nota da entrevista: '))
            while nota_entrevista < 0 or nota_entrevista > 10:
                print('insira uma nota válida entre 0 e 10')
                nota_entrevista = float(input('nota da entrevista: '))
           
            nota_teorico = float(input('nota do teste teórico: '))
            while nota_teorico < 0 or nota_teorico > 10:
                print('insira uma nota válida entre 0 e 10')
                nota_teorico = float(input('nota do teste teórico: '))
        
            nota_pratica = float(input('nota do teste prático: '))
            while nota_pratica < 0 or nota_pratica > 10:
                print('insira uma nota válida entre 0 e 10')
                nota_pratica = float(input('nota do teste prático: '))
         
            nota_soft = float(input('nivel de soft skill: '))
            while nota_soft < 0 or nota_soft > 10:
                print('insira uma nota válida entre 0 e 10')
                nota_soft = float(input('nivel de soft skill: '))
        
            lista_candidato.append(candidato.title())
            lista_candidato.append(nota_entrevista) 
            lista_candidato.append(nota_teorico)
            lista_candidato.append(nota_pratica)
            lista_candidato.append(nota_soft) 
            print(f'\nAs informações do candidato(a): {candidato.title()} foram inseridas corretamente no sistema.')

        elif opcoes == '2':
            aprovados = listar_resultados(4,4,8,8)
            print(aprovados)
            
# a função .join junta itens da lista e são separados pelo caractere escolhido sem a necessidade de aspas e vírgulas.
#separador = '_'
#juntar = separador.join(lista_candidato) 
#print(lista_candidato)

mensagem = ('Obrigado por utilizar nosso sistema :)')
print(mensagem)

