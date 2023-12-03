def print_rangoli(size):
    #your code goes here
    import string
    alphabet = string.ascii_lowercase

    width = 4 * size - 3

    for i in range(size -1, 0, -1):
        line = "-".join(alphabet[size - 1:i:-1] + alphabet[i:size])
        print(line.center(width, "-"))

    center_line = "-".join(alphabet[size - 1::-1] + alphabet[1:size])
    print(center_line.center(width, "-"))

    for i in range(1, size):
        line = "-".join(alphabet[size - 1:i:-1] + alphabet[i:size])
        print(line.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)