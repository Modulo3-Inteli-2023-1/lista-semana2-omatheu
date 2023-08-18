#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(palavra1, palavra2):
    d = ''
    # g = []
    # for letras in palavra1:
    #     print(letras)
    #     d += letras
    # for letra in palavra2:
    #     print(letra)
    #     g += letra

    for letra in palavra1:
        d += letra
        print(d)

    if d in palavra2:
        return True
    else:
        print('Not is a anagram')
        return False
    # if d == g:
    #     return True
    # else:
    #     print('Nada não')

    # print(d)
    # print(g)
    # if len(palavra1) == len(palavra2):
    #     return True






# Teste a sua função aqui (caso ache necessário)
a = 'amor'
b = 'roma'

print(is_anagram(a, b))











