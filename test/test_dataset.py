from core.dataset import *

json_path = "data/samples/index.json"
csv_path = "data/samples/housing.csv"

df = load_csv(csv_path)

data = load_json(json_path)

#Affichage
for key in df.keys():
    print(df[key])

for d in data:
    print(d)