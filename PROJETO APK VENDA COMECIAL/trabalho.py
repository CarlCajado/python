from funçoes import *
print('#'*40)
print('#'*9,'CAJADO MOTOS E PEÇAS','#'*9)
print('#'*40)
menu = '''
DIGITE A OPÇÃO DESEJADA:

VEÍCULOS:
[1] Listar Veículos Disponíveis.
[2] Cadastrar Novo Veículo.
[3] Localizar pelo Código.
[4] Excluir Veículo.
[5] Alterar Veículo.


FINANCIAMENTOS.
[6] Listar Financiamentos.
[7] Cadastrar Nova Venda.
[8] Localizar pelo Nome.
[9] Excluir Financiamentos.
[0] Alterar Financiamentos.

                                [X] Para sair.
 '''
Disp = {
        '001':{
         'Codigo':'001',
         'Tipo': 'Motocicleta',
         'Marca': 'Honda',
         'Modelo': 'biz',
         'Ano': '2010',
         'Placa': 'BVF-5481',
         'Chassi':'XXXXXXXXXXXXXXXXXXXX'
    },
        '002':{
            'Codigo':'002',
            'Tipo': 'Carro',
            'Marca': 'Fiat',
            'Modelo': 'uno',
            'Ano': '2013',
            'Placa': 'DSX-8587',
            'Chassi':'XXXXXXXXXXXXXXXXXXXX'

        }
}
Financiamentos = {
        'JOSEBSON_SOUSA':{
         'Nome' :'JOSEBSON SOUSA',
         'Entrada':'10.000 R$',
         'Pacelas': '24X',
         'Data': '20/03/2010',
         'Codigo':'004',
         'Tipo': 'Motocicleta',
         'Marca': 'Honda',
         'Modelo': 'BROS',
         'Ano': '2021',
         'Placa': '(SEM PLACA)',
         'Chassi':'XXXXXXXXXXXXXXXXXXXX'
    },
        'DALZIRENE PINTO':{
        'Nome' :'DALZIRENE PINTO',
        'Entrada': '50.000 R$',
        'Pacelas' : '14',
        'Data': '20/1/2021',
        'Codigo': '005',
        'Tipo': 'Carro',
        'Marca': 'HILUX',
        'Modelo': 'uno',
        'Ano': '2012',
        'Placa': 'TYU-8526',
        'Chassi':'XXXXXXXXXXXXXXXXXXXX'

        }
}
while True:
    opcao = input(menu).upper()
    if opcao == 'X':
        print("\n\033[1;92mOBRIGADO !!, FUI.\033[m")
        break
    elif opcao == '1':
        print('='*40)
        print('='*9,'Veículos Disponíveis','='*9)
        print('='*40)
        listar_D(Disp)

    elif opcao == '2':
        print('='*40)
        print('='*13,'Novo Veículo','='*13)
        print('='*40)
        Codigo = input('Digite o Código: (EX: 003): ')
        Tipo = input('Digite o Tipo (EX: Carro): ')
        Modelo = input('Digite o Modelo :')
        Ano = input('Digite o Ano de Fabricação: ')
        Placa = input('Digite A PLACA :(EX: XXX-1234): ')
        Chassi = input('Digite o Chassi: ')
        print('='*40)
        print('='*9,'CADASTRADO COM SUCESSO:','='*9)
        print('='*40)
        cadastrar_D (Disp, Codigo, Tipo, Modelo, Ano, Placa, Chassi)

    elif opcao=='3':
        codigo= input('Digite o codigo do Veículo  que voce deseja localizar: ').upper()
        localizarV(Disp, codigo)

    elif opcao == '4':
        Codigo= input('Digite o codigo do Veículo que voce deseja excluir: ')
        ApagarD (Codigo,Disp)

    elif opcao=='5':
        codigo = input('Digite o codigo do Veículo que voce deseja alterar: ').upper()
        alterarV(Disp, codigo)


    elif opcao == '6':
        print('='*40)
        print('='*12,'Financiamentos','='*12)
        print('='*40)
        listar_F(Financiamentos)



    elif opcao == '7':
        print('='*40)
        print('='*14,'Nova Venda','='*14)
        print('='*40)
        Nome = input('Digite o Nome do Comprador: ')
        Entrada = input('Digite A Entrada: (EX: 1000,00 R$): ')
        Pacelas = input('Digite o Número de Pacelas: (EX: 4X): ')
        Data = input('Digite a Data da Venda: (EX: 01/07/2021): ')
        Codigo = input('Digite o Código: (EX: 003): ')
        Tipo = input('Digite o Tipo (EX: Carro): ')
        Modelo = input('Digite o Modelo :')
        Ano = input('Digite o Ano de Fabricação: ')
        Placa = input('Digite A PLACA :(EX: XXX-1234): ')
        Chassi = input('Digite o Chassi: ')
        print('='*40)
        print('='*9,'CADASTRADO COM SUCESSO:','='*9)
        print('='*40)
        cadastrar_F (Financiamentos, Nome, Entrada, Pacelas, Data, Codigo, Tipo, Modelo, Ano, Placa, Chassi)
    elif opcao == '8':
        Nome= input('Digite Nome que deseja Localizar: ').upper()
        localizarF(Financiamentos,Nome)

    elif opcao == '9':
            Nome = input('Digite o Nome do Financiamento que voce deseja excluir: ')
            ApagarF (Nome,Financiamentos)

    elif opcao=='0':
        Nome = input('Digite o Nome que voce deseja alterar os dados: ').upper()
        alteraF(Financiamentos, Nome)
