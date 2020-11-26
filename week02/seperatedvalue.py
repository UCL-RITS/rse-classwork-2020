import numpy as np
import requests

spots = requests.get('http://www.sidc.be/silso/INFO/snmtotcsv.php', stream=True)

sunspots = np.genfromtxt(spots.raw, delimiter=';')

print(sunspots[0][3])

from matplotlib import pyplot as plt
plt.plot(sunspots[:,2], sunspots[:,3])