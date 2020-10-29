
import json

#print(my_group.items())
#print(json.dumps(my_group, indent=4))
group = {'Jill':{'Age':26,'Job':'biologist','Relationship':{'Zalika':'friend','John':'partner'}},
'Zalika':{'Age':28,'Job':'artist','Relationship':{'Jill':'friend'}},
'John':{'Age':27,'Job':'writer','Relationship':{'Jill':'partner'}},
'Nash':{'Age':34,'Job':'chef','Relationship':{'John':'cousin','Zalika':'landlord'}}}


my_group = []
#write something to page
with open('my_group.json', 'w') as f:
    json.dump(group, f, indent=4)


# read file and load
with open('my_group.json', 'r') as json_file:
    my_group = json_file.read()

mydata = json.loads(my_group)

print(my_group)
print(mydata)



