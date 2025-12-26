import math
import errors

def mean(data):
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise errors.NoListError()
    
    if len(data) == 0:
        raise errors.VoidList()  
    
    #Calcul de la moyenne
    mean = 0.0
    for i in range(len(data)):
        mean += data[i]
        
    return mean / len(data)

def variance(data, sample=True):
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise errors.NoListError()
    
    if len(data) == 0:
        raise errors.VoidList()  
    
    #Calcul de la variance
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
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise errors.NoListError()
    
    if len(data) == 0:
        raise errors.VoidList()  
    
    #Calcul por l'écart-type
    if sample:
        return math.sqrt(variance(data))
    else:
        return math.sqrt(variance(data, sample))
    
def covariance(x, y):
    #Gestion des erreurs possibles
    if type(x).__name__ != "list" & type(y).__name__ != "list":
        raise errors.NoListError()
    
    if len(x) == 0 & len(y) == 0:
        raise errors.VoidList() 
    
    if len(x) != len(y):
        raise errors.NoEqualLengthError()

    #Calcul de la covariance
    covariance = 0.0
    mean_x = mean(x)
    mean_y = mean(y)
    length = len(x)
    for i in range(length):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)
    
    return covariance / length

def correlation(x, y):
    #Gestion des erreurs possibles
    if type(x).__name__ != "list" & type(y).__name__ != "list":
        raise errors.NoListError()
    
    if len(x) == 0 & len(y) == 0:
        raise errors.VoidList() 
    
    if len(x) != len(y):
        raise errors.NoEqualLengthError()
    
    #Calcul du coefficient de correlation
    return covariance(x, y) / (std_dev(x, False) * std_dev(y, False))

def correlation_matrix(dataset):
    #Détermination de la matrice de correlation
    matrix = {}
    for i in dataset.keys():
        for j in dataset.keys():
            key = f"Corr_{i}_&_{j}"
            matrix[key] = correlation(dataset[i], dataset[j])
    
    return matrix

#def histogram(data):
    