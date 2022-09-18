class concat_string:
    def con_str(self, a, b):
        self.a =a
        self.b=b

        out=[]

        for x,y in zip(a, b):
            out.append(str(x.lower()+' '+ y.lower()))
        if len(out) == len(self.a):
            return(out)

method = concat_string()

#inputs
m = ['HellO', 'BYe']
n = ['woRlD', 'WOrld']

print(method.con_str(m,n))
