import sys

conta = 0
nSques = 0
extrato = []

# Função principal
def main():
    print('')
    print(
        """Escolha uma opção:

            1 - Depósito
            2 - Saque
            3 - Extrato
            4 - SAIR
        """)

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        depositar()
    elif escolha == '2':
        sacar()
    elif escolha == '3':
        tirarExtrato()
    elif escolha == '4':
        print('')
        sys.exit('O usuário saio do sistema.')
    else:
        print('')
        print("Opção inválida!")
        main()

def depositar():
    global conta
    global extrato
    print('')
    valor = input('Que valor você deseja depositar? R$ ') 
    if valor.startswith('-'):
        print('')
        print('Não é possível depositar um número negativo, Faça um saque.')
        main()
    valor = float(valor)
    conta += valor
    extrato.append('+ R$ ' + str(format(valor,'.2f')))
    main()

def sacar():
    global conta
    global nSques
    global extrato
    print('')
    valor = input('Que valor você deseja sacar? R$ ') 
    if valor.startswith('-'):
        print('')
        print('Não é possível sacar um número negativo.')
        main()
    valor = float(valor)
    nSques += 1
    if valor > 500:
        print('')
        print('O limite de saque é de R$ 500,00 .')
        main()
    if nSques <= 3: 
        if conta > valor:
            conta -= valor
            extrato.append('- R$ ' + str(format(valor,'.2f')))
            main()
        else:
            print('')
            print('Não é possível sacar por falta de saldo.')    
            main()
    else:
        print('')
        print('Você atingiu seu limite de 3 saques diários.')
        main()

def tirarExtrato():
    global extrato
    print('')
    for i in range(len(extrato)):
        print(extrato[i])
    print('Saldo atual R$ ' + str(format(conta,'.2f')))
    main()

main()