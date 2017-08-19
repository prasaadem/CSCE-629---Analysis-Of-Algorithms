# Python 2.7.13
# OS: Macintosh
# Author: Aditya Emani - 524002563
# Course: CSCE 629 - Analysis of Algorithms - Fall 2016

# Matrix Chain Multiplication


import sys                                                                  # import sys
                                                                            #Main Definition
def main():
    matrix = [1,2,3]
    m = matrix_chain_multiplication(matrix)                                 #Call to matrix chain multiplication Method
    print 'The shortest cost for is: ', m[rc(1, len(matrix)-1)]             #Print the output of matrix chain multiplication to Console

def matrix_chain_multiplication(matrix):                                    # Definition of Matrix Chain Multiplication
    length = len(matrix)
    costMatrix = {}
    for x in xrange(1, length):
        costMatrix[rc(x, x)] = 0                                            #Set all the diagnol elements of matrix m to 0
    for x in xrange(2, length):                                             #Loop to fill the upper triangular matrix
        for a in xrange(1, length-1-x+2):                                   
            b = a+x-1
            costMatrix[rc(a, b)] = sys.maxint                               #Initialize each element with max int to compare below
            for c in xrange(a, b):
                cost = costMatrix[rc(a, c)] + costMatrix[rc(c+1, b)] + matrix[a-1] * matrix[c] * matrix[b]      #cost = cost of first portion + second portion + pqr 
                if cost < costMatrix[rc(a, b)]:                             #compare cost to store the least value
                    costMatrix[rc(a, b)] = cost
    return costMatrix                                                       #return costMatrix

def rc(i,j):
    return str(i) + ',' + str(j)                                            # returns index of matrix at an element like 2,3 or 1,1 as a string

#Call Main Definition to run program.
main()