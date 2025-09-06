def gerar_tabela(num_proposicoes):

    #Variavéis locais da função:
    valores_verdade = ('F', 'V')
    tabela_verdade = {}
    valor_posicional_da_tupla = 1
    base = 2
    expoente = 1
    potencia_de_2 = base**expoente
    num_linhas = base**num_proposicoes

    #Criação da matriz tabela-verdade: 
    for indice_proposicional in range(num_proposicoes):
        tabela_verdade[f"p{indice_proposicional+1}"] = []


    #Preenchimento da matriz tabela-verdade:
    for i in range(num_proposicoes):
        for j in range(potencia_de_2):
            for k in range(int(num_linhas/potencia_de_2)):
                if (valor_posicional_da_tupla == 1):
                    tabela_verdade[f'p{i+1}'].append(valores_verdade[valor_posicional_da_tupla])
                    if (k == (num_linhas/potencia_de_2) - 1):
                        valor_posicional_da_tupla = 0
                else:
                    tabela_verdade[f'p{i+1}'].append(valores_verdade[valor_posicional_da_tupla])
                    if (k == (num_linhas/potencia_de_2) - 1):
                        valor_posicional_da_tupla = 1
        expoente+=1; potencia_de_2 = base**expoente

    #Retorno de tupla
    return tabela_verdade, num_linhas