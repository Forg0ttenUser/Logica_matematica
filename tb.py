#Tratamento de erro/exceção:
try:
    #Variável global de entrada:
    num_proposicoes = int(input("""Insira o número de proposições
    (\033[0;33mLembre-se:\033[m n \u2208 \u2115 \u22C0 n \u2265 1 ): """))
except ValueError:
    print(f"\n\033[0;31mErro:\033[m entrada não é um número natural. Por favor, redigite o número baseado nas \033[4;33mcondições de inserção\033[m.")

else:
    if num_proposicoes <= 0:
        print("\n\033[0;31mErro:\033[m n \u2264 0. Por favor, insira um \033[33mnúmero \u2265 1\033[m.")
    else:
        #Variavéis globais:
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


        #Exibição da matriz tabela-verdade de n proposições:
        for a in tabela_verdade.values():
            print(a)