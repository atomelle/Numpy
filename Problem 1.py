import numpy as np

x = np.random.random((5,5))
print (x)

y = x.mean()
print (' ')
print ("Value of the mean is: ", y)

a = x.std()
print (' ')
print("Value of the standard deviation is: ", a)

Z = (x - y)/a
print (' ')
print ("Value of the normalized X is: ", Z)