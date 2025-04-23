def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_nums = 0
    orange_nums = 0
    for i in range(len(apples)):
        if(a + apples[i] >= s and a + apples[i] <= t):
            apple_nums +=1
    for j in range(len(oranges)):
        if(b + oranges[j] >= s and b + oranges[j] <=t):
            orange_nums += 1
    print(apple_nums)
    print(orange_nums)