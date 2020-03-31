import pandas as pd
import matplotlib.pyplot as plt
dt=pd.read_excel("pic_500.xlsx")
dt['ratio']=dt.unlabeled_size/500

fig = plt.figure(figsize=(8,5))
plt.plot(dt.ratio,dt.acc)
plt.title("Test accuracy vs the ratio of unlabeled data and labeled data")
plt.xlabel("number of unlabeled data as multiple of labeled data")
plt.ylabel("test accuracy")