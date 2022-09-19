list_a = ['12', '13', 'Hello', '4', '6', '10]']
list_b = ['2', '3', '4', 5, '[6', 12, 14]
result = []
print(str.isdigit(list_a[0]))
def concatenator(a, b):
    for i in range(min(len(a),len(b))):
        if str.isdigit(str(a[i])) and str.isdigit(str(b[i])):   
            result.append(int(a[i])*int(b[i]))
    return result
    
print(concatenator(list_a, list_b))