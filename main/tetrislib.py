import numpy as np

def make_bar(bloks):
    bar = [0, 0, 0]
    for i in range(3):
        bar[i] = bloks[np.random.randint(2)]
    return bar

