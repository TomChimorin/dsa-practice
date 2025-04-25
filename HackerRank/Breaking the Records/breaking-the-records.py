def breakingRecords(scores):
    # Write your code here
    lowestCount = 0
    highestCount = 0
    lowest = scores[0]
    highest = scores[0]
    for i in range (1, len(scores)):
        if scores[i] < lowest:
            lowest = scores[i]
            lowestCount += 1
        elif scores[i] > highest:
            highest = scores[i]
            highestCount += 1
    return(highestCount, lowestCount)