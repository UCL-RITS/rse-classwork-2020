import requests

response = requests.get("https://static-maps.yandex.ru/1.x/?size=400,400&ll=-0.1275,51.51&z=10&l=sat&lang=en_US",
                params={
                    'size': '400,400',
                    '11': '-0.1275,51.51',
                    'zoom': 10,
                    '1': 'sat',
                    'lang': 'en_US'
                })

print(response.content[0:50])

lines = ("\n")
lines[0:5]

