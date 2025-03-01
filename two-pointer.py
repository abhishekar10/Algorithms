#Move Zeroes
sampleList = [0,1,0,3,12]
l,r = 0,1
while r < len(sampleList):
    if sampleList[r] != 0 :
        sampleList[l],sampleList[r] = sampleList[r],sampleList[l]
        l+=1
    r+=1
# print(sampleList)

#Finding two lines storing most water
c = [1,8,6,2,5,4,8,3,7] #c short for container
n,x = 0,0
l,r = 0,len(c)-1 #n for minimum and x for maximum
a = 0 #a for area
while l <= r:
    ta = min(c[l],c[r])*(r-l)
    a = max(a,ta)
    if(c[l] < c[r]):
        l+=1
    else:
        r-=1
print(a)