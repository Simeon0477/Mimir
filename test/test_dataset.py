from core.dataset import *

#Chemin d'accès des fichiers
json_path = "data/samples/index.json"
json_path2 = "data/samples/object.json"
csv_path = "data/samples/housing.csv"

#Chargement des données
df = load_csv(csv_path)
data = load_json(json_path) #Cas d'une liste de String
data2 = load_json(json_path2, is_object=True) #Cas d'une liste de d'Object

#Affichage des données du fichier csv
print("----- Contenu du CSV -----")
for key in df.keys():
    print(f"{key} : {df[key][:10]}")
print("\n")

#Affichage des données du fichier json
print("----- Contenu du JSON -----")
print("-> Cas d'une liste de listes")
for d in data:
    print(d)
print("\n")

print("-> Cas d'une liste d'object")
for d in data2:
    for key in d.keys():
        print(f"{key} : {d[key]}")
    print("\n")
print("\n")