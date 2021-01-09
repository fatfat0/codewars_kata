# 1st way (faster)
def index(array, n):
    try:
        number = array[n]
    except IndexError:
        return -1
    return number ** n

# 2nd way


def index(array, n):
    if len(array) < n+1:
        return -1
    else:
        number = array[n]
        return number ** n
