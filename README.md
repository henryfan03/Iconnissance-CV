# Iconnissance-CV
A simple computer vision system that identifies objects commonly attributed to video game icons.

## Table of Contents
- **Architecture**
- **Repository Components**
- **Running Instructions**
- **Example Inputs/Outputs**
- **Resources**

### Architecture 
This project implements the functionality of icon classification using the K-means algorithm. It uses Python and multiple frameworks and libraries such as scikit-learn to implement the kmeans and numpy to represent images as arrays. While it does not perform tradition supervised learning image classification, image classification is achieved via unsupervised categorization of input images through the Kmeans and WCSS (Within-cluster sum of squares) and the elbow method to determine a good value for clusters

### Repository Components
The repository consists of a source directory and two other directories containing images.
- The `/src` directory contains the running code of the project.
- The `/PixelArtDataset` directory contains a directory of cleaned 16x16 3-Channel RGB video game icons in the jpg format, as well as a csv with the labels and a numpy array corresponding to the image data and another array corresponding to the image labels.
- The `/Results` directory contains all finished folders for each run.

#### `/src` Contents
- `directoryhandler.py` - Contains functions to create directories (corresponding to the result of the kmeans classification)
- `iconnissance.py` - Runner code for the entire project.
- `kmeans.py` - Contains code to perform the kmeans algorithm.

### Running Instructions
- After downloading this repo, `cd src`
- If you have python3 installed, run `python3 iconissance.py`
- There are a couple of steps to fully identify images.
- Select sample size: Pick any number between 0-89400, I used 1000, 5000, etc. In the 50000+ it becomes a bit slow but will finish running.
- Selecting cluster size: You can test out any number for clusters, but any number that is too low or too high will not yield good results. 
- Cluster-size selection can be found using the elbow method, where you can look for elbows on the graph and choose accordingly. You must close the chart in order for the code to proceed.
- Plotting example classified images: enter yes to view a few samples of images classified into clusters. You must close the images in order for the code to proceed.
- Saving identified images: enter a name for the resulting folder for classified images.

### Example Inputs/Outputs
- This dataset used in this project is very large, with around 89,000 unclassified images, running the kmeans algorithm on the entire dataset takes a very long time, so it is suggested when running you select a smaller number such as 1000, 5000, 10000.
- It is not perfect but in general will select pretty similar categories such as food, people, and objects in a similar manner. Color is weighted in the classification, so it may not be as good as identifying specific things such as how grayscale classifiers do.

### Resources
- This project uses [Ebrahim Elgazar's Pixel Art Dataset](https://www.kaggle.com/datasets/ebrahimelgazar/pixel-art) under the Apache License 2.0.
- I do not own any of the artworks used as the training data for this project.