
"""
x=np.array([1,2,3])
y=np.array([4,5,6])
ad=[np.sum((x,y),axis=0)]
print(ad)

#np.zeros(3,3,int)


sam=np.array([34,65,12,23,10,5,100,3])

print(sam[np.argsort(sam)[-2:][::-1]])


import numpy as np
x=np.arange(0,10)
y=np.arange(0,10)
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X vs Y")

"""

from matplotlib import pyplot as plt

dict={"fruits":10,"flowers":30,"leaves":50,"coconuts":10}

names=list(dict.keys())
values=list(dict.values())

plt.bar(names,values)

plt.xlabel("names")
plt.ylabel("values")
plt,title("names vs values")

