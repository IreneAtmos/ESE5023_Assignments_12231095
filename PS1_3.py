import numpy as np

# n>2
def Pascal_triangle(n):
    old_tri = [1,1]
#    print('1')
#    print('1,1')
    for t in range(3,n+1):
        new_tri = np.zeros(t)#.astype(int)
        new_tri[0] = 1
        new_tri[t-1] = 1
#        print(1, end=',')
        for i in range(1,t-1):
            new_tri[i] = old_tri[i-1]+old_tri[i]
#            print(int(new_tri[i]), end=',')
#        print('1')
        old_tri = new_tri
    print(new_tri)

Pascal_triangle(100)
Pascal_triangle(200)