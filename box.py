
def space(string):
    return ' '.join(string)

def rotate(string, i):
    return string[i:] + string [:i]

def box(string):
    string = string.upper()
    for i in range(len(string)):
        print(space(rotate(string, i)))
    print()


if __name__ == "__main__":
    while True:
        try:
            string = input("> ")
            box(string)
        except KeyboardInterrupt:exit(0)

