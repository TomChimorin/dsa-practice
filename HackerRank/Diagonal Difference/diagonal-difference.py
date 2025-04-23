def diagonalDifference(arr):
    # Write your code here
    rightDiagonal = 0
    leftDiagonal = 0
    for i in range(len(arr)):
        rightDiagonal += arr[i][i]
        leftDiagonal += arr[i][len(arr) - 1 - i]
    return abs(rightDiagonal - leftDiagonal)