def concat_string(a, b):

    out=[]

    for x,y in zip(a, b):

       out.append(str(x.lower()+' '+ y.lower()))
       if len(out) == len(a):
        return(out)

#inputs
a = ['HellO', 'BYe']
b = ['woRlD', 'WOrld']

if __name__ == '__main__':
    print(concat_string(a, b))