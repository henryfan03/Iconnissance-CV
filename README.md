# Iconnissance-CV
A computer vision system that identifies objects commonly attributed to video game icons.

## Table of Contents
- **Architecture**
- **Repository Components**
- **Running Instructions**
- **Example Inputs/Outputs**
- **Benchmarks**

### Architecture 
This project implements the functionality of icon classification using the K-means algorithm. It uses Python and multiple frameworks and libraries such as scikit-learn to implement the kmeans and numpy to represent images as arrays.

### Repository Components
The repository consists of a source directory and two other directories containing images.
- The `/src` directory contains the running code of the project.
- The `/PixelArtDataset` directory contains a directory of cleaned 16x16 3-Channel RGB video game icons in the jpg format, as well as a csv with the labels and a numpy array corresponding to the image data and another array corresponding to the image labels.
- The `/TrainingData` directory contains various fullsize icons of different categories to test on.

#### `/src` Contents
- `arrayoperations.py` - Contains helper functions to modify numpy arrays representing the images.
- `directoryhandler.py` - Contains functions to create directories (corresponding to the result of the kmeans classification)
- `iconnissance.py` - Runner code for the entire project.
- `initialsetup.py` - Contains all functions to setup and configure the project.
- `kmeans.py` - Contains code to perform the kmeans algorithm.

### Running Instructions

### Example Inputs/Outputs

### Benchmarks