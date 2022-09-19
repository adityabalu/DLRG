list_a = ['HellO', 'BYe']
list_b = ['woRLD', 'WOrld']
result = []
def concatenator(a, b):
    combined = list(zip(a, b))
    for s,r in combined:   
            result.append(s.lower()+" "+r.lower())
    return result
    
print(concatenator(list_a, list_b))       