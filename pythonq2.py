

import numpy as np

low = int(input("Enter lower limit of list:"))
high = int(input("Enter upper limit of list:"))

random_list = np.random.randint(low, high, 24)
print("The generated list of 26 numbers is: ")
print(random_list)

array = np.array(random_list)

matrix = array.reshape(6, 4)
print("Original matrix:")
print(matrix)

transpose = matrix.transpose()
print("Transpose of the matrix:")
print(transpose)


