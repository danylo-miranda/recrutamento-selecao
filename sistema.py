def listar_resultados(entrevista, teorico, pratica, soft):
    candidatos_aprovados = []
    for i in lista_candidato:
        if lista_candidato[0][1] >= entrevista and lista_candidato[0][2] >= teorico and lista_candidato[0][3] >= pratica and lista_candidato[0][4] >= soft:
            candidatos_aprovados.append(i)
    return candidatos_aprovados

lista_candidato = ['joao',4,4,8,8],['ana',2,2,8,8]

entrevista = int(input('insira a nota da entrevista: '))
teorico = entrevista = int(input('insira a nota do teste teorico: '))
pratico = int(input('insira a nota dteste pratico: '))
soft = int(input('insira a nota de soft skill: '))

aprovados = listar_resultados(entrevista,teorico,pratico,soft)
print(aprovados)

# a função .join junta itens da lista e são separados pelo caractere escolhido sem a necessidade de aspas e vírgulas.
#separador = '_'
#juntar = separador.join(lista_candidato) 
#print(lista_candidato)