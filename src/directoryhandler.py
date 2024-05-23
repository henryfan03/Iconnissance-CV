import os
from PIL import Image


def save_results(results_path, num_clusters, data, kmeans):
    os.mkdir(results_path)
    for cluster in range(num_clusters):
        directory_name = str(cluster)
        path = results_path + '/' + directory_name
        os.mkdir(path)
        print("Directory for cluster " + directory_name + " created at " + path)
        cluster_data = data[kmeans.labels_ == cluster]
        for i in range(len(cluster_data) - 1):
            cluster_image = cluster_data[i]
            image_reshaped = cluster_image.reshape(16, 16, 3)
            im = Image.fromarray(image_reshaped)
            im.save(path + "/cluster_" + str(cluster) + "_img_" + str(i) + ".jpg")
