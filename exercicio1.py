#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(frase):
    
    lista_palavras = frase.split()


    palavras_unicas = set(lista_palavras)

    quantidade = len(palavras_unicas)

    return quantidade

    # print(lista_palavras)

    # aux = 0

    # for i in lista_palavras:
    #     print(i)
    #     aux += 1

    # return aux






# Teste a sua função aqui (caso ache necessário)
print(conta_palavras_unicas('string string a b'))


