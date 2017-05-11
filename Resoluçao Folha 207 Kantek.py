# Folha 207 b2 - Matemática

print ("Digite f():")

def f():

    #Primeira sequencia
    
    a = []
    for i in range(1,7):
        x = int(input("Digite o " + str(i) +"º número da primeira sequência: "))
        a.append(x)
    # print (l)
    a.append(0)
    a.append(0)
    a.append(0)
    a.append(0)
    a.append(0)
    if a[3] == a[1] + a[2] and a[4] == a[2] + a[3]:
        regra = "A"
    else:
        if a[3] == a[0] + a[1] + a[2] and a[4] == a[1] + a[2] + a[3]:
            regra = "B"
        else:
            if a[3] == a[2] + 16 and a[4] == a[3] + 25:
                regra = "C"
            else:
                if a[3] == (2 * a[1]) + a[2] and a[4] == (2 * a[2]) + a[3]:
                    regra = "D"
                else:
                    if a[3] == a[1] + (2 * a[2]) and a[4] == a[2] + (2 * a[3]):
                        regra = "E"
                    else:
                        regra = "F"
                        aleatorio = a[4] - (a[2] + a[3])

    if regra == "A":
        a[6] = a[4] + a[5]
        a[7] = a[5] + a[6]
        a[8] = a[6] + a[7]
        a[9] = a[7] + a[8]
        a[10] = a[8] + a[9]
    if regra == "B":
        a[6] = a[3] + a[4] + a[5]
        a[7] = a[4] + a[5] + a[6]
        a[8] = a[5] + a[6] + a[7]
        a[9] = a[6] + a[7] + a[8]
        a[10] = a[7] + a[8] + a[9]
    if regra == "C":
        a[6] = a[5] + 49
        a[7] = a[6] + 64
        a[8] = a[7] + 81
        a[9] = a[8] + 100
        a[10] = a[9] + 121
    if regra == "D":
        a[6] = 2 * a[4] + a[5]
        a[7] = 2 * a[5] + a[6]
        a[8] = 2 * a[6] + a[7]
        a[9] = 2 * a[7] + a[8]
        a[10] = 2 * a[8] + a[9]
    if regra == "E":
        a[6] = a[4] + 2 * a[5]
        a[7] = a[5] + 2 * a[6]
        a[8] = a[6] + 2 * a[7]
        a[9] = a[7] + 2 * a[8]
        a[10] = a[8] + 2 * a[9]
    if regra == "F":
        a[6] = a[4] + a[5] + aleatorio
        a[7] = a[5] + a[6] + aleatorio
        a[8] = a[6] + a[7] + aleatorio
        a[9] = a[7] + a[8] + aleatorio
        a[10] = a[8] + a[9] + aleatorio

    busca = input("Digite a posição do número buscado: ")
    busca = int(busca) - 1
        
    print ("A regra utilizada foi: " + regra)    
    print ("A sequencia de números completa é:\n" + str(a))
    print ("O número buscado é: " + str(a[int(busca)]) + "\n")

    # Segunda sequencia.

    b = []
    for i in range(1,7):
        x = int(input("Digite o " + str(i) +"º número da segunda sequência: "))
        b.append(x)
    # print (l)
    b.append(0)
    b.append(0)
    b.append(0)
    b.append(0)
    b.append(0)
    if b[3] == b[1] + b[2] and b[4] == b[2] + b[3]:
        regra = "A"
    else:
        if b[3] == b[0] + b[1] + b[2] and b[4] == b[1] + b[2] + b[3]:
            regra = "B"
        else:
            if b[3] == b[2] + 16 and b[4] == b[3] + 25:
                regra = "C"
            else:
                if b[3] == (2 * b[1]) + b[2] and b[4] == (2 * b[2]) + b[3]:
                    regra = "D"
                else:
                    if b[3] == b[1] + (2 * b[2]) and b[4] == b[2] + (2 * b[3]):
                        regra = "E"
                    else:
                        regra = "F"
                        aleatorio = b[4] - (b[2] + b[3])

    if regra == "A":
        b[6] = b[4] + b[5]
        b[7] = b[5] + b[6]
        b[8] = b[6] + b[7]
        b[9] = b[7] + b[8]
        b[10] = b[8] + b[9]
    if regra == "B":
        b[6] = b[3] + b[4] + b[5]
        b[7] = b[4] + b[5] + b[6]
        b[8] = b[5] + b[6] + b[7]
        b[9] = b[6] + b[7] + b[8]
        b[10] = b[7] + b[8] + b[9]
    if regra == "C":
        b[6] = b[5] + 49
        b[7] = b[6] + 64
        b[8] = b[7] + 81
        b[9] = b[8] + 100
        b[10] = b[9] + 121
    if regra == "D":
        b[6] = 2 * b[4] + b[5]
        b[7] = 2 * b[5] + b[6]
        b[8] = 2 * b[6] + b[7]
        b[9] = 2 * b[7] + b[8]
        b[10] = 2 * b[8] + b[9]
    if regra == "E":
        b[6] = b[4] + 2 * b[5]
        b[7] = b[5] + 2 * b[6]
        b[8] = b[6] + 2 * b[7]
        b[9] = b[7] + 2 * b[8]
        b[10] = b[8] + 2 * b[9]
    if regra == "F":
        b[6] = b[4] + b[5] + aleatorio
        b[7] = b[5] + b[6] + aleatorio
        b[8] = b[6] + b[7] + aleatorio
        b[9] = b[7] + b[8] + aleatorio
        b[10] = b[8] + b[9] + aleatorio

    busca2 = input("Digite a posição do número buscado: ")
    busca2 = int(busca2) - 1
        
    print ("A regra utilizada foi: " + regra)    
    print ("A sequencia de números completa é:\n" + str(b))
    print ("O número buscado é: " + str(b[int(busca2)]) + "\n")

    # Terceira sequencia

    c = []
    for i in range(1,7):
        x = int(input("Digite o " + str(i) +"º número da terceira sequência: "))
        c.append(x)
    # print (l)
    c.append(0)
    c.append(0)
    c.append(0)
    c.append(0)
    c.append(0)
    if c[3] == c[1] + c[2] and c[4] == c[2] + c[3]:
        regra = "A"
    else:
        if c[3] == c[0] + c[1] + c[2] and c[4] == c[1] + c[2] + c[3]:
            regra = "B"
        else:
            if c[3] == c[2] + 16 and c[4] == c[3] + 25:
                regra = "C"
            else:
                if c[3] == (2 * c[1]) + c[2] and c[4] == (2 * c[2]) + c[3]:
                    regra = "D"
                else:
                    if c[3] == c[1] + (2 * c[2]) and c[4] == c[2] + (2 * c[3]):
                        regra = "E"
                    else:
                        regra = "F"
                        aleatorio = c[4] - (c[2] + c[3])

    if regra == "A":
        c[6] = c[4] + c[5]
        c[7] = c[5] + c[6]
        c[8] = c[6] + c[7]
        c[9] = c[7] + c[8]
        c[10] = c[8] + c[9]
    if regra == "B":
        c[6] = c[3] + c[4] + c[5]
        c[7] = c[4] + c[5] + c[6]
        c[8] = c[5] + c[6] + c[7]
        c[9] = c[6] + c[7] + c[8]
        c[10] = c[7] + c[8] + c[9]
    if regra == "C":
        c[6] = c[5] + 49
        c[7] = c[6] + 64
        c[8] = c[7] + 81
        c[9] = c[8] + 100
        c[10] = c[9] + 121
    if regra == "D":
        c[6] = 2 * c[4] + c[5]
        c[7] = 2 * c[5] + c[6]
        c[8] = 2 * c[6] + c[7]
        c[9] = 2 * c[7] + c[8]
        c[10] = 2 * c[8] + c[9]
    if regra == "E":
        c[6] = c[4] + 2 * c[5]
        c[7] = c[5] + 2 * c[6]
        c[8] = c[6] + 2 * c[7]
        c[9] = c[7] + 2 * c[8]
        c[10] = c[8] + 2 * c[9]
    if regra == "F":
        c[6] = c[4] + c[5] + aleatorio
        c[7] = c[5] + c[6] + aleatorio
        c[8] = c[6] + c[7] + aleatorio
        c[9] = c[7] + c[8] + aleatorio
        c[10] = c[8] + c[9] + aleatorio

    busca3 = input("Digite a posição do número buscado: ")
    busca3 = int(busca3) - 1
        
    print ("A regra utilizada foi: " + regra)    
    print ("A sequencia de números completa é:\n" + str(c))
    print ("O número buscado é: " + str(c[int(busca3)]))

    # Conclusão

    soma = a[int(busca)] + b[int(busca2)] + c[int(busca3)]

    print("\nA soma das 3 sequencias é: " + str(soma))
    
# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Créditos: pkantek.
# Comp.
