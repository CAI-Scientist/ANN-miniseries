import numpy as np

sleep = 12
study = 4
stress = 10

xs = np.array([[sleep],
               [study],
               [stress]])

#sleep, study, stress
ws = np.array([0.5, 0.3, -0.2]).reshape(3, 1)

p = xs.T.dot(ws)
s = 1/(1+np.exp(-p))
prediction = s*100
print(prediction)
