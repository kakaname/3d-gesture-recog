import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import PIL

image_dir = 'C:/Users/anxiety/Desktop/Codepile/3d-gesture-recog/Data'
image_dir = pathlib.Path(image_dir)
gesture_1_dir = 'gesture_1/*/*/*/*.png'
image_count = list(image_dir.glob(gesture_1_dir))

batch_size = 32
img_height = 180
img_width = 180
