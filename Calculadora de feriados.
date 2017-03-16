# Calculadora de feriados nacionais.

import math

def somentenumeros(entrada: object) -> bool:
    try:
        int(entrada)
        return True
    except:
        return False

def inputnumerico(texto: str) -> int:
    while True:
        numero = input(texto)
        if not somentenumeros(numero) or (len(numero) !=4):
            print ('Erro! O ano digitado é invalido,')
        else:
            return numero
while True:
    
    ano = int(inputnumerico('Digite o ano cujo você quer descobrir a data da pascoa: '))

    A = ano%19
    B = math.floor(ano/100)
    C = ano%100
    D = math.floor(B/4)
    E = B%4
    F = math.floor((B+8))/25
    G = math.floor((1+B-F))/3
    H = ((19*A)+B+15-(D+G))%30
    I = math.floor(C/4)
    K = C%4
    L = (32+(2*E)+(2*I)-(H+K))%7
    M = math.floor((A+(11*H)+(22*L))/451)
    P = math.floor((H+L+114-(7*M))/31)
    Q = (H+L+114-(7*M))%31

    print ('Os feriados deste ano serão nas seguintes datas:')
    print ('Páscoa: ' + str(int(Q+1)) + '/' + str(P))
    
    x = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)        
    y = [0,0,0,0,0,0,0,0,0,0,0,0]
    s = 0
    
    for i in range(1,12):
        s = s + x[i-1]
        y[i] = s
        
    i = 0
    dd = y[P-1] + Q+1
    i = 0
    dd = dd + 60
    
    while y[i] < dd:
      i = i + 1
    ee = dd - y [i-1]
    
    print ('Corpus Christi: '+str(int(ee))+'/'+str(i))
    
    i = 0
    dd = dd - (60+47)
    while y[i] < dd:
        i = i + 1
    ee = dd - y [i-1]
    
    print ('Carnaval: '+str(int(ee))+'/'+str(i))

    i = 0
    dd = dd + (47-2)
    while y[i] < dd:
        i = i + 1
    ee = dd - y [i-1]

    print ('Sexta-feira Santa: '+str(int(ee))+'/'+str(i))
    print ('Desenvolvido por: @dygonn')

    break
    
# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Créditos: @vnbrs, pkantek.
# Comp.
