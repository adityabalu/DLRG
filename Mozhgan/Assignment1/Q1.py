def strobogrammatic(n):
    result = num_stro(n, n)
    return result


def num_stro(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]
    middles = num_stro(n - 2, length)
    x = []
    for i in middles:
        if n != length:
            x.append("0" + i + "0")
        x.append("8" + i + "8")
        x.append("1" + i + "1")
        x.append("9" + i + "6")
        x.append("6" + i + "9")
    return x


num = int(input("Please enter the length of numbers: "))
print(strobogrammatic(num))

