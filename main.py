import sys

conta = 0
nSques = 0
extrato = []
contas = []
usuarios = []
# Função principal
def main():
    print('')
    print(
        """Escolha uma opção:

            1 - Depósito
            2 - Saque
            3 - Extrato
            4 - Nova conta
            5 - Listar contas
            6 - Novo usuário
            7 - Listar usuários
            8 - SAIR
        """)

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        depositar()
    elif escolha == '2':
        sacar()
    elif escolha == '3':
        tirarExtrato()
    elif escolha == '4':
        criarConta()
    elif escolha == '5':
        listarConta()
    elif escolha == '6':
        criarUsuario()
    elif escolha == '7':
        listarUsuario()
    elif escolha == '8':
        print('')
        sys.exit('O usuário saio do sistema.')       
    else:
        print('')
        print("Opção inválida!")
        main()

def depositar():
    global contas
    global usuarios
    print('Depósito...')
    cpf = input('digite o cpf do dono da conta: ')
    if cpf_existe(cpf, usuarios):
        print('Contas do usuário')
        for i in range(len(contas)):
            if contas[i]['cpfUsuario'] == cpf:
                print(str(i + 1) + 'ª - Nº :' + str(contas[i]['nuConta']))
        print('')
        conta = input('voce deseja depositar em qual conta: ')
        for i in range(len(contas)):
            if str(contas[i]['nuConta']) == conta:
                valor = input('Que valor você deseja depositar? R$ ')
                if valor.startswith('-'):
                    print('')
                    print('Não é possível depositar um número negativo.')
                    main()
                valor = float(valor)
                contas[i]['saldo'] += valor
                contas[i]['extrato'].append('+ R$ ' + str(format(valor,'.2f')))
                main()
        else:
            print('Conta inexistente')
            main()
        
    else:
        print('O usuário não consta na base.')
        main()

def sacar():
    global contas
    global usuarios
    print('Saque...')
    cpf = input('digite o cpf do dono da conta: ')
    if cpf_existe(cpf, usuarios):
        print('Contas do usuário')
        for i in range(len(contas)):
            if contas[i]['cpfUsuario'] == cpf:
                print(str(i + 1) + 'ª - Nº :' + str(contas[i]['nuConta']))
        print('')
        conta = input('voce deseja sacar de qual conta: ')
        for i in range(len(contas)):
            if str(contas[i]['nuConta']) == conta:
                valor = input('Que valor você deseja sacar? R$ ') 
                if valor.startswith('-'):
                    print('')
                    print('Não é possível sacar um número negativo.')
                    main()
                valor = float(valor)
                contas[i]['nSques'] += 1
                if valor > 500:
                    print('')
                    print('O limite de saque é de R$ 500,00 .')
                    main()
                if contas[i]['nSques'] <= 3: 
                    if contas[i]['saldo'] > valor:
                        contas[i]['saldo'] -= valor
                        contas[i]['extrato'].append('- R$ ' + str(format(valor,'.2f')))
                        main()
                    else:
                        print('')
                        print('Não é possível sacar por falta de saldo.')    
                        main()
                else:
                    print('')
                    print('Você atingiu seu limite de 3 saques diários.')
                    main()
                contas[i]['saldo'] += float(valor)
                contas[i]['extrato'].append('+ R$ ' + str(format(valor,'.2f')))
                main()
        else:
            print('Conta inexistente')
            main()
    else:
        print('O usuário não consta na base.')
        main()

def tirarExtrato():
    global contas
    global usuarios
    print('Extrato...')
    cpf = input('digite o cpf do dono da(s) conta(s): ')    
    if cpf_existe(cpf, usuarios):
        for i in range(len(contas)):
            if contas[i]['cpfUsuario'] == cpf:
                print('--------------------------')
                print('Extrato da conta nº ' + str(contas[i]['nuConta']))
                for i2 in range(len(contas[i]['extrato'])):
                    print(contas[i]['extrato'][i])
                print('Saldo atual R$ ' + str(format(contas[i]['saldo'],'.2f')))        
        main()
    else:
        print('O usuário não consta na base.')
        main()

def criarConta():
    global contas
    print('Criando nova Conta')
    cpf = input('digite o CPF do dono da conta: ')
    if cpf_existe(cpf, usuarios):
        nuConta = len(contas) + 1
        agencia = '0001' 
        contas.append({'cpfUsuario' : cpf, 'nuAgencia' : agencia, 'nuConta' : nuConta, 'saldo' : 0.0, 'extrato' : [], 'nSques' : 0})
        print('Conta Crianda!')
        main()
    else:
        print('O usuário não consta na base.')
        main()
    

def listarConta():
    global contas
    for i in range(len(contas)):
        print('------------------------')
        print('CPF Usuário: ' + str(contas[i]['cpfUsuario']))
        print('Agência: ' + str(contas[i]['nuAgencia']))
        print('Conta: ' + str(contas[i]['nuConta']))
    main()

def criarUsuario():
    global usuarios
    print('Criando Usuário')
    cpf = input('digite o CPF: ')
    if cpf_existe(cpf, usuarios):
        print('Usuário já cadastrado na base.')
        main()
    nome = input('digite nome: ')
    dataNascimento = input('digite a data de nascimento (dd/mm/yyyy): ')
    print('Dados de Endereco')
    Enderecologradouro = input('digite o logradouro: ')
    EnderecoNumero = input('digite o nº: ')
    EnderecoBairro = input('digite o bairro: ')
    EnderecoCidade = input('digite a cidade: ')
    EnderecoUf = input('digite a UF: ')
    usuarios.append({'cpfUsuario' : cpf, 'nome' : nome, 'dataNascimento' : dataNascimento, 'endereco' : str(Enderecologradouro) + ', ' + str(EnderecoNumero) + ', ' + str(EnderecoBairro) + ', ' + str(EnderecoCidade) + ' - ' + str(EnderecoUf) })
    main()

def cpf_existe(cpf, lista):
    for tupla in lista:
        if cpf == tupla['cpfUsuario']:
            return True
    return False

def listarUsuario():
    global usuarios
    for i in range(len(usuarios)):
        print('------------------------')
        print('CPF Usuário: ' + str(usuarios[i]['cpfUsuario']))
        print('Nome: ' + str(usuarios[i]['nome']))
        print('Data de Nascimento: ' + str(usuarios[i]['dataNascimento']))
        print('Endereço: ' + str(usuarios[i]['endereco']))
    main()
main()