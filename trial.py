from math import floor
from typing import NoReturn

import cv2
import json
with open('/Users/joefreybayan/Desktop/ha_challenge/resources/video_1_detections.json', 'r') as f:
  dict1 = json.load(f)
for y in range (1,6):
    z = str(y)
    x = dict1[z]["bounding boxes"]
    print(x)


list_of_lists = [ [1, 2, 3], [4, 5], [7, 8, 9 , 10]]
for list in list_of_lists:

        print(list[0]//2)

