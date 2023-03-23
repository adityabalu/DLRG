# strobogrammatic function

def strg_num(n):
	
	out = filler(n, n)
	return out



def filler(n, len): 
	
    if n == 0: return [""] #n=0, no fill
    if n == 1: return ["1", "0", "8"] #n=1, fill with 0,1,8 and 6 & 9 can't fill

    fill = filler(n-2, len)

    # print(fill, n, len) 

    out = []
	
    for f in fill:

        out.append("8" + f + "8")
        out.append("1" + f + "1")
        out.append("9" + f + "6")
        out.append("6" + f + "9")
    
    return out



if __name__ == '__main__':

	print(strg_num(4))

# sample output:
# ['8888', '1881', '9886', '6889', '8118', '1111', '9116', '6119', '8968', '1961', '9966', '6969', '8698', '1691', '9696', '6699']