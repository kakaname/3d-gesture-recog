import glob
import os
import pathlib
import cv2
import mediapipe as mp
import re
from pathlib import Path
import math


gesture_1 = []
gesture_2 = []



file_path = pathlib.Path(pathlib.Path().parent.resolve()).parent.resolve()
for g in range(1,3):

    for f in range(1,3):
        for s in range(1,11):
            new_list = []
            for e in range(1,6):
                for d in range(1,200):
                    path_string = str(file_path) + "/NewData/gesture_" + str(g) + "/finger_" + str(f) + "/subject_" + str(s) + "/essai_" + str(e) + "/depth_" + str(d) +".png"
                    if os.path.exists(path_string):
                        new_list.append((path_string))
                    else:
                        break

            if g == 1:
                gesture_1.append(new_list)
            else:
                gesture_2.append(new_list)

f = open("attempt2_data.txt", "w")

for i in range(len(gesture_1)):
    for j in range(len(gesture_1[i])):
        f.write(gesture_1[i][j])
        f.write(",")
    f.write("\n")

for i in range(len(gesture_2)):
    for j in range(len(gesture_2[i])):
        f.write(gesture_2[i][j])
        f.write(",")
    f.write("\n")

f.close()