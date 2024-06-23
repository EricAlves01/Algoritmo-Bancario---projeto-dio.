# Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
#  O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
# O sistema será desenvolvido para um banco que busca monetizar suas operações. 
# Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule 
# as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.
menu = '''  >>> menu <<< 
---- escolha suas operações ----
1 - deposito 
2 - saque 
3 - extrato 
4 - sair
------------- /// ---------------
''' 
saldo = 2000 
limite = 1000
extrato = ""
numeroSaque = 0
limiteSaque = 2  


while True:
    opcao = input(menu)
    if opcao =='1':
        Deposito = float(input('digite o valor do deposito: '))
        if Deposito >= limite:
            saldo += Deposito
            print('-- Deposito Realizado --') 
        if Deposito < limite:
            print('erro no deposito tente novamente mais tarde')
    if opcao =='2':
            print('>> Opção Saque <<')
            saque = float(input(' digite o valor do saque:  ')) 
            excedeuSaldo = saque > saldo
            excedeuLimite = saque > limite
            excedeuSaque = numeroSaque >= limiteSaque
            if saldo >= saque: 
                print('saque realizado')
            if saldo < saque:
                print('erro de saque , tente novamente mais tarde')
            if excedeuSaldo:
                 print('Operação falhou!!, você não possui saldo suficiente')
            elif excedeuLimite:
                 print('Operação falhou!!você execedeu o limite fixado!!')
            elif excedeuSaque:
                 print('Operação falhou !! numero de saque excedido!!')
            elif saque > 0: 
                saldo -= saque 
                extrato += f'saque: R$ {saque:.2f}'
                numeroSaque += 1
            else:
                 print('Operação falhou o numero informado é invalido!!')
    
    if opcao == '3':
         print('>> Opção extrato <<') 
         print('---Extrato---')
         print('Não foram realizadas movimentações' if not extrato else extrato)    
         print(f'Saldo : R$ {saldo:.2f}') 
         print('>>>>>>>>>//<<<<<<<<<')     
    elif opcao =='4': 
         print('voltando para aba inicial')
         break
   
         
         
                     
         




