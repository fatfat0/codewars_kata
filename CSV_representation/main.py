def toCsvText(array):
    result = []
    for line in array:
        result.append(','.join([str(i) for i in line]))
    return '\n'.join(result)
