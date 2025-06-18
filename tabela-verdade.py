#Tratamento de erro/exceção:
try:
    num_proposicoes = int(input("""Insira o número de proposições
    (Lembre-se: o número pertence ao conjunto dos números naturais e é maior ou igual a 1): """))
except ValueError:
    print(f"\nErro: entrada não é um número natural. Por favor, redigite o número baseado nas condições de inserção.")

else:
    #Variavéis:
    valores_verdade = ('F', 'V')
    tabela_verdade = []
    valor_posicional_da_tupla = 1
    base = 2
    expoente = 1
    potencia_de_2 = base**expoente
    num_linhas = base**num_proposicoes

    #Criação da matriz tabela-verdade: 
    for indice_proposicional in range(num_proposicoes):
        tabela_verdade.append([f"p{indice_proposicional+1}"])
        
    #Preenchimento da matriz tabela-verdade:
    for i in range(num_proposicoes):
        for j in range(potencia_de_2):
            for k in range(int(num_linhas/potencia_de_2)):
                if (valor_posicional_da_tupla == 1):
                    tabela_verdade[i].append(valores_verdade[valor_posicional_da_tupla])
                    if (k == (num_linhas/potencia_de_2) - 1):
                        valor_posicional_da_tupla = 0
                else:
                    tabela_verdade[i].append(valores_verdade[valor_posicional_da_tupla])
                    if (k == (num_linhas/potencia_de_2) - 1):
                        valor_posicional_da_tupla = 1
        expoente+=1; potencia_de_2 = base**expoente

    #Exibição da matriz tabela-verdade de n proposições:
    print("\n"+"-------"*num_proposicoes)
    for index in range(num_linhas+1):
        for lista in tabela_verdade:
            if index == 0:
                print(f'|  {lista[index]} |', end="")
            else:
                print(f'|  {lista[index]}  |', end="")
        print()
        print("-------"*num_proposicoes, end="")    
        print()