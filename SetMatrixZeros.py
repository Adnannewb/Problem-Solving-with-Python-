matrix=[[7,9,8,3],[2,1,0,4],[5,0,6,2],[9,1,8,7]]

#Brute force
# def markinfinity(matrix,rows,cols):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(0,r):
#         if(matrix[i][cols]!=0):
#             matrix[i][cols]=float("inf")
#     for j in range(0,c):
#         if(matrix[rows][j]!=0):
#             matrix[rows][j]=float("inf")

# def setzeros(matrix):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(0,r):
#         for j in range(0,c):
#             if(matrix[i][j]==0):
#                 markinfinity(matrix,i,j)
#     for i in range(0,r):
#         for j in range(0,c):
#             if(matrix[i][j]==float("inf")):
#                 matrix[i][j]=0
    
#     for i in range(0,r):
#         for j in range(0,c):
#             print(matrix[i][j],end=" ")
#         print("")
            
# setzeros(matrix)       

#Optimal Solution
r=len(matrix)
c=len(matrix[0])
rowtrack=[0]*r
coltrack=[0]*c
for i in range(0,r):
    for j in range(0,c):
        if(matrix[i][j]==0):
            rowtrack[i]=-1
            coltrack[j]=-1
for i in range(0,r):
    for j in range(0,c):
        if(rowtrack[i]==-1 or coltrack[j]==-1):
            matrix[i][j]=0
            
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()      