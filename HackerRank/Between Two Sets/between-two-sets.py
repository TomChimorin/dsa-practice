def getTotalX(a, b):
    # Write your code here
    lcm_a = reduce(lcm, a)
    gcd_b = reduce(math.gcd, b)
    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    return count
    
def lcm(x, y):
    return x * y // math.gcd(x, y)