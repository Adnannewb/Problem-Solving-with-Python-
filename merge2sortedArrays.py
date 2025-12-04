nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
def mergesorted(nums1,nums2):
    i,j=0,0
    result=[]
    n,m=len(nums1),len(nums2)
    val=0
    while(i<n and j<m):
        
        if(nums1[i]<=nums2[j] ):
            val=nums1[i]
            i+=1
        else:
            val=nums2[j]
            j+=1
        if val not in result:
            result.append(val)
    
    while(i<n):
        if(nums1[i] not in result):
            result.append(nums1[i])
        i+=1
    
    while(j<m):
        if(nums2[j] not in result):
            result.append(nums2[j])
        j+=1
    return result
print(mergesorted(nums1,nums2))