def load_csv (file_path, separator = ',', encoding = 'utf-8'):
    with open(file_path, 'r', encoding) as file:
        file_list = []
        for line in file:
            line = line.strip()
            if line == "":
                continue
            sep = line.split(separator)
            file_list.append(sep)
        return file_list

def load_json(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as _json:
        file_list = []
        in_chain = False
        temp_json_text = ""
        text = _json.read()
        text = text.strip()
        if text[0] == "[":
            if text[-1] == "]":
                print("liste JSON, traitement en cours...")
                for c in text:
                    if c == "\"":
                        temp_json_text += c





def validateData(strict = True):


def cleanData (strategy='remove'):


def filterBy (condition: callable):


def normalize(methods = 'minmax', column = 'none'):


def getStats():


def exportCsv(file_path):

