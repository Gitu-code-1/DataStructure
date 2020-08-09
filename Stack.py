multipleinput = int(input())

for i in range(multipleinput):
    input1 = list(input())
    input2 = list()
    dict1 = {'{':'}','[':']','(':')'}
    if (len(input1)%2!=0) or len(input1)==0:
        print("NO")
    elif input1[0] in [')',']','}']:
        print("NO")
    else:
        flag=True
        for i in input1:
            if i not in ['(','[','{',')',']','}']:
                flag=False
                break
            else:
                if  i in ['(','[','{']:
                    input2.append(i)
                elif i in [')',']','}']:
                    if dict1[input2[-1]] == i:
                        input2.pop()
                    else:
                        flag=False
                        break
                else:
                    continue

        if flag == True and len(input2) == 0:
            print("YES")
        else:
            print("NO")

