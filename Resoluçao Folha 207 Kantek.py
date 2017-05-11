# Folha 207 b2 - Matemática

print ("Digite f():")

def f():
    a = []
    for i in range(1,7):
        x = int(input("Digite o " + str(i) +"º número da sequência: "))
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
    print ("O número buscado é: " + str(a[int(busca)]))
    
# Desenvolvido por: @dygonn
# www.github.com/dygonn
# Créditos: pkantek.
# Comp.
