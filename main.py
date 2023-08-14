def convertTypes(value):
    if isinstance(value,int):
        return str(value)
    if isinstance(value,float):
        return str(value)
    if isinstance(value, bool):
        return str(value)

def print_hi(name):
    print(f'Hi, {name}')
    print("Type is:",type(name))

if __name__ == '__main__':
    print_hi('Visual Studio')
    print(convertTypes(123))
    print(convertTypes(123.34))
    print(convertTypes(True))

