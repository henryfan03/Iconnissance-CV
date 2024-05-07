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

def main():
    src_path = os.path.abspath('../src')
    image_database_path = os.path.abspath('../ImageDatabase')
    arr = os.listdir('../ImageDatabase')
    print(arr)
    print("Image database path: " + image_database_path)
    print("Source code path: " + src_path)
    return None

if __name__ == '__main__':
    main()