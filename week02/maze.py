house = {
    'living': {
        'exits': {
            'north': 'kitchen',
            'outside': 'garden',
            'upstairs': 'bedroom'
        },
        'people': ['James'],
        'capacity': 2
    },
    'kitchen': {
        'exits': {
            'south': 'living'
        },
        'people': [],
        'capacity': 1
    },
    'garden': {
        'exits': {
            'inside': 'living'
        },
        'people': ['Sue'],
        'capacity': 3
    },
    'bedroom': {
        'exits': {
            'downstairs': 'living',
            'jump': 'garden'
        },
        'people': [],
        'capacity': 1
    }
}

import json

with open('maze.json', 'w') as json_maze_out:
    json_maze_out.write(json.dumps(house))
