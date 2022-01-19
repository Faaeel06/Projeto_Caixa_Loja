import datetime as dt


print('Digite o CPF/ID do cliente que deseja incluir o horário.')
hora_atual = str(dt.datetime.now())
print(f'Data: {hora_atual[8:10]}/{hora_atual[5:7]}/{hora_atual[0:4]}')
print(f'Hora: {hora_atual[11:13]}h:{hora_atual[14:16]}m:{hora_atual[17:19]}s')
cliente_ID = int(input('Digite o CPF do cliente: '))
time_insert = input('Digite o horário para envio do pedido: ')
print(time_insert)
