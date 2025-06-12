import math as m

def equalize(a,b):
    try:
        y=m.sqrt(((a + b) ** 3)/(a - b) ** 2)
    except ZeroDivisionError:
        result ="c"
        raise ZeroDivisionError
    except ValueError:
        result = "dsjh"
    except TypeError:
        result = "cush"  
    else:
        result = round(y, 4)
    return result
