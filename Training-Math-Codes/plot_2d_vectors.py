import matplotlib.pyplot as plt
import numpy as np


# some tests
# vectors = [
#     [1, 1, -2, 3],
#     [2, 1, -2.5, 1.5],
#     [-3.2, -1.5, 0, 4.3]
# ]
#
# vectors_array = np.array(vectors)
#
# for row in vectors_array:
#     row[2] = row[2]-row[0]
#     row[3] = row[3]-row[1]

# x_points = []
# y_points = []
# for row in vectors_array:
#     x_points.extend([row[0], row[2]])
#     y_points.extend([row[1], row[3]])


# Solution for plotin vectors
def plot_vectors(vectors, colors, title):
    vectors_array = np.array(vectors)
    start_x, start_y, end_x, end_y = zip(*vectors_array)
    length_x = tuple(end_x[i]-start_x[i] for i in range(len(start_x)))
    length_y = tuple(end_y[i]-start_y[i] for i in range(len(start_y)))
    x_points = [x[::2] for x in vectors_array]
    y_points = [y[1::2] for y in vectors_array]
    min_x, max_x = np.amin(x_points)-1, np.amax(x_points)+1
    min_y, max_y = np.amin(y_points)-1, np.amax(y_points)+1
    plt.quiver(start_x, start_y, length_x, length_y, angles="xy", scale_units="xy", scale=1, color=colors)
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.xticks(np.arange(min_x, max_x, step=1), rotation=45)
    plt.yticks(np.arange(min_y, max_y, step=1), rotation=45)
    plt.xlabel("X", loc="center", color="mediumslateblue", fontsize="x-large")
    plt.ylabel("Y", loc="center", color="mediumslateblue", fontsize="x-large")
    plt.gca().set_aspect("equal")
    plt.grid()
    plt.title(title)
    plt.show()


# plot_vectors([[0, 0, 2, 3]], ["red"], "One vector")
# plot_vectors([[0, 0, 1, 0], [0, 0, 0, 1]], ["red", "blue"], "Two orthogonal vectors")
# plot_vectors([[1, 1, -2, 3], [2, 1, -2.5, 1.5], [-3.2, -1.5, 0, 4.3]], ["red", "blue", "orange"], "Three arbitrary")

def find_linear_combination_coefficients(e1, e2, v):
    basis_vectors_array = np.transpose(np.array([e1, e2]))
    required_coefficients = np.linalg.solve(basis_vectors_array, v)
    return required_coefficients


e1, e2 = [[1, 0], [0, 1]]
v = [3.5, 8.6]
# Find the unknown coefficients. Extract the logic in a function.
# It should accept the two basis vectors and the one we need to represent
# and should return the two coefficients
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
# Plot the three vectors
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"], "Three arbitrary vectors")
