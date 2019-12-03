import pandas as pd
import cv2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import time

time.sleep(1)
sizes = [4, 8, 6]
labels = 'Count 1 = '+ str(sizes[0]),'Count 2 = '+ str(sizes[1]), 'Count 3 = '+ str(sizes[2])

colors = ['red', 'yellow', 'green']
explode = (0.02, 0.03, 0.04)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()