#code starts here
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import matplotlib as mpl
fig, ax = plt.subplots()
df = pd.read_ods("Object.ods")
df
plt.scatter(df.x,df.y)
plt.show()
