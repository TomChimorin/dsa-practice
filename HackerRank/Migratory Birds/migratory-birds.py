def migratoryBirds(arr):
    # Write your code here
    count = Counter(arr)
    return min(count, key=lambda x: (-count[x], x))
