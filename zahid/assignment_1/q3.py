class match_product():

    def mat_pro(self, a,b):
        self.a =a
        self.b =b
        out =[]

        for x,y in zip(a,b):

            if isinstance(x, str)  and isinstance(y, str): # both str
                if x.isdigit() and y.isdigit(): #both number
                    out.append(int(x)*int(y))
            elif (isinstance(x, int) and isinstance(y, str)):
                if y.isdigit():
                    out.append(int(x)*int(y))
            elif (isinstance(x, str) and isinstance(y, int)):
                if x.isdigit():
                    out.append(int(x)*int(y))
            else:
                continue
        return out


method= match_product()
#inputs
a = ['12', '13', 'Hello', '4', '6', '10]']
b = ['2', '3', '4', 5, '[6', 12, 14]


if __name__== "__main__":
    print(method.mat_pro(a,b))



