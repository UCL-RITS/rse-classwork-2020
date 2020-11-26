import subprocess
import numpy as np
from sagital_brain import run_averages

output = np.loadtxt('brain_average.csv', dtype=int, delimiter=',')
np.testing.assert_array_equal([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0], output)

cp = subprocess.run(["ls -lha"],shell=True)

cp