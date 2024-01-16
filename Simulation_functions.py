import Lattice
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# (Save it  to file)? and then draw - denote dog by the gray color and empty cell by the white color.
def visualize(lat, model: Lattice):
    '''Function for visualizing modified Lattice object
    returns heatmap'''
    color_map = {0: np.array([255, 255, 255]), # white
                 1: np.array([192, 192, 192])  # grey
                 } # 2: np.array([255, 0, 0]) red

    # Create a ListedColormap using the provided color_map
    custom_cmap = ListedColormap([color_map[key] / 255.0 for key in color_map])

    plt.imshow(lat, cmap=custom_cmap, interpolation='nearest')

    # add text annotations/labels for each element
    for i in range(lat.shape[0]):
        for j in range(lat.shape[1]):
            plt.text(j, i, str(lat[i, j]), ha='center', va='center', color='black')

    plt.title(f"L={model.size}, p={model.p}")
    plt.show()
