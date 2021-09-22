def listar_D(Disp):
    for Codigo, Motocicleta in Disp.items():
        print(f'Codigo: {Codigo}')
        print(f"Tipo:   {Motocicleta['Tipo']}")
        print(f"Modelo: {Motocicleta['Modelo']}")
        print(f"Ano:    {Motocicleta['Ano']}")
        print(f"Placa:  {Motocicleta['Placa']}")
        print(f"Chassi: {Motocicleta['Chassi']}")
        print('='*41)
def listar_F(Financiamentos):
    for Nome, JOSEBSON_SOUSA in Financiamentos.items():
        print(f'Nome:     {Nome}')
        print(f"Entrada :  {JOSEBSON_SOUSA['Entrada']}")
        print(f"Pacelas:   {JOSEBSON_SOUSA['Pacelas']}")
        print(f"Data:      {JOSEBSON_SOUSA['Data']}")
        print(f"Codigo:    {JOSEBSON_SOUSA['Codigo']}")
        print(f"Tipo:      {JOSEBSON_SOUSA['Tipo']}")
        print(f"Modelo:    {JOSEBSON_SOUSA['Modelo']}")
        print(f"Ano:       {JOSEBSON_SOUSA['Ano']}")
        print(f"Placa:     {JOSEBSON_SOUSA['Placa']}")
        print(f"Chassi:    {JOSEBSON_SOUSA['Chassi']}")
        print('='*41)
def cadastrar_D (Disp, Codigo, Tipo, Modelo, Ano, Placa, Chassi):
    Disp[Codigo] = {
        "Codigo":Codigo,
        "Tipo" : Tipo,
        "Modelo": Modelo,
        "Ano": Ano,
        "Placa": Placa,
        "Chassi": Chassi}

def cadastrar_F (Financiamentos, Nome, Entrada, Pacelas, Data, Codigo, Tipo, Modelo, Ano, Placa, Chassi):
    Financiamentos[Nome] = {
        "Nome": Nome,
        "Entrada": Entrada,
        "Pacelas": Pacelas,
        "Data": Data,
        "Codigo":Codigo,
        "Tipo" : Tipo,
        "Modelo": Modelo,
        "Ano": Ano,
        "Placa": Placa,
        "Chassi": Chassi
}
def ApagarD (Codigo,Disp):
    if Codigo in Disp :
        Disp.pop(Codigo)
        print('-'*42)
        print('\033[1;92mVeículo removido com sucesso!\033[m')
        print('-'*42)

def ApagarF (Nome,Financiamentos):
    if Nome in Financiamentos :
        Financiamentos.pop(Nome)
        print('-'*42)
        print('\033[1;92m Financiamentos removido com sucesso!\033[m')
        print('-'*42)
def localizarV(Disp, codigo):
    if codigo in Disp:
        print('-'*42)
        print("SEU VEÍCULO FOI LOCALIZADO COM SUCESSO.")
        print('-'*42)
        print(Disp[codigo])

def localizarF(Financiamentos, Nome):
    if Nome in Financiamentos:
        print('-'*42)
        print("SEU VEÍCULO FOI LOCALIZADO COM SUCESSO.")
        print('-'*42)
        print(Financiamentos[Nome])

def alterarV(Disp, codigo):
    if codigo in Disp :

        novo_Tipo = input ('Digte o Tipo: ')
        novo_Modelo = input('Digite o novo Modelo : ')
        novo_Ano = float(input('Digite o Ano : '))
        novo_Placa = input('Digite a nova Placa : ')
        novo_Chassi = input('Digite o novo Chassi : ')
        Disp[codigo] = {
        'Tipo': novo_Tipo,
        'Modelo': novo_Modelo,
        'Ano': novo_Ano,
        'Placa': novo_Placa,
        'Chassi': novo_Chassi,
        }
        print('-'*42)
        print('Alterado com sucesso!')
        print('-'*42)
    else:
        print('-'*42)
        print('Este codigo não existe!')
        print('-'*42)

def alteraF(Financiamentos, Nome):
    if Nome in Financiamentos :

        novo_Entrada = input ('Digte a Entrada: ')
        novo_Pacelas = input('Digite as Pacelas  : ')
        novo_Data = float(input('Digite a Data : '))
        novo_Codigo = input('Digite o novo Código : ')
        novo_Tipo = input ('Digte o Tipo: ')
        novo_Modelo = input('Digite o novo Modelo : ')
        novo_Ano = float(input('Digite o Ano : '))
        novo_Placa = input('Digite a nova Placa : ')
        novo_Chassi = input('Digite o novo Chassi : ')
        Financiamentos[Nome] = {
        'Entrada': novo_Entrada,
        'Pacelas': novo_Pacelas,
        'Data': novo_Data,
        'Codigo':novo_Codigo,
        'Tipo': novo_Tipo,
        'Modelo': novo_Modelo,
        'Ano': novo_Ano,
        'Placa': novo_Placa,
        'Chassi': novo_Chassi,
        }
        print('-'*42)
        print('Alterado com sucesso!')
        print('-'*42)
    else:
        print('-'*42)
        print('Este Nome não existe!')
        print('-'*42)
