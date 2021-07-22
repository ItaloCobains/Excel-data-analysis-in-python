import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC003b1b313b7cf2b70a33796401440d35"
# Your Auth Token from twilio.com/console
auth_token  = "a4c5031163009d4598829b07cc9ec3d7"
client = Client(account_sid, auth_token)



lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5564992527258", 
            from_="+16466814584",
            body=f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

#end