def timeConversion(s):
    # Write your code here
    period = s[-2:]
    hour = int(s[:2])
    rest = s[2:-2]
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    return f'{hour:02d}{rest}'