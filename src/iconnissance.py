"""
Title: Iconnissance
Author: Henry Fan
Description: A simple vision system for detecting and classifying icons of common video game items. Examples include potions, scrolls, books, swords, and more
"""

# Setup Code
import os
import pathlib
import numpy as np
import keras
from keras import layers
from tensorflow import data as tf_data
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import kmeans as iconissancekmeans
import directoryhandler
from PIL import Image


def initialSetUp():
    src_path = os.path.abspath('../src')
    pixel_art_dataset_path = os.path.abspath('../PixelArtDataset')
    results_path = os.path.abspath('../Results')
    print("src path: " + src_path)
    print("dataset path: " + pixel_art_dataset_path)
    print("results path: " + results_path)
    labels = os.path.abspath(pixel_art_dataset_path + '/sprites_labels.npy')
    pixelartimages = os.path.abspath(pixel_art_dataset_path + '/sprites.npy')
    print(labels)
    # with np.load(labels) as data:
    #     a = data['a']
    labelsarray = np.load(labels)
    labelsarray.ndim
    print("Labels Array Info")
    print(labelsarray.ndim)
    print(labelsarray.size)
    print(labelsarray.shape)
    dataset = np.load(pixelartimages)
    header = np.lib.format.header_data_from_array_1_0(dataset);
    # plt.imshow(dataset, interpolation='nearest')
    # plt.show()
    print(header)
    print(dataset.ndim)
    print(dataset.size)
    print(dataset.shape)
    # print(dataset[0])
    print(dataset[0].ndim)
    print(dataset[0].size)
    print(dataset[0].shape)

    data = dataset[:1000]

    data_flattened = data.reshape(data.shape[0], -1)

    print(data_flattened.shape)
    print(data_flattened)



    kmeans = KMeans(n_clusters=12)
    kmeans.fit(data_flattened)

    # Assuming 'data' is your flattened image data and 'cluster_labels' are the assigned labels
    # num_clusters = 12  # Get the number of clusters
    #
    # # Loop through clusters
    # for cluster in range(num_clusters):
    #     # Select a few images from this cluster (replace 3 with your desired number)
    #     cluster_data = data[kmeans.labels_ == cluster]
    #     image_samples = cluster_data[np.random.choice(len(cluster_data), size=3)]  # Randomly select 3 images
    #
    #     # Plot each image with its cluster label
    #     for image in image_samples:
    #         iconissancekmeans.plot_image(image, cluster)
    #
    # for cluster in range(num_clusters):
    #     directory_name = str(cluster)
    #     path = results_path + '/' + directory_name
    #     os.mkdir(path)
    #     print("Directory for cluster " + directory_name + " created at " + path)
    #     cluster_data = data[kmeans.labels_ == cluster]
    #     for i in range(len(cluster_data)-1):
    #         cluster_image = cluster_data[i]
    #         image_reshaped = cluster_image.reshape(16, 16, 3)
    #         im = Image.fromarray(image_reshaped)
    #         im.save(path + "/cluster_" + str(cluster) + "_img_" + str(i) + ".jpg")

    directoryhandler.prune_results(results_path)


def main():
    initialSetUp()

    return None


if __name__ == '__main__':
    main()
