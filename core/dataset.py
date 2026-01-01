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
    
    data = {col : [] for col in columns}
    for line in lines[1:]:
        row = line.strip().split(separator)
        if len(row) != len(columns):
            raise ValueError("CSV mal formé")
        
        for col, val in zip(columns, row):
            data[col].append(val)
        
    return data

#Fonction de lecture de fichier JSON 
def load_json(file_path, is_object=False):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not (text.startswith("[") and text.endswith("]")):
        raise ValueError("Le JSON n'est pas une liste")

    content = text[1:-1].strip()
    if not content:
        return []

    return (
        _parse_object_list(content)
        if is_object
        else _parse_string_list(content)
    )
    
#Parseur pour les listes de chaines de caractères
def _parse_string_list(text):
    elements = []
    buffer = ""
    in_string = False
    escape = False

    for c in text:
        if in_string:
            if escape:
                buffer += c
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
                elements.append(buffer)
                buffer = ""
            else:
                buffer += c
        else:
            if c == '"':
                in_string = True

    if in_string:
        raise ValueError("JSON mal formé : chaîne non fermée")

    return elements

#Parseur pour les listes d'objets
def _parse_object_list(text):
    objects = []
    buffer = ""
    level = 0
    in_string = False
    escape = False

    for c in text:
        if in_string:
            buffer += c
            if escape:
                escape = False
            elif c == "\\":
                escape = True
            elif c == '"':
                in_string = False
            continue

        if c == '"':
            in_string = True
            buffer += c
            continue

        if c == "{":
            if level == 0:
                buffer = ""
            level += 1

        if level > 0:
            buffer += c

        if c == "}":
            level -= 1
            if level == 0:
                objects.append(buffer)

    if level != 0 or in_string:
        raise ValueError("JSON mal formé : accolades ou chaînes non fermées")

    if not objects:
        raise ValueError("Aucun objet JSON détecté")
    
    parsed = [parse_object_string(s) for s in objects]

    return parsed

def parse_object_string(obj_str):
    obj_str = obj_str.strip()
    # On supprime les sauts de ligne et espaces inutiles
    obj_str = obj_str.replace("\n", "").replace("  ", "")
    
    obj_dict = {}
    # Cette version naïve ne gère que "clé": valeur simple (string, number, null)
    pairs = obj_str[1:-1].split(",")
    for pair in pairs:
        key, val = pair.split(":", 1)
        key = key.strip().strip('"')
        val = val.strip()
        if val == "null":
            val = None
        elif val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        else:
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
        obj_dict[key] = val
    return obj_dict