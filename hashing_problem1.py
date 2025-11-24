n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
#question : print the m element frequency in  n list
# constraints:
#     1.1<=n[i]<=10
#     2.n can have 10^8 elements
#     3.m can have 10^8 elements


#Brute Force
# for num in m:
#     count=0
#     for x in n:
#         if(num==x):
#             count+=1      #but this brute for will show TLE ,check the constraints you will get it.
#     print(count)        
        


#Optimal Solution

# hashlist=[0]*11
# for num in n:
#     hashlist[num]+=1
# for x in m:                #It will not show TLE   
#     if(x<1 or x>10):       #but if we dont know the size of n list there will have been an issue
#         print(0)
#     else:
#         print(hashlist[x])        


#using Dictionary 
freq_map=dict()
for num in n:
    if(num in freq_map):
        freq_map[num]+=1
    else:
        freq_map[num]=1    #it will not have any issues to solve this problem
for num in m:
    if(num in freq_map):
        print(freq_map[num])
    else:
        print(0)           
        
