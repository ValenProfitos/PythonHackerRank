def count_substring(string, substring):
    #CREAMOS UNA VARIABLE CON VALOR 0 QUE ALMACENARÁ CUANTAS VECES APARECE LA SUB CADENA EN LA CADENA PRINCIPAL
    count = 0

    #CREAMOS UNA VARIABLE QUE NOS DICE LA LONGITUD DE LA SUB CADENA PARA NO TENER QUE HACERLO EN EL LOOP FOR
    sub_len= len(sub_string)

    #CREAMOS UN BUCLE FOR PARA ITERAR A TRAVES DE LA CADENA PRINCIPAL. DURANTE CADA ITERACION, COMPARA SI UNA PORCION DE LA CADENA PRINCIPAL ES IGUAL A LA SUB CADENA
    for i in range(len(string) - sub_len + 1): #INICIA EL BUCLE QUE RECORERÁ TODAS LAS POSIBLES SUBCADENAS DE LA CADENA PRINCIPAL QUE TIENEN LA MISMA LONGITUD QUE LA SUB CADENA. ESTE INICIA EN i = 0 Y TERMINA EN i= len(string) - sub_len
        if string[i:i+sub_len] == sub_string: #comprueba si la sub cadena de la cadena principal desde la posicion i hasta i+sub_len es igual a sub_string. esto verifica si la subcadena de la principal coincide con exacamente con la subcadena pedida
            count += 1 #en caso de coincidir la variable que almacena la cant de subcadenas incrementa de a 1
    return count #devuelve el valor de la variable

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)