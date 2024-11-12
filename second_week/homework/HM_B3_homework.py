import numpy as np
# create an n rows and m columns by random
n = int(input("Enter the rows of the matrix : "))
#m=3
#n=3

m = int(input("Enter the columns of the matrix : "))

arr = np.random.randint(-10,10,size=(n,m))
"""
arr = []

# Prompt the user to enter values row by row
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"Enter value for position ({i},{j}): "))
        row.append(value)
    arr.append(row)
"""

# Convert the list to a NumPy array
arr = np.array(arr)
# calculate the sum of the main diagonal and secondary diagonal in square matrix
def sum_diagonals(arr):
    sum_of_diagonal =0
    for i in range(n) :
        sum_of_diagonal+=arr[i][i] # sum  the main diagonal
        sum_of_diagonal+= arr[i][n-i-1]# sum of the secondary diagonal
    return sum_of_diagonal

 #  Convert negative elements to absolute values
def convert_negatives_to_absolute(arr):
    return np.abs(arr)

# Replace even numbers in matrix with a given number
def replace_even_numbers(arr,x):
    return np.where(arr%2==0,x,arr)

# check if all elements in matrix are even 
def is_all_even(arr):
    if np.all(arr%2==0)== False:
        print(" the array doesn't contain all even numbers")

    else :
        print(" the array contains all even numbers")
# check symmetric matrix
def is_symmetric_matrix(arr):
    for i in range(n):
        for j in range(i,n):
            if arr[i][j]!=arr[j][i]:
                return False
    return True


# display array
def display(arr):
    for row in arr:
        print("  ".join(map(str, row)))

# is this array's the main diagonal in ascending order
def is_main_diagonal_asc(arr):
    for i in range(n-1):
        for j in range(i,n):
            if arr[i][i]>=arr[i+1][i+1]:
                return False
    return True

# is the secondary diagonal is descending
def is_secondary_diagonal_des(arr):
    for i in range(n-1):
        if arr[i][n-i-1]<= arr[i+1][n-(i+1)-1] :
            return False
    return True

#show the array
print("this is random array:")
display(arr)

# calculates the sum of the diagonals
sum_of_diagonal_of_matrix= sum_diagonals(arr)
print("the sum of both the main diagonal and the secondary diagonal: ",sum_of_diagonal_of_matrix)
#replacing even numbers:
arr=  replace_even_numbers(arr,60)
print("this is array after replacing even numbers:")
display(arr)

#converting negatives to absolute
print("this is array after converting negatives to absolute")
#convert_negatives_to_absolute(arr)
#display(arr)

# check if all elements are even
is_all_even(arr)

# check symmetric matrix
if is_symmetric_matrix(arr) :
    print("This array is symmetric array")
else :
    print("This array isn't symmetric array")

# is the main diagonal in ascending order
if is_main_diagonal_asc(arr) :
    print("The main diagonal is in ascending order")
else :
    print("The main diagonal isn't in ascending order ")

#is the secondary diagonal in descending order
if is_secondary_diagonal_des(arr) :
    print("The secondary diagonal is in descending order")
else :
    print("The secondary diagonal isn't in descending order")







