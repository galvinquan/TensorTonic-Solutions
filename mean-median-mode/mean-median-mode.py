import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = sorted(x)
    mean = sum(x)/len(x)
    if len(x)%2==0:
        median = (x[(len(x)//2)-1]+x[len(x)//2])/2
    else:
        median = x[len(x)//2]
    dem = Counter(x)
    sorted_dict = dict(sorted(dem.items(), key=lambda item: (-item[1], item[0])))
    mode = list(sorted_dict)[0]
    return float(mean), float(median), float(mode)