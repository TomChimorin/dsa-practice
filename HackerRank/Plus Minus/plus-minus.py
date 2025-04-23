def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    neutral = 0
    for num in arr:
        if(num > 0):
            positive += 1
        elif(num < 0):
            negative += 1
        else:
            neutral += 1
            
    positiveRatio = positive/len(arr)
    negativeRatio = negative/len(arr)
    neutralRatio = neutral/len(arr)
    
    print(positiveRatio)
    print(negativeRatio)
    print(neutralRatio)