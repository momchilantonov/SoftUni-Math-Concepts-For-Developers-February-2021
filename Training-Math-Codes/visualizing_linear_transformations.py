from celluloid import Camera
from IPython.display import HTML
import matplotlib.pyplot as plt
import numpy as np


def get_colors(x_point, y_point):
    # Map x-y coordinates to rgb color
    red = min(1, 1-(y_point / y_axis_end))
    green = min(1, 1+(y_point / y_axis_end))
    blue = (1 / x_axis_end)+(x_point / x_axis_end ** 2)
    return red, green, blue


def generate_original_grid(x_start, x_end, x_samples, y_start, y_end, y_samples):
    # Create original grid in x-y space
    x_axis = np.linspace(x_start, x_end, x_samples)
    y_axis = np.linspace(y_start, y_end, y_samples)
    grid = np.column_stack([[x, y] for x in x_axis for y in y_axis])
    return grid


def generate_stepwise_transform(target_grid, grid, steps=30):
    # Create empty array of the right size
    transform_grid = np.zeros((steps+1,)+np.shape(grid))
    # Compute intermediate transforms
    for i in range(steps+1):
        intermediate = np.eye(2)+i / steps * (target_grid-np.eye(2))
        # Apply intermediate grid transformation
        transform_grid[i] = np.dot(intermediate, grid)
    return transform_grid


def plot_original_grid(grid, colors):
    # Plot grid grid
    plt.figure(figsize=(5, 5), facecolor="w")
    plt.scatter(grid[0], grid[1], s=36, c=colors, edgecolor="none")
    plt.axis("equal")
    plt.title("Original grid in x-y space")
    plt.grid()
    plt.show()


def plot_transformed_grids(transformed_array, color, title):
    # Create a series of figures showing the intermediate transforms
    steps = transformed_array.shape[0]
    # Set axis limits
    max_value = np.abs(transformed_array.max())
    # Plot individual frames
    for i in range(steps):
        plt.scatter(transformed_array[i,0], transformed_array[i,1], s=36, c=color, edgecolor="none")
        plt.scatter(transformed_array[i, 0], transformed_array[i, 1], s=36, c=color, edgecolor="none")
        plt.xlim(1.1 * np.array([-max_value, max_value]))
        plt.ylim(1.1 * np.array([-max_value, max_value]))
        plt.title(title)
        plt.grid()
        plt.draw()
        camera.snap()


# Plot original grid in x-y space
x_axis_start = -5
x_axis_end = 5
x_axis_samples = 11
y_axis_start = -5
y_axis_end = 5
y_axis_samples = 11
xy_grid = generate_original_grid(x_axis_start, x_axis_end, x_axis_samples, y_axis_start, y_axis_end, y_axis_samples)
points_colors = list(map(get_colors, xy_grid[0], xy_grid[1]))
plot_original_grid(xy_grid, points_colors)

# Plot animated transformed grid in u-v space
fig = plt.figure(figsize=(5, 5), facecolor="w")
camera = Camera(fig)
uv_grid = np.column_stack([[2, 1], [-1, 1]])
transform = generate_stepwise_transform(uv_grid, xy_grid)
plot_transformed_grids(transform, points_colors, "Transformed grid in u-v space")
animate = camera.animate()
animate.save("uvspace.gif")
HTML(animate.to_html5_video())

# Plot animated 60 degree clockwise rotation grid
fig = plt.figure(figsize=(5, 5), facecolor="w")
camera = Camera(fig)
theta = np.pi/3
rotation_60 = np.column_stack([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
transform = generate_stepwise_transform(rotation_60, xy_grid)
plot_transformed_grids(transform, points_colors, "Transformed grid\n60 degree clockwise rotation")
animate = camera.animate()
animate.save("rotation.gif")
HTML(animate.to_html5_video())

# Plot animated shear grid
fig = plt.figure(figsize=(5, 5), facecolor="w")
camera = Camera(fig)
shear = np.column_stack([[1, 0], [2, 1]])
transform = generate_stepwise_transform(shear, xy_grid)
plot_transformed_grids(transform, points_colors, "Transformed grid\nShear Matix")
animate = camera.animate()
animate.save("shear.gif")
HTML(animate.to_html5_video())

# Plot animated permutation grid
fig = plt.figure(figsize=(5, 5), facecolor="w")
camera = Camera(fig)
permutation = np.column_stack([[0, 1], [1, 0]])
transform = generate_stepwise_transform(permutation, xy_grid)
plot_transformed_grids(transform, points_colors, "Transformed grid\nPermutation")
animate = camera.animate()
animate.save("permutation.gif")
HTML(animate.to_html5_video())

# Plot animated projection grid
fig = plt.figure(figsize=(5, 5), facecolor="w")
camera = Camera(fig)
projection = np.column_stack([[1, 0], [0, 0]])
transform = generate_stepwise_transform(projection, xy_grid)
plot_transformed_grids(transform, points_colors, "Transformed grid\nProjection")
animate = camera.animate()
animate.save("projection.gif")
HTML(animate.to_html5_video())
