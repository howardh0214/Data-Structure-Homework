def poly_add(pol1, pol2):
    new_pol1 = pol1.replace('-', '+-').split('+')
    new_pol2 = pol2.replace('-', '+-').split('+')

    while ("" in new_pol1): 
        new_pol1.remove("") 

    while ("" in new_pol2): 
        new_pol2.remove("") 

    if (new_pol1[-1].find('x^1') != -1):
        pass
    else:
        new_pol1[-1] = new_pol1[-1]+"x^0"

    if (new_pol2[-1].find('x^1') != -1):
        pass
    else:
        new_pol2[-1] = new_pol2[-1]+"x^0"

    for i in range(len(new_pol1)):
        new_pol1[i] = new_pol1[i].split('x^')
        if (new_pol1[i][0] == ''):
            new_pol1[i][0] = 1.00
            new_pol1[i][1] = int(new_pol1[i][1])
        elif (new_pol1[i][0] == '-'):
            new_pol1[i][0] = -1.00
            new_pol1[i][1] = int(new_pol1[i][1])
        else:
            new_pol1[i][0] = float(new_pol1[i][0])
            new_pol1[i][1] = int(new_pol1[i][1])

    for i in range(len(new_pol2)):
        new_pol2[i] = new_pol2[i].split('x^')
        if (new_pol2[i][0] == ''):
            new_pol2[i][0] = 1.00
            new_pol2[i][1] = int(new_pol2[i][1])
        elif (new_pol2[i][0] == '-'):
            new_pol2[i][0] = -1.00
            new_pol2[i][1] = int(new_pol2[i][1])
        else:
            new_pol2[i][0] = float(new_pol2[i][0])
            new_pol2[i][1] = int(new_pol2[i][1])

    max_pol = int(max(new_pol1[0][1], new_pol2[0][1]))

    pol_sum = []
    for i in range(max_pol, -1, -1):
        pol_sum.append([0.0,i])

    for i in range(len(pol_sum)):
        for j in range(len(new_pol1)):
            if (pol_sum[i][1] == new_pol1[j][1]):
                pol_sum[i][0] += new_pol1[j][0]
        for j in range(len(new_pol2)):
            if (pol_sum[i][1] == new_pol2[j][1]):
                pol_sum[i][0] += new_pol2[j][0]

    return pol_sum

if __name__ == '__main__':
    pol1 = str(input())
    pol2 = str(input())
    output = poly_add(pol1, pol2)
    counter = 0
    for i in output:
        if (i[0] == 0.0):
            counter += 1
    if (counter == len(output)):
        print(0)
    else:
        for i in range(len(output)):
            if (output[i][0] == 0):
                continue
            else:
                if (i != 0) & (output[i][0] > 0):
                    print("+", end = "")
                if (i == len(output)-1):
                    if (output[i][0].is_integer() == True):
                        print(int(output[i][0]), end = "")
                    else:
                        print('{:0.1f}'.format(output[i][0]), end = "")
                else:
                    if (output[i][0] == 1):
                        pass
                    elif (output[i][0] == -1):
                        print('-', end = "")
                    else:
                        if (output[i][0].is_integer() == True):
                            print(int(output[i][0]), end = "")
                        else:
                            print('{:0.1f}'.format(output[i][0]), end = "")
                    print("x^", end = "")
                    print(output[i][1], end = "")