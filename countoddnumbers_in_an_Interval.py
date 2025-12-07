low=4
high=7
if(low%2==0 and high%2==0):
    count=(high-low)/2
elif(low%2!=0 and high%2!=0):
    count=(high-low)/2 +1 
else:
    count=(high-low+1)/2
print(int(count))