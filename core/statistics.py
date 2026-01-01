import math

def mean(data):
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise TypeError("The parameter 'data' should be a 'list'")
    
    if len(data) == 0:
        raise ValueError("The list is void")  
    
    #Calcul de la moyenne
    mean = 0.0
    for i in range(len(data)):
        mean += data[i]
        
    return mean / len(data)

def variance(data, sample=True):
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise TypeError("The parameter 'data' should be a 'list'")
    
    if len(data) == 0:
        raise ValueError("The list is void")  
    
    #Calcul de la variance
    variance = 0.0
    moyenne = mean(data)
    if sample:
        for i in range(len(data)):
            variance += (data[i] - moyenne)**2
            
        return variance / (len(data) - 1)
    else:
        for i in range(len(data)):
            variance += (data[i] - moyenne)**2
            
        return variance / len(data)
    
def std_dev(data, sample=True):
    #Gestion des erreurs possibles
    if type(data).__name__ != "list":
        raise TypeError("The parameter 'data' should be a 'list'")
    
    if len(data) == 0:
        raise ValueError("The list is void")  
    
    #Calcul por l'écart-type
    if sample:
        return math.sqrt(variance(data))
    else:
        return math.sqrt(variance(data, sample))
    
def covariance(x, y):
    #Gestion des erreurs possibles
    if type(x).__name__ != "list" and type(y).__name__ != "list":
        raise TypeError("The parameter 'data' should be a 'list'")
    
    if len(x) == 0 & len(y) == 0:
        raise ValueError("The list is void") 
    
    if len(x) != len(y):
        raise ValueError("The parameters 'x' and 'y' have differents lengths")

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
    if type(x).__name__ != "list" and type(y).__name__ != "list":
        raise TypeError("The parameter 'data' should be a 'list'")
    
    if len(x) == 0 & len(y) == 0:
        raise ValueError("The list is void") 
    
    if len(x) != len(y):
        raise ValueError("The parameters 'x' and 'y' have differents lengths")
    
    #Calcul du coefficient de correlation
    return covariance(x, y) / (std_dev(x, False) * std_dev(y, False))

def correlation_matrix(dataset):
    #Détermination de la matrice de correlation
    matrix = {}
    for i in dataset.keys():
        for j in dataset.keys():
            key = f"{i}_&_{j}"
            matrix[key] = correlation(dataset[i], dataset[j])
    
    return matrix

#def histogram(data):
    