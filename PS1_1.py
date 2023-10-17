def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            print(c,a,b)
        else:
            print(c,b,a)

a = 3
b = 2
c = 1
Print_values(a,b,c)

a = 3
b = 1
c = 2
Print_values(a,b,c)

a = 2
b = 1
c = 3
Print_values(a,b,c)

a = 1
b = 2
c = 3
Print_values(a,b,c)