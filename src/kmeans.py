import os
import pathlib
import numpy as np
import keras
from keras import layers
from tensorflow import data as tf_data
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot_image(image, label, title=None, cmap='gray'):
    """
    Plots a single image (flattened vector) with its cluster label.

    Args:
        image: A flattened image vector (1D array).
        label: The cluster label assigned to the image.
        title: Optional title for the plot.
        cmap: Optional colormap for the image (default 'gray' for grayscale).
    """
    # Reshape the image vector to its original dimensions (assuming 16x16)
    image_reshaped = image.reshape(16, 16, 3)

    # Create the plot
    plt.imshow(image_reshaped, cmap=cmap)
    plt.title(f"Cluster: {label}" if title is None else title)
    plt.axis('off')  # Hide axes for better visualization
    plt.show()

def WCSS_Elbow_Analysis(data_flattened):
    # Define a range of k values to explore
    k_range = range(2, 16)  # Example range, adjust as needed

    # Create a list to store WCSS values
    wcss_list = []

    for k in k_range:
        # Create and fit the k-means model
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data_flattened)

        # Get the WCSS value from the inertia_ attribute
        wcss = kmeans.inertia_
        wcss_list.append(wcss)

    # Plot the elbow curve (using matplotlib or other plotting library)
    import matplotlib.pyplot as plt

    plt.plot(k_range, wcss_list)
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("WCSS")
    plt.title("Elbow Method for KMeans Clustering")
    plt.show()

