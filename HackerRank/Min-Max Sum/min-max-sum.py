def miniMaxSum(arr):
    # Write your code here
    totalMin = 0
    totalMax = 0
    sortedArray = sorted(arr)
    for i in range(len(arr) - 1):
        totalMin += sortedArray[i]
    for j in range(1, len(arr)):
        totalMax += sortedArray[j]
        
    print(totalMin, totalMax)