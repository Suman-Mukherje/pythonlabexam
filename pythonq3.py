
import pandas as pd
import numpy as np

iris = pd.read_csv('Iris.csv')
#print("Reading data from Iris.csv File")
#print(iris)
#print("Type of iris: "+ str(type(iris)))
#print(iris.head)
data =np.array(list(iris.columns))
print("Printing numeric attributes of iris data: ")
print(data)
target=list(iris['Species'])
print("Printing species of iris dataset:")
print(target)


