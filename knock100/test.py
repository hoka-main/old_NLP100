import numpy as np
from tqdm import tqdm
import time

x = np.logspace(-10, 9, 20)
print(x)
for i in tqdm(range(100)):
    time.sleep(0.05)

