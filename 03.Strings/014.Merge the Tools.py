def merge_the_tools(string, k):
    # your code goes here
    n = len(string)

    for i in range(0, n, k):
        sub_str = string[i:i+k]
        seen = {}
        sub_str_result = ""

        for char in sub_str:
            if char not in seen:
                seen[char] = True
                sub_str_result += char
        print(sub_str_result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)