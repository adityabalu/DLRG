
def concatList(l1,l2):
    #l1 = input("enter list 1");
    #l2 = input("enter list 2");
    lcon = [];
    for a,b in zip(l1,l2):
        lcon.append(a.lower()+" "+b.lower())
    print(lcon)


if __name__ == '__main__':
    l1 = [string for string in input("Enter the list items : ").split()]
  
    l2 = [string for string in input("Enter the list items : ").split()]
    concatList(l1,l2);