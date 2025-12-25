import math
import statistics

def mean(data):
    mean = 0.0
    for i in range(len(data)):
        mean += data[i]
        
    return mean / len(data)

def variance(data, sample=True):
    variance = 0.0
    mean = mean(data)
    if sample:
        for i in range(len(data)):
            variance += (data[i] - mean)**2
            
        return variance / (len(data) - 1)
    else:
        for i in range(len(data)):
            variance += (data[i] - mean)**2
            
        return variance / len(data)
    
def std_dev(data, sample=True):
    if sample:
        return math.sqrt(variance(data))
    else:
        return math.sqrt(variance(data, sample))
    
def covariance(x, y):
    if len(x) != len(y):
        print("Longueur des listes différentes") 
        return None

    covariance = 0.0
    mean_x = mean(x)
    mean_y = mean(y)
    length = len(x)
    for i in range(length):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)
    
    return covariance / len

def correlation(x, y):
    