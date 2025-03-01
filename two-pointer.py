#Move Zeroes
sampleList = [0,1,0,3,12]
l,r = 0,1
while r < len(sampleList):
    if sampleList[r] != 0 :
        sampleList[l],sampleList[r] = sampleList[r],sampleList[l]
        l+=1
    r+=1
print(sampleList)