def print_formatted(number):
    # your code goes here
    numbers = list(range(1, number + 1))

    width = len(bin(number)[2:])

    for num in numbers:
        decimal = str(num).rjust(width)
        octal = oct(num)[2:].rjust(width)
        hexadecimal = hex(num)[2:].upper().rjust(width)
        binary = bin(num)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")
                   

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)