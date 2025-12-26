import math

def mean(data_list):
    if len(data_list) == 0:
        raise ValueError("La liste est vide !")
    return math.fsum(data_list) / len(data_list)

def variance(data_list, samples = True):
    if len(data_list) == 0:
        raise ValueError("Liste vide!")
    _mean = mean(data_list)
    total = math.fsum((li - _mean)**2 for li in data_list)
    if samples:
        return total / (len(data_list) - 1)
    else :
        return total / len(data_list)

def std_dev(data_list, samples = True):
    if len(data_list) == 0:
        raise ValueError("Liste VIde !")
    return math.sqrt(variance(data_list, samples))
    

def covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Impossible de calculer la COV dans ces conditions")
    
    mean_x = mean(x)
    mean_y = mean(y)

    return math.fsum((li - mean_x) * (lu - mean_y) for li,lu in zip(x,y)) / (len(x) - 1)

def correlation(x, y):
    varX = std_dev(x)
    varY = std_dev(y)
    if varX == 0 or varY == 0:
        raise ValueError("Math Error")
    return covariance(x,y) / (varX * varY)


def correlation_matrix(data):
    var = list(data[0])
    matrix = {v: {} for v in var}

    for v1 in var:
        for v2 in var:
            list1 = [row[v1] for row in data]
            list2 = [row[v2] for row in data]
            matrix[v1][v2] = correlation(list1, list2)
