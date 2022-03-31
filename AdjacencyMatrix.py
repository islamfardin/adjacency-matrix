n = [[0,1,4],[1,0,2,3,4],[2,1,3],[3,1,2,4],[4,0,1,3]]

def adj_matrix():
    
    matrix = []
    length = len(n) # finds length of the original matrix
    for i in range(length):    # using a for loop, finds range of matrix length
        matrix.append([0]*length)    # adds to end of new matrix by multyplying length with each iteration
        for y in n[i]: # using for loop for previous iteration
            matrix[i][y] = 1 # multiplying by 1 to replace vertexes that need 1
    print(matrix)

adj_matrix()