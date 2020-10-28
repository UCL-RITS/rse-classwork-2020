# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:23:21 2020

@author: User
"""

import json
import requests

response=requests.get("https://raw.githubusercontent.com/DavidScobie/friend-group-2020/main/group.py").text
my_group_file=json.dumps(response)
print(my_group_file)
