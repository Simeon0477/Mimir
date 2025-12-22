"""
* dataset.py
* Gestion complète du cycle de vie des données
* Fontionnalités :
*  - Chargement de données
*  - Validation et nettoyage
*  - Opérations de filtrage
*  - Transformations
*  - Représentation des données
"""

#Fonction de lecture de fichier CSV
def load_csv(filepath, separator=',', encoding='utf-8'):
    with open(filepath, "r", encoding=encoding) as file:
        lines = file.readlines()   
    columns = lines[0].strip().split(separator)
    
    for line in lines[1:]:
        values = line.strip().split(separator)
        
    return dict(zip(columns, values))

#Fonction de lecture de fichier JSON 
def load_json(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        contain = file.read()
        
    return contain