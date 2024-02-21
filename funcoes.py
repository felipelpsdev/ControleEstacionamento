def gerar_codigo_reserva(reservas):
    if not reservas:
        return 1
    else:
        return reservas[-1]['codigo'] + 1

def cadastrar_reserva(reservas, placa, hora_entrada):
    if hora_entrada < 0 or hora_entrada > 24:
        raise ValueError("Hora de entrada inválida. Deve estar entre 0 e 24.")

    if len(reservas) < 10:
        codigo = gerar_codigo_reserva(reservas)
        reserva = {'codigo': codigo, 'placa': placa, 'hora_entrada': hora_entrada, 'hora_saida': None, 'valor_pagar': None}
        reservas.append(reserva)
        return reservas
    else:
        raise ValueError("Estacionamento lotado! Não há vagas disponíveis.")

def saida_carro(reservas, placa, hora_saida):
    for reserva in reservas:
        if reserva['placa'] == placa and reserva['hora_saida'] is None:
            if hora_saida < 0 or hora_saida > 24:
                raise ValueError("Hora de saída inválida. Deve estar entre 0 e 24.")

            if hora_saida < reserva['hora_entrada']:
                raise ValueError("Hora de saída não pode ser menor que a hora de entrada.")

            reserva['hora_saida'] = hora_saida
            reserva['valor_pagar'] = calcular_valor(reserva['hora_entrada'], hora_saida)
            return reservas

    raise ValueError("Placa não encontrada ou carro já saiu.")

def calcular_valor(hora_entrada, hora_saida):
    return (hora_saida - hora_entrada) * 5

def imprimir_reservas(reservas):
    print('-----------------------')
    for reserva in reservas:
        print('CÓDIGO: ', reserva['codigo'])
        print('PLACA: ', reserva['placa'])
        print('HORA DE ENTRADA: ', reserva['hora_entrada'])
        if reserva['hora_saida'] is not None:
            print('HORA DE SAÍDA: ', reserva['hora_saida'])
            print('VALOR A PAGAR: R$ ', reserva['valor_pagar'])
        else:
            print('CARRO AINDA ESTACIONADO')
        print('-----------------------')