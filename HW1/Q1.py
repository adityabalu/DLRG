
def strobogrammatic(n):
    if n == 0: 
        return [""];
    if n == 1:
        return ["1","8","0"]
    if n > 1:
        list = [];
        subset = strobogrammatic(n-2)
        for s in subset:
            list.append("1"+s+"1")
            list.append("8"+s+"8")
            list.append("0"+s+"0")
            list.append("6"+s+"9")
            list.append("9"+s+"6")
        return list;

if __name__ == '__main__':
    n = int(input("enter n:"))
    print(strobogrammatic(n))
