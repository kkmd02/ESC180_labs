##Problem 1
#Write a function with the signature def list1_start_with_list2(list1, list2), which returns True iff list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2. Note: len(lis) is the length of the list lis, i.e., the number of elements in lis.

def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2): #list1 must be >= list2
        for ind in range (len(list2)): #[0,len) so will not include last length
            if list1[ind] == list2[ind]:
                ind += 1
            else:
                return False
        return True #will return if does not return false
    else:
        return False

A=[1, 5, 6, 7, 8, 9, 0]
B=[1, 5, 6]

list1_start_with_list2(A, B)

##Problem 2
#Write a function with the signature def match_pattern(list1, list2) which returns True iff the pattern list2 appears in list1. In other words, we return True iff there is an i such that 0≤i≤len(list1)-len(list2) and

def match_pattern(list1, list2):
    if len(list2) <= len(list1): #list 1 must be bigger
        ind1 = 0
        while ind1 < len(list1): #ind1 is the index of list 1
            ind2 = 0
            ind1_if = ind1 #ind1_if is ind1 within the if block so can change it without changing ind1
            while ind2 < len(list2): #ind2 is the intex of list 2
                if list1[ind1_if] == list2[ind2]:
                    if ind2 == len(list2) - 1:
                        return True #because at end of list2
                    ind1_if += 1
                    ind2 += 1
                else:
                    ind2 = len(list2) #will stop this loop from running
                    continue #will restart the loop
            ind1 += 1
        return False
    else:
        return False

A = [1, 5, 6, 7, 2, 9, 0]
B = [6, 2, 9, 0]

match_pattern(A, B) #i realized this doesn't work for more than 2

##Problem 3
#Write a function with the signature def repeats(list0), which returns True iff list0 contains at least two adjacent elements with the same value.

def repeats(list0):
    ind = 0
    while ind + 1 < len(list0):
        if list0[ind] == list0[ind + 1]:
            return True
        else:
            ind += 1
    return False

A = [0, 1, 2, 2, 4, 5]

repeats(A)

##Problem 4a
#Write a function with the signature def print_matrix_dim(M) which accepts a matrix M in the format above, and prints the matrix dimensions. For example, print_matrix_dim([[1,2],[3,4],[5,6] ]) should print 3x2.

def print_matrix_dim(M):
    rows = len(M)
    columns = len(M[1]) #assuming all of the rows have the same number of columns
    print (rows, 'x', columns)

M = [[5,  6, 7],
     [0, -3, 5]]

print_matrix_dim(M)

##Problem 4b
#Write a function with the signature def mult_M_v(M, v) which returns the product Mv of a matrix M and a vector v. Vectors are stored as lists of floats.
#To write this function, you will need to create a new vector. Here are two ways to create a new vector (stored as a list) with 10 zeros in it:

ten_zeros1 = [0]*10

ten_zeros2 = []
for i in range(10):
  ten_zeros2.append(0)

def mult_M_v(M, v):
    list_mult_M_v = []
    if len(M[0]) == len(v):
        ind_M_row = 0
        ind_M_column = 0
        while ind_M_row < len(M):
            ind_v = 0
            ind_M_column = 0
            summation = 0
            while ind_v < len(v) and ind_M_column < len(M[0]):
                summation += M[ind_M_row][ind_M_column] * v[ind_v] #can use same var
                ind_M_column += 1
                ind_v += 1
            ind_M_row += 1
            list_mult_M_v.append (summation)
        return list_mult_M_v
    else:
        print ('Undefined')

M = [[1, 2, 3],
    [4, 5, 6]]

v = [1, 2, 3]

mult_M_v(M, v) # [14, 32] 1*1 + 2*2 + 3*3, 1*4 + 2*5 + 3*6

##Problem 4c
#multiply Matrices

def mult_M1_M2(M1, M2):
    ind_M1_row = 0
    ind_M1_column = 0
    ind_M2_row = 0
    ind_M2_column = 0
    if len(M1[0]) == len(M2):
        while ind_M1_row < len(M):
            pass
    else:
        print ('Undefined')
