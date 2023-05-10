resultado = []
#ESTRUTURA DE REPETIÇÃO WHILE: o usuário posde inserir quantos candidatos quiser
while True:
    candidato = str(input('nome do candidato: '\
        'Digite "fim" para encerrar'))
    if candidato == 'fim': 
        break
  
    nota_entrevista = float(input('nota da entrevista: '))
    while nota_entrevista < 0 or nota_entrevista > 10.1:
        print('insira uma nota válida entre 0 e 10')
        nota_entrevista = float(input('nota da entrevista: '))
           
    nota_teorico = float(input('nota do teste teórico: '))
    while nota_teorico < 0 or nota_teorico > 10.1:
        print('insira uma nota válida entre 0 e 10')
        nota_teorico = float(input('nota do teste teórico: '))
        
    nota_pratica = float(input('nota do teste prático: '))
    while nota_pratica < 0 or nota_pratica > 10.1:
        print('insira uma nota válida entre 0 e 10')
        nota_pratica = float(input('nota do teste prático: '))
         
    nota_soft = float(input('nivel de soft skill: '))
    while nota_soft < 0 or nota_soft > 10.1:
        print('insira uma nota válida entre 0 e 10')
        nota_soft = float(input('nivel de soft skill: '))
        
    resultado.append({'candidato':candidato, 'entrevista':nota_entrevista, 'prova teorica':nota_teorico, 'prova pratica':nota_pratica, 'soft skill':nota_soft}) 
print(resultado)

