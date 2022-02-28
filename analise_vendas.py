"""
ANALISANDO UMA TABELA DE VENDAS COM A BIBLIOTECA PANDAS
"""

import pandas as pd

# Importar a Base de Dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar a Base de Dados
pd.set_option('display.max_columns', None)
# print(tabela_vendas[['ID Loja', 'Valor Final']])

# Faturamento por Loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print('\n', '>>>> FATURAMENTO POR LOJA <<<<')
print(faturamento)
print('='*60)

# Quantidade de produtos vendidos por Loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print('\n', '>>>> QUANTIDADE DE PRODUTOS VENDIDOS POR LOJA <<<<')
print(quantidade)
print('='*60)

# Ticket médio dos produto em cada Loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})  # Renomeando a coluna
print('\n', '>>>> TICKET MÉDIO DOS PRODUTO EM CADA LOJA <<<<')
print(ticket_medio)
print('='*60)


