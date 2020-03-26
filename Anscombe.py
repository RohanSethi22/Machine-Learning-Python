import numpy as np
import matplotlib.pyplot as plt

x1=[10,8,13,9,11,14,6,4,12,7,5]
y1=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x2=[10,8,13,9,11,14,6,4,12,7,5]
y2=[9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]

x3=[10,8,13,9,11,14,6,4,12,7,5]
y3=[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

x4=[8,8,8,8,8,8,8,19,8,8,8]
y4=[6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0,20])
ax.set_ylim([0,20])

plt.xlim(0,20)
plt.ylim(0,20)
#plt.scatter(x1,y1) #
#plt.scatter(x2,y2,color='red') #color='red'
#plt.scatter(x3,y3,color='green') #color='red'
plt.scatter(x4,y4,color='brown') #color='red'

tx1=x4
ty1=y4
tx1=tx1-np.mean(x4)
ty1=ty1-np.mean(y4)
temp1=tx1*ty1
temps1=tx1*tx1
n, d = sum(temp1), sum(temps1)
if d==0:
  	pass
else:
   	slope=n/d
   	intercept=np.mean(y4)-slope*np.mean(x4)
   	xval=np.array([0,20])
   	yval=xval*slope+intercept
   	plt.plot(xval,yval)

fig.canvas.draw()

plt.show()
print(x2,y2)