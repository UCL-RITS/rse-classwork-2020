import json

def load_data(filepath):
    f = open(filepath, 'r')
    data=f.read()
    obj = json.loads(data)
    print("usd: " + str(obj['usd']))

load_data("/Users/indie/Documents/Github/RSE-Classwork/week05/example.json")