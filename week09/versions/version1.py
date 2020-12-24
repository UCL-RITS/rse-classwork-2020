from visualisation import *
from processing import *

fs = ['81500.tab', '48151.tab', '62342.tab']
R=[]
R.append(analyse(preprocess(load(fs[0]),0.3)))
R.append(analyse(preprocess(load(fs[1]),0.3)))
R.append(analyse(preprocess(load(fs[2]),0.3)))

for i in range(3):
    save_figure(fu_map(R[i]))
