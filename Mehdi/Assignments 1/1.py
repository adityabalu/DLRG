def strobogrammatic(n, length):
    #print(n)
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = strobogrammatic(n-2, length)
    result = []
    for middle in middles:
        #print(middle)
        if n != length:
           result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result

print('Please enter "n":')
n = input()
print("n =",n ,"\n\n",'Strobogrammatic=',strobogrammatic(int(n), int(n)))