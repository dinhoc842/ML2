"""
Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA() que consiga mostrar os valores
como um valor monetário formatado.
"""

from exercicio108 import Moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10%, temos {Moeda.moeda(Moeda.aumentar(p))}')
