import json

mydata = {'key': ['value1', 'value2'],
            'key2': {'key4':'value3'}}

print(json.dumps(mydata, indent=4))

import yaml

