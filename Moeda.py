def aumentar(valor):
    resultado = ((valor * 10) / 100 + valor)

    return resultado


def dobro(valor):
    resultado = valor * 2

    return resultado


def metade(valor):
    resultado = valor / 2

    return resultado


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')  #formata

