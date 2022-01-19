import pandas as pd


def incluir_produtos():
    start = input('[ENTER]')
    inicio_produtos = ''
    list_item = {}
    while inicio_produtos != 'NÃO':
        inicio_produtos = input('Deseja inserir produtos?').upper()
        if inicio_produtos == 'SIM':
            item_name = input('Insira o nome do produto: ')
            item_value = input('Insira o valor da unidade: R$ ')
            item_amount = input('Digite a quantidade de unidades: ')

            inicio_produtos = input('Deseja inserir produtos?').upper()
            list_item = {item_name: [item_value, item_amount]}
            trat = list(list_item.values())
        elif inicio_produtos == 'NÃO':
            # with open('Lista Produtos.csv', 'w', encoding='UTF-8') as file:
            #     file.write(list_item)
            #     print(f'{final:.2f}')
            produtos = pd.DataFrame(data=list_item)
            produtos.to_csv('files/Lista_Produtos.csv', sheet_name='Produtos', index=False)
            produtos.to_excel('files/Produtos.xlsx', sheet_name='Produtos', index=False)
            print(list_item)
            return list_item


# Precisa salvar em um csv

incluir_produtos()
