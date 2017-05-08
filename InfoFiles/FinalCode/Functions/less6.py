def cube(number):
    return number*number*number
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
cube(99)
by_three(99)
