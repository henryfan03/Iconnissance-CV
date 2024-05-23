"""
Title: Iconnissance
Author: Henry Fan
Description: A simple vision system for detecting and classifying icons of common video game items. Examples include potions, scrolls, books, swords, and more
"""

# Setup Code
import os
import numpy as np
from sklearn.cluster import KMeans
import kmeans as iconissancekmeans
import directoryhandler

def initialSetUp():
    src_path = os.path.abspath('../src')
    pixel_art_dataset_path = os.path.abspath('../PixelArtDataset')
    results_path = os.path.abspath('../Results')
    print("src path: " + src_path)
    print("dataset path: " + pixel_art_dataset_path)
    print("results path: " + results_path)
    labels = os.path.abspath(pixel_art_dataset_path + '/sprites_labels.npy')
    pixelartimages = os.path.abspath(pixel_art_dataset_path + '/sprites.npy')
    dataset = np.load(pixelartimages)
    print("Dataset dimensions: " + str(dataset.ndim))
    print("Dataset size: " + str(dataset.size))
    print("Dataset shape: " + str(dataset.shape))

    datasize = input("Enter the number of images you would like to use from the database (i.e. 1000,5000,10000): ")
    data = dataset[:int(datasize)]

    data_flattened = data.reshape(data.shape[0], -1)

    kmeans = KMeans

    number_of_clusters = input("Enter the number of clusters (leave blank to use elbow method): ")
    if number_of_clusters == "":
        print("Close the chart after you have figured out a number")
        iconissancekmeans.WCSS_Elbow_Analysis(data_flattened)
        number_of_clusters = int(input("Select a # of clusters based on if you see an elbow in the curve: "))
        kmeans = KMeans(n_clusters=number_of_clusters)

    elif (isinstance(int(number_of_clusters), int)):
        number_of_clusters = int(number_of_clusters)
        kmeans = KMeans(n_clusters=number_of_clusters)

    kmeans.fit(data_flattened)

    show_images = input("Enter yes if you would like to see some example of classified images: ")
    if (show_images.lower() == "yes"):
        print("Close images to proceed")
        for cluster in range(number_of_clusters):
            cluster_data = data[kmeans.labels_ == cluster]
            image_samples = cluster_data[np.random.choice(len(cluster_data), size=1)]
            for image in image_samples:
                iconissancekmeans.plot_image(image, cluster)

    resultdirectoryname = ""
    while (resultdirectoryname == ""):
        resultdirectoryname = input("Enter a name for the result folder: (i.e. test): ")

    result_path = results_path + "/" + resultdirectoryname;

    directoryhandler.save_results(result_path, number_of_clusters, data, kmeans)


def main():
    initialSetUp()

    return None


if __name__ == '__main__':
    main()
