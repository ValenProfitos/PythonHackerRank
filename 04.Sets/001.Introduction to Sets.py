def average(array):
    # your code goes here
    numerosUnicos = set(array)

    promedio = sum(numerosUnicos) / len(numerosUnicos)

    return promedio

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)