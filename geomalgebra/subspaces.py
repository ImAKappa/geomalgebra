# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_subspaces.ipynb.

# %% auto 0
__all__ = ['calc_projection_vector', 'plot_dot_product', 'plot_bivector']

# %% ../nbs/01_subspaces.ipynb 2
import matplotlib.pyplot as plt
import numpy as np

# %% ../nbs/01_subspaces.ipynb 10
def calc_projection_vector(vec1: np.ndarray, vec2: np.ndarray) -> np.ndarray:
    """Calculate the projection vector of vec1 onto vec2"""
    vec2_magnitude = np.linalg.norm(vec2) 
    projection_magnitude = (np.dot(vec1, vec2) / vec2_magnitude)
    projection_direction = vec2 / vec2_magnitude
    projection_vec = projection_magnitude * projection_direction
    return projection_vec

# %% ../nbs/01_subspaces.ipynb 11
def plot_dot_product(vec1: np.ndarray, vec2: np.ndarray) -> plt.Figure:
    """Visualize the dot product"""
    fig, ax = plt.subplots(1, 1)
    origin = np.array([0, 0])
    colors = ('r', 'b')
    for color, vec in zip(colors, (vec1, vec2)):
        ax.quiver(*origin, *vec, scale=1, scale_units='xy', width=0.01, color=[color],
            label=f'len={round(np.linalg.norm(vec), 2)}'
        )
    try:
        projected_vector = calc_projection_vector(vec1, vec2)
        ax.quiver(*origin, *projected_vector, scale=1, scale_units='xy', width=0.01, color=['g'], 
            label=f'len={round(np.linalg.norm(projected_vector), 2)}'
        )
        projection_line = np.array([projected_vector, vec1]).T
        ax.plot(*projection_line)
        
    except ZeroDivisionError as zerr:
        print('Encountered zero division! Cannot plot projected vector')
    ax.set_title(f'Projection Vectors (Dot Product={np.dot(vec1, vec2)})')
    ax.set_aspect('equal')
    ax.set_xlim([-10., 10])
    return fig

# %% ../nbs/01_subspaces.ipynb 17
def plot_bivector(vec1: np.ndarray, vec2: np.ndarray) -> plt.Figure:
    """Plot a bivector given two vectors"""
    origin = np.array([0., 0.])
    vectors = (vec1, vec2, -vec1, -vec2)
    colors = ('r', 'g', 'b', 'y')
    fig, ax = plt.subplots(1, 1)
    for color, vec in zip(colors, vectors):
        ax.quiver(*origin, *vec, scale=1, scale_units='xy', width=0.02, color=[color])
        origin += vec
    ax.set_title('Bivector')
    ax.set_aspect('equal')
    return fig
