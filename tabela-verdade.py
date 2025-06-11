#Variavéis globais:
valor_logico = ('F', 'V')
tabela_verdade = []
posicao_valor = 1
base = 2
expoente = 1


#Variável de entrada:
num_proposicoes = int(input("""Insira o número de proposições
(Lembre-se: o número pertence ao conjunto dos números naturais e é maior ou igual a 1): """))

#Criação de lista de listas: 
for _ in range(num_proposicoes):
    tabela_verdade.append([])

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
for n in range(base**num_proposicoes):
    for e in tabela_verdade:
        print(f'| {e[n]} |', end="")
    print()
