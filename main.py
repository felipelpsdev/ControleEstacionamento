import os as sistema
import funcoes as controle_estacionamento

vagas_totais = 10
reservas = []

while True:
    sistema.system('cls')
    print('===== CONTROLE DE ESTACIONAMENTO =====')
    print('1 - Entrada de Carro')
    print('2 - Saída de Carro')
    print('3 - Consultar Reservas')
    print('0 - Sair')
    menu = input('>> ')

    if menu == '0':
        sistema.system('cls')
        break
    elif menu == '1':
        sistema.system('cls')
        try:
            reservas = controle_estacionamento.cadastrar_reserva(reservas, input('Digite a placa do carro: '), int(input('Digite a hora de entrada (0-24): ')))
            print('Entrada registrada com sucesso!')
        except ValueError as e:
            print(f'Erro: {e}')
        sistema.system('pause')
    elif menu == '2':
        sistema.system('cls')
        try:
            reservas = controle_estacionamento.saida_carro(reservas, input('Digite a placa do carro: '), int(input('Digite a hora de saída (0-24): ')))
        except ValueError as e:
            print(f'Erro: {e}')
        sistema.system('pause')
    elif menu == '3':
        sistema.system('cls')
        controle_estacionamento.imprimir_reservas(reservas)
        sistema.system('pause')
    else:
        print('\nOpção Inválida!')
        sistema.system('pause')