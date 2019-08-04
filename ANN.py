import numpy as np

#sleep, study, stress
weights = np.array([0.5, 0.3, -0.2]).reshape(3, 1)


def s(p):
    s = 1/(1+np.exp(-p))
    return s


def predict(sleep, study, stress):
    inputs = np.array([[sleep],
                       [study],
                       [stress]])

    p = inputs.T.dot(weights)
    pred = s(p)
    return pred


sleep = float(input("sleep: "))
study = float(input("study: "))
stress = float(input("stress: "))

prediction = predict(sleep, study, stress)

print(prediction)
