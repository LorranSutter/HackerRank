def is_leap(year):
    leap = False

    # Write your logic here
    if not year % 100:
        if not year % 400:
            leap = True
    elif not year % 4:
        leap = True

    return leap
