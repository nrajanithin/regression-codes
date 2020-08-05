import numpy as np
time = np.array([6,8,11,14,16,18,19])
temp = np.array([4,7,10,12,11.5,9,7])

beta = np.polyfit(time,temp,2)
p = np.poly1d(beta)

xp = np.linspace(6,19,100)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(time,temp,'bo',xp,p(xp),'-')
plt.show()




'''import matplotlib.pyplot as plt
plt.figure()
plt.plot(time,temp,'bo')
plt.xlabel('Time')
plt.ylabel('Temp')
plt.title('Temparature vs Time')
plt.show()'''
