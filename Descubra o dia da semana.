# Descubra o dia da semana de uma data específica.

import math

print ('Descubra em que dia de semana cai uma data específica.')

def somentenumeros(entrada: object) -> bool:
    try:
        int(entrada)
        return True
    except:
        return False

while True:

    while True:
        dia = input('Digie o dia: ')
        if somentenumeros(dia) or (len(dia) <= 2):
            mes = input('Digite o mes: ')
            if somentenumeros(mes) or (len(mes) <= 2):
                ano = input('Digite o ano: ')
                if somentenumeros(ano) or (len(ano) <= 4):
                    break
                else:
                    print('Erro! O valor digitado era inválido.')
                    continue

    ano = int(ano)
    mes = int(mes)
    dia = int(dia)
    
    A = math.floor((12-mes)/10)
    B = ano-A
    C = mes+(12*A)
    D = math.floor(B/100)
    E = math.floor(D/4)
    F = E+2-D
    G = math.floor(365.25*B)
    H = math.floor(30.6001*(C+1))
    I = F+G+H+dia+5
    R = I%7

# Dia da semana encontrado em numeral.

    if R == 1:
        R = 'Domingo'
    if R == 2:
        R = 'Segunda-feira'
    if R == 3:
        R = 'Terça-feira'
    if R == 4:
        R = 'Quarta-feira'
    if R == 5:
        R = 'Quinta-feira'
    if R == 6:
        R = 'Sexta-feira'
    if R == 0:
        R = 'Sábado'

# Dia da semana convertido em texto.

    print('Este dia será um(a): ' + str(R) + '.')
    print('Desenvolvido por: @dygonn')

    break
    
# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Comp.
