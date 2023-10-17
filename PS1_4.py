def Least_moves(n):
    count = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
            count += 1
        else:
            n = n-1
            count += 1
    print(count)

for i in range(1,101):
    print(i,end=',')
    Least_moves(i)