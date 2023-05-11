lista_candidato = []
entrevista = []
teorica = []
pratica = []
soft = []

#ESTRUTURA DE REPETIÇÃO WHILE: o usuário posde inserir quantos candidatos quiser
while True:
        opcoes = input(
        f'\nBem Vindo(a)\n'
        '[1] Cadastrar Candidato\n'
        '[2] Listar como Tabela\n'
        '[3] Resultados\n'
        '[4] Encerrar o Sistema\n'
        'Escolha uma das opções:'
    )
        
        if opcoes == '4': 
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
        
            lista_candidato.append({'candidato':candidato})
            entrevista.append({'entrevista':nota_entrevista})
            teorica.append({'prova teorica':nota_teorico})
            pratica.append({'prova pratica':nota_pratica})
            soft.append({'soft skill':nota_soft}) 
            print(f'\nAs informações do candidato(a): {candidato} foram inseridas corretamente no sistema.')
resultado = lista_candidato + entrevista + teorica + pratica + soft
print(resultado)

