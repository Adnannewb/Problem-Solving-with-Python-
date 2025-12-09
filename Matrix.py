nums=[[5,20,3],[7,-9,10],[1,-52,6]]
rows=len(nums)
cols=len(nums[0])

#Print matrix
for i in range(0,rows):
    for j in range(0,cols):
        print(nums[i][j] ,end=" ")
    print()

# #print upper triangle of matrix:
# for i in range(0,rows):
#     for j in range(0,cols):
#         if(j>=i):
#             print(nums[i][j] ,end=" ")
#         else:
#             print("*",end=" ")
#     print()
    
# #Print lower triangle of matrix
# for i in range(0,rows):
#     for j in range(0,cols):
#         if(j<=i):
#             print(nums[i][j] ,end=" ")
#         else:
#             print("*",end=" ")
#     print()

# #Print the diagonal matrix
# for i in range(0,rows):
#     for j in range(0,cols):
#         if(j==i):
#             print(nums[i][j] ,end=" ")
#         else:
#             print("*",end=" ")
#     print()


#Transpose of a matrix 
print("")
result=[[0]*rows for  _ in range(cols)]
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i]=nums[i][j]

for i in range(0,len(result)):
    for j in range(0,len(result[0])):
        print(result[i][j] ,end=" ")
    print()