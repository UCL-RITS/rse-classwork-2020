house = {
    'living' : {
        'exits': {
            'north' : 'kitchen',
            'outside' : 'garden',
            'upstairs' : 'bedroom'
        },
        'people' : ['Graham'],
        'capacity' : 2
    },
    'kitchen' : {
        'exits': {
            'south' : 'living'
        },
        'people' : [],
        'capacity' : 1
    },
    'garden' : {
        'exits': {
            'inside' : 'living'
        },
        'people' : ['David'],
        'capacity' : 3
    },
    'bedroom' : {
        'exits': {
            'downstairs' : 'living',
            'jump' : 'garden'
        },
        'people' : [],
        'capacity' : 1
    }
}

{name: room['capacity'] for name, room in house.items()}
{name: len(room['people']) for name, room in house.items() if len(room['people']) > 0}

capacity = 0
occupancy = 0
for name, room in house.items():
    capacity += room['capacity']
    occupancy += len(room['people'])
print(f"House can fit {capacity} people, and currently has: {occupancy}.")