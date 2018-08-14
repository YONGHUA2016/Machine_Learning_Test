import numpy as np
import pandas as pd
import tensorflow as tf

fake_data = np.random.rand(1000,20)

data = pd.read_csv('dataset.csv')

print data.size(0)


