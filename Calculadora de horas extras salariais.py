'''
 ============================================================================
 Name         : Calculadora de horas extras salariais
 Author       : Ramon Soares Mendes Meneses Leite
 Version      : 0.49
 E-mail:      : ramnsores1000@gmail.com
 University   : Universidade Federal de Goiás - Catalão GO
 Objective    : Por pura diversão
 ============================================================================
'''

#funções

def erro_e_fim(valor_qualquer, tipo):
#tipo == 1: int, tipo == 2: float
    if valor_qualquer.isnumeric():
        if tipo == 1:
            return int(valor_qualquer)
        elif tipo == 2:
            return float(valor_qualquer)
    elif valor_qualquer == "-1":
        fim()
    else:
        return (-99)


def fim():
    import time
    print()
    print('#  Encerrando', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print(f'{x: <74}#')
    print('#                            #FIM DO PROGRAMA#                            #')
    exit()

#main

print("=+="*25, end='')
print(' '*18, end='')
print("CALCULADORA DE HORAS EXTRAS SALARIAIS")
print("=+="*25)

x = '#'

print(f'{x: <74}#')
print('# ======== Digite -1 em qualquer campo para finalizar o programa ======== # ')
print(f'{x: <74}#')
cont = 1

while True:

    print(f"#       ===================== Operação Nº {cont} =====================         #")

    print(f'{x: <74}#')
    salario = str(input("#  Digite seu salário bruto: "))
    salario = erro_e_fim(salario, 2)
    while salario < -1:
        salario = str(input("#  Erro! Digite seu salário bruto: "))
        salario = erro_e_fim(salario, 2)
    print(f'{x: <74}#')

    dias_trab = str(input('#  Qual foi a quantidade de dias trabalhados no mês? '))
    dias_trab = erro_e_fim(dias_trab, 1)
    while dias_trab < -1:
        dias_trab = str(input('#  Erro! Qual foi a quantidade de dias trabalhados no mês? '))
        dias_trab = erro_e_fim(dias_trab, 1)
    print(f'{x: <74}#')

    dias_uteis = str(input('#  Qual foi a quantidade de dias úteis no mês? '))
    dias_uteis = erro_e_fim(dias_uteis, 1)
    while dias_uteis < -1:
        dias_uteis = str(input('#  Erro! Qual foi a quantidade de dias úteis no mês? '))
        dias_uteis = erro_e_fim(dias_uteis, 1)
    print(f'{x: <74}#')

    dsr = str(input('#  Qual foi a quantidade de DSR no mês? '))
    dsr = erro_e_fim(dsr, 1)
    while dsr < -1:
        dsr = str(input('#  Erro! Qual foi a quantidade de DSR no mês? '))
        dsr = erro_e_fim(dsr, 1)
    print(f'{x: <74}#')

    horas_semana = str(input('#  Digite a quantidade de horas normais trabalhadas por semana: '))
    horas_semana = erro_e_fim(horas_semana, 2)
    while horas_semana < -1:
        horas_semana = str(input('#  Erro! Digite a quantidade de horas normais trabalhadas por semana: '))
        horas_semana = erro_e_fim(horas_semana, 2)
    print(f'{x: <74}#')

    hora_extra = str(input('#  Digite a quantidade de horas extras trabalhadas por dia [SEG-SAB]: '))
    hora_extra = erro_e_fim(hora_extra, 2)
    while hora_extra < -1:
        hora_extra = str(input('#  Erro! Digite a quantidade de horas extras trabalhadas por dia [SEG-SAB]: '))
        hora_extra = erro_e_fim(hora_extra, 2)
    print(f'{x: <74}#')

    #cálculos:
    hr_extra_mes = hora_extra*dias_trab
    media_diaria = (hr_extra_mes)/dias_uteis
    hrs_dsr = media_diaria*dsr
    hrs_extrastot = hr_extra_mes+hrs_dsr
    salario_hora = salario/(horas_semana*5)
    salario_extra = salario_hora*1.5*hrs_extrastot
    v_final = salario_extra+salario

    print(f'#  O total de horas extras [SEG-SAB] foi de {hr_extra_mes} horas.')
    print('#  O valor a ser recebido pelas horas extras = R${:.2f}'.format(salario_extra))
    print('#  O valor total a ser recebido no mês = R${:.2f}'.format(v_final))
    print(f'{x: <74}#')
    cont += 1
