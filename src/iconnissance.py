"""
Title: Iconnissance
Author: Henry Fan
Description: A simple vision system for detecting and classifying icons of common video game items. Examples include potions, scrolls, books, swords, and more
"""

"""
Training Accelerator/Hardware Information
CPU: Intel Core i7-12700k
GPU: NVIDIA RTX 3070 8GB GDDR6
RAM: 32GB DDR4 3200 MHZ
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
import arrayoperations

def initialSetUp():
    src_path = os.path.abspath('../src')
    pixel_art_dataset_path = os.path.abspath('../PixelArtDataset')
    print("src path: " + src_path)
    print("pixel_art_dataset_path: " + pixel_art_dataset_path)
    labels = os.path.abspath(pixel_art_dataset_path + '/sprites_labels.npy')
    pixelartimages = os.path.abspath(pixel_art_dataset_path + '/sprites.npy')
    print(labels)
    # with np.load(labels) as data:
    #     a = data['a']
    # data = np.load(labels)
    dataset = np.load(pixelartimages)
    header = np.lib.format.header_data_from_array_1_0(dataset);
    # plt.imshow(dataset, interpolation='nearest')
    # plt.show()
    # print(header)
    print(dataset.ndim)
    print(dataset.size)
    print(dataset.shape)
    # print(dataset[0])
    print(dataset[0].ndim)
    print(dataset[0].size)
    print(dataset[0].shape)

    # Assuming your data is a list of 16x16 images (pixel values)
    data = dataset # Your list of images

    # Define the number of clusters (initial estimate)
    k = 10

    # Reshape data (optional, check scikit-learn documentation for specific requirements)
    data_reshaped = np.array(data).reshape(-1, 16 * 16)  # Flatten each image to a 1D array
    print("Data reshaped: " + str(data_reshaped.ndim))

    # Create and fit the k-means model
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data_reshaped)

    arrayoperations.test()

def main():
    initialSetUp()

    return None

if __name__ == '__main__':
    main()