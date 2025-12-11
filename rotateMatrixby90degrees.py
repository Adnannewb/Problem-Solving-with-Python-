matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#bruteforce solution
# def rotatetodegrees(matrix):
#     n=len(matrix)
#     result=[[0 for _ in range(n)]for _ in range(n)]
#     for i  in range(0,n):
#         for j in range(0,n):
#             result[j][n-1-i]=matrix[i][j]
#     return result
# updated_matrix=rotatetodegrees(matrix)
# for i in range(0,len(updated_matrix)):
#     for j in range(0,len(updated_matrix)):
#         print(updated_matrix[i][j],end=" ")
#     print()
    

#Optimal Solution
def rotatetodegrees(matrix):
    n=len(matrix)
    for i in range(0,n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(0,n):
        matrix[i].reverse()
        
    return matrix
rotatetodegrees(matrix)       
for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
        print(matrix[i][j],end=" ")
    print()