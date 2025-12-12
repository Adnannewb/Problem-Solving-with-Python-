matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
rows=len(matrix)
cols=len(matrix[0])
top,left=0,0
bottom=rows-1
right=cols-1
result=[]
while(top<=bottom and right>=left):
    for i in range(left,right+1):
        result.append(matrix[top][i])
    top+=1
    for i in range(top,bottom+1):
        result.append(matrix[i][right])
    right-=1
    if(top<=bottom):
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
        bottom-=1
    if(left<=right):
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left+=1
    
print(result)