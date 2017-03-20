# Digito verificador (CPF)

def somentenumeros(entrada: object) -> bool:
    try:
        int(entrada)
        return True
    except:
        return False

while True:

    while True:
        cpf = input('Digite os nove primeiros digitos de seu CPF: ')
        if not somentenumeros(cpf) or (len(cpf) != 9):
            print('Erro! O valor digitado era inválido.')
        else:
            break

    x = [int(i) for i in list(cpf)]
    y = (x[0] * 10) + (x[1] * 9) + (x[2] * 8) + (x[3] * 7) + (x[4] * 6) + (x[5] * 5) + (x[6] * 4) + (x[7] * 3) + (
        x[8] * 2)
    z= 11 - (y % 11)

    if z == 10 or z == 11:
        d1 = 0
    else:
        d1 = z

    y = (x[0] * 11) + (x[1] * 10) + (x[2] * 9) + (x[3] * 8) + (x[4] * 7) + (x[5] * 6) + (x[6] * 5) + (x[7] * 4) + (
        x[8] * 3) + (d1 * 2)
    z = 11 - (y % 11)

    if z == 10 or z == 11:
        d2 = 0
    else:
        d2 = z

    digitos = str(d1) + str(d2)
    cpfprimeiraparte = cpf[:3]
    cpfsegundaparte = cpf[3:6]
    cpfterceiraparte = cpf [6:9]
    cpfprocurado = cpfprimeiraparte + '.' + cpfsegundaparte + '.' + cpfterceiraparte

    if len(cpf) == 9:
        print('Seu CPF é ' + cpfprocurado + '-' + digitos)
    break

# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Créditos: @vnbrs
# Comp.
