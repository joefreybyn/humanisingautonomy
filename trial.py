from math import floor
from typing import NoReturn

import cv2
import json
with open('/Users/joefreybayan/Desktop/ha_challenge/resources/video_1_detections.json', 'r') as f:
  dict1 = json.load(f)
# temp = []
# for y in range (1,len(dict1)):
#     z = str(y)
#     x = dict1[z]["bounding boxes"]
#     a = dict1[z]["detected classes"]
    
#     for n in a:
#         if n not in temp:
#             temp.append(n)
# print (temp)

# temp2 = []
# list_of_lists = [ [1, 2, 3], [4, 3], [7, 8, 9 , 10]]
# for list in list_of_lists:
#     for x in list:
#         if x not in temp2:
#             temp2.append(x)

# print (temp2)
# def calculate_centroid(*bounding_box):

#     centroid = (bounding_box[0] + (bounding_box[2]//2) , bounding_box[1] + (bounding_box[3]//2))

#     return centroid

# for y in range (1,6):
#     z = str(y)
#     x = dict1[z]["bounding boxes"]
#     a = dict1[z]["detected classes"]
#     for box in x:
#         b = calculate_centroid(x[box])
#         print (b)

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()

# x = {}
# for y in range (3):
#     x[y] = (1, 1)
#     for z in range (2):
#         x[z].update(2,2)
# print(x)