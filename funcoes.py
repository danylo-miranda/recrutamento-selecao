#FUNÇÃO QUE BUSCA O CANDIDATO DE ACORDO COM AS ENTRADAS DO USUÁRIO
def listar_resultados(entrevista, teorico, pratica, soft, candidatos):
    candidatos_aprovados = []
    for lista_candidato in candidatos: #estrutura de repetição para percorrer a lista_candidatos
        if lista_candidato[1] >= entrevista and lista_candidato[2] >= teorico and lista_candidato[3] >= pratica and lista_candidato[4] >= soft: #condições que comparam as entradas do usuário com as notas que tem na lista_candidato
            candidatos_aprovados.append(lista_candidato) #adiciona os itens que cumprem as condições a lista candidatos_aprovados
    return candidatos_aprovados



