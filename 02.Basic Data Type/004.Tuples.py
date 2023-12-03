# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__== '__main__':
     n = int(input())
     integer_list = map(int, input().split())
     #crear una tupla a partir de la lista de enteros
     tuple_list = tuple(integer_list)

       #calcular la hash de la tupla
     hash_value = hash(tuple_list)

        #imprimir la hash de la tupla
     print(hash_value)

#solo funciona en pypy3, mi primer codigo estaba bien