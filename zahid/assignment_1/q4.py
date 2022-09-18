class chapter_num():

    def chp_num(self, n):
        self.n =n 

        out =[]

        way= list(range(n+1))
        for idx, val in enumerate(way):
            out.append('Chapter '+ str(val+1))

        return(out)


method = chapter_num()
#inputs
n=3
print(method.chp_num(n))