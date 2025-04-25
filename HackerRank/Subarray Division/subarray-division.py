def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count