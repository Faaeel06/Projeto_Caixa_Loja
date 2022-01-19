def cadastro_clientes():
    inicio_entrada = ' '
    while inicio_entrada != 'Não':
        inicio_entrada = input('Deseja adicionar clientes?')

        name = input('Digite o nome completo do cliente: ')
        tel = int(input('Digite o telefone[Somente números]: '))
        endereco = input('Digite o endereço: ')
        cpf = int(input('Digite o CPF[Somente números]: '))

        dados_cliente = {cpf: [f'Nome:{name}', f'\nTEL: {tel}', f'\nEndereço: {endereco}']}
        print(dados_cliente.values())
# precisa salvar em um CSV


cadastro_clientes()
