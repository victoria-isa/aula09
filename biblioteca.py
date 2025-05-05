def impirmirnome(nome):
    print(f"Olá{nome}")

def piramide(t):
    for x in range (1,t+1,1):
        for y in range(0,x):
            print(x, end="")
        print()

def contadorVogais(frase):
    contador = 0
    vogais = "aeiouAEIOU"
    for x in range(len(frase)):
        if frase[x] in vogais:
            contador = contador + 1
    print(contador)

def estoque(produto, quantidade, valor):
    calculo = quantidade * valor
    return calculo

def verificarNumero(numero):
    if numero > 0:
        return "P"
    elif numero < 0:
        return "N"
    else:
        return "Z"

def soma(*num):
    contador = 0
    for x in range(len(num)):
        contador = contador + num[x]
    print(contador)

def qntdLetras(texto):
    contador = 0
    for x in range (len(texto)-1,-1,-1):
        print(texto[x], end="")
        if texto[x] != " ":
            contador += 1
    print(f"\n {contador}")

def listaSimplificada(L):
    novaLista =[]
    for x in L:
        if x not in novaLista:
            novaLista.append(x)
    print(novaLista)