g = []
txt_1 = [26, 23, "50", "30", "Hello", 20, "Mozhgan", 20, "20"]
txt_2 = [27, "25", 26, "40", "50", "Thanks"]
for i in txt_1:
    if (txt_1.index(i) + 1) > len(txt_2):
        break
    else:
        if type(i) == int:
            if type(txt_2[txt_1.index(i)]) == int:
                g.append(i * txt_2[txt_1.index(i)])
            else:
                x = txt_2[txt_1.index(i)].isdigit()
                if x is True:
                    g.append(i * eval(txt_2[txt_1.index(i)]))
        else:
            x = i.isdigit()
            if x is True:
                if type(txt_2[txt_1.index(i)]) == int:
                    g.append(eval(i) * txt_2[txt_1.index(i)])
                else:
                    x = txt_2[txt_1.index(i)].isdigit()
                    if x is True:
                        g.append(eval(i) * eval(txt_2[txt_1.index(i)]))
print(g)
