import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array.shape)
print(my_array[0])

my_new_array = np.zeros(5)
print(my_new_array)
my_new_array_2 = np.ones(5)
print(my_new_array_2)
my_random_array = np.random.random(5)
print(my_random_array)

my_2d_array = np.zeros((2, 3))
print(my_2d_array)
my_2d_array_new = np.ones((2, 4))
print(my_2d_array_new)

my_array = np.array([[4,5], [6,7]])
print(my_array)
print(my_array.shape)
my_array_column2 = my_array[:, 1]
print(my_array_column2)
my_array_row1 = my_array[0,:]
print(my_array_row1)

a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a/b
print("sum = " , sum)
print("difference = " , difference)
print("product = " , product)
print("quotient = " , quotient)