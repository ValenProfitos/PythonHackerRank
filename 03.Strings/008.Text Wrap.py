import textwrap

def wrap(string, max_width):
    #utilizar textwrap.wrap() para dividir el texto en lineas
    wrapped_text = textwrap.wrap(string, max_width)

    return "\n".join(wrapped_text)

if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)