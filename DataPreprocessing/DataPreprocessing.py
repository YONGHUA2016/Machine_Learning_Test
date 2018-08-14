import numpy as np
import pandas as pd
import tensorflow as tf

fake_data = np.random.rand(1000,20)
fake_data = pd.DataFrame(fake_data)
dataname = 'datasest.csv'
fake_data.to_csv(dataname)

data = pd.read_csv(dataname)




