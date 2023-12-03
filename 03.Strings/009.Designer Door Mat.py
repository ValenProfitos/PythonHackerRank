# Enter your code here. Read input from STDIN. Print output to STDOUT

def desing_door_mat(N,M): #definimos una funcion que toma dos argumentos y esto representa las dimensiones del tapete
    #parte superior del tapete
    for i in range(1, N // 2 + 1): #iniciamos un bucle for que itera desde 1 hasta N // 2 + 1. la parte superior tiene la mitad de filas mas una linea adiional para la linea central
        pattern = ".|."*(2 * i - 1) #creamos un patron que consiste en el texto ".|." repetido un numero de veces que sigue un patron simetrico. (i = 1) --> ".|." (i = 2) --> ".|..|."
        print(pattern.center(M, "-")) #imprimimos el patron (centrado) de longitud M y rellenamos el espacio vacio con "-"
    #Linea central del tapete
    print("WELCOME".center(M, "-"))
    #parte inferior del tapete
    for i in range(N // 2, 0, -1): #creamos un loop que itera desde N // 2 - 1 hasta 0 (excluyendolo)
        pattern = ".|." * (2 * i -1)
        print(pattern.center(M, "-"))

if __name__ == "__main__":
    N, M = map(int, input().split())
    desing_door_mat(N, M)


