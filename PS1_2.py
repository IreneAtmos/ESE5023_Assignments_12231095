import numpy as np

# Always create the same random matrices by using seeds. 
np.random.seed(12231095)

# Get 50 integers from 0 to 50, and using `reshape` to get the rows and columns from M1 and M2.
M1 = np.mat(np.random.randint(0,50,50).reshape(5,10))
M2 = np.mat(np.random.randint(0,50,50).reshape(10,5))

print(M1)
print(M2)

def Matrix_multip(m1,m2):
    if m1.shape[1] == m2.shape[0]:
        commonCR = m1.shape[1]
        newR = m1.shape[0]
        newC = m2.shape[1]
        m1_mul_m2 = np.zeros((newR,newC))
        for i in range(newR):
            for j in range(newC):
                for k in range(commonCR):
                    m1_mul_m2[i,j] += m1[i,k]*m2[k,j]
        print('the mutiplication of m1 and m2 is:\n',m1_mul_m2)
    else:
        print('m1 cannot mulitiple m2, because the rows of m2 and the columns of m1 are not the same')

Matrix_multip(M1,M2)
print('the result from numpy calculation is:\n',np.dot(M1,M2))