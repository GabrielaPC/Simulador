'''
simulação de circuitos quânticos

autores: Gabriela Pinheiro Costa e Luis Kowada

ultima alteração: 19/05/2021 (GP)

pendências:   

1- Definição de funções
2- Otimização do processamento 
3- *Ideia: definição de funções já salvar o matriz operador resultante.

status atual: cx,ccx,swap são permutações.

última alteração: reorganização das classes em arquivos diferentes e atualização da documentação do código.            
'''

from simulacao import *

nome_arquivo = "teste.txt"
#nome_arquivo = input("Digite o nome do arquivo: ")

simu = simulacao(0,nome_arquivo)
simu.simular()
