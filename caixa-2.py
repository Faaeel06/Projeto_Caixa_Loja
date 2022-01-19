import time

# Desenvolver um programa que crie fluxo de caixa para um restaurante

# Programa deve conter opções principais de almoço = 'def', 'while' e 'if'
novos_produtos = ''
print('-=-' * 10, 'Bem-Vindo(a)', '-=-' * 10)
time.sleep(1)
print('=' * 10, 'CAIXA', '=' * 10)
print(['Incluir', 'Fechar Caixa'])
entrada = input('O que deseja fazer? ')

if entrada == 'Incluir':
        def inclsuao_produtos(incluir):
            produtos = ' '
            while novos_produtos != 'NÃO':
                novos_produtos = input('Incluir novos produtos? ').upper()
                if novos_produtos == 'SIM':
                    produto = input('Digite o nome do produto: ').title()
                    preco = float(input('Digite o valor: R$ '))
                    quantidade = int(input('Quantidade: '))
                    produtos += produto
                else:
                    novos_produtos = 'NÃO'
                    print('Fechando inclusão de produtos.')
            return(entrada)
elif entrada == 'Fechar Caixa':
    print('Fechamento concluído.')


# Bomboniere = excel

# Produtos avulsos = excel

# Inclusão de novos produtos = excel

# Formas de pagamentos = excel

# Valores separados por forma de pagamento = 'def', 'while' e 'if'

# Fluxo final de caixa = tkinter/pandas/outlook/twilio
'''fechamento_caixa.py'''
# Valores totais do dia = tkinter/pandas/outlook/twilio

# Programa deve conter interface gráfica = Tkinter

# Botões que auxiliem nas funções = tkinter

# Botões que apresentem resumos = tkinter/while/if

# Botões de fechamento e faturamento = tkinter/pandas/outlook/twilio/

# Condições de acionar o envio de resumo via e-mail/menssagem

# Envio automático no fechamento = outlook/twilio

#Programa tem que ser executável = pywin32

#Pasta para inclusão e edição de arquivos excel
