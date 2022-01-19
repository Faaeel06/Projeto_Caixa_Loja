def incluir_produtos():
    inclusao_produtos = []
    incluir = str(input('Iniciar inclusão de produtos? ')).upper()

    while inclusao_produtos != 'Sair':
        print('A qualquer momento digite sair para encerrar o comando.')
        produto = ''
        incluir = str(input('Iniciar inclusão de produtos? ')).upper()
        produto = str(input('Digite o nome do produto: ')).title()
        if incluir == 'SIM':
            produto = str(input('Digite o nome do produto: ')).title()
            inclusao_produtos.append(produto)
        elif incluir == 'Sair' and produto == 'Sair':

            return inclusao_produtos

        elif incluir == 'NÂO':
            break


if __name__ == '__main__':
    incluir_produtos()
