#Variavéis globais:
valor_logico = ('F', 'V')
tabela_verdade = []
posicao_valor = 1
base = 2
expoente = 1

#Variável de entrada:
try:
    num_proposicoes = int(input("""Insira o número de proposições
    (Lembre-se: o número pertence ao conjunto dos números naturais e é maior ou igual a 1): """))
except ValueError:
    print(f"\nErro: entrada não é um número natural. Por favor, redigite o número baseado nas condições de inserção.")

else:

    #Criação de lista de listas: 
    for index_proposicional in range(num_proposicoes):
        tabela_verdade.append([f"p{index_proposicional+1}"])

    #Geração da tabela-verdade:
    for i in range(num_proposicoes):
        for j in range(base**expoente):
            for k in range(int(base**num_proposicoes/(base**expoente))):
                if (posicao_valor == 1):
                    tabela_verdade[i].append(valor_logico[posicao_valor])
                    if (k == (base**num_proposicoes/(base**expoente)) - 1):
                        posicao_valor = 0
                else:
                    tabela_verdade[i].append(valor_logico[posicao_valor])
                    if (k == (base**num_proposicoes/(base**expoente)) - 1):
                        posicao_valor = 1
        expoente+=1

    #Exibição da tabela-verdade de n proposições:
    print("\n"+"-------"*num_proposicoes)
    for indice in range(base**num_proposicoes+1):
        for lista in tabela_verdade:
            if indice == 0:
                print(f'|  {lista[indice]} |', end="")
            else:
                print(f'|  {lista[indice]}  |', end="")
        print()
        print("-------"*num_proposicoes, end="")    
        print()
