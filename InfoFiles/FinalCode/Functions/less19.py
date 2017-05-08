def distance_from_zero(name):
    if type(name)==int or type(name)==float:
        return abs(name)
    else:
        return "Nope"

distance_from_zero(-2.2)
