def numeric(n):
    try:
        float(n)  
    except ValueError:
        return False
    return True

def product(l1,l2):
    lpro = []
    for a,b in zip(l1,l2):
        a = a.strip().lstrip('\'')
        a = a.strip().rstrip('\'')
        b = b.strip().lstrip('\'')
        b = b.strip().rstrip('\'')
        print(a, b)
        if numeric(a) & numeric(b):
            lpro.append(int(float(a)*float(b)))
    print(lpro)


if __name__ == '__main__':
    l1 = [string for string in input("Enter the list items : ").split(',')]
    l2 = [string for string in input("Enter the list items : ").split(',')]
    product(l1,l2)