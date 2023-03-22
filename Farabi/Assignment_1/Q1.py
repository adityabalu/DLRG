def num_finder(n_length):
    if n_length == 0:
        return [""]
    elif n_length == 1:
        return ["1","0","8"]
    mid_point == num_finder(n_length - 2)
    strob_list = []

    for mid in mid_point:
        strob_list.append('0' +  + '0')
        strob_list.append('1' +  + '1')
        strob_list.append('6' +  + '9')
        strob_list.append('8' +  + '8')
        strob_list.append('9' +  + '6')
    return strob_list    

if __name__ == '__main__':
    num = input("give the length :")
    print(num_finder(int(num)))


