def compareTriplets(a, b):
    # Write your code here
    alicePoint = 0
    bobPoint = 0
    
    for i in range(len(a)):
        if(a[i] > b[i]):
            alicePoint+=1
        elif(a[i] < b[i]):
            bobPoint+=1

    return [alicePoint, bobPoint]