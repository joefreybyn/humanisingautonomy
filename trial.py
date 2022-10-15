from math import floor
from typing import NoReturn
import math
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
centroid = {1: [], 2: [(981, 733), (1091, 734)], 3: [(1090, 731)], 4: [], 5: [(979, 735)], 6: [(976, 736), (1113, 731)], 7: [(911, 728), (973, 738)], 8: [(974, 741)], 9: [(971, 741)]}
current_frame = 3
prev_frame = current_frame- 1

# print(centroid[2][0])
# y = math.hypot((centroid[current_frame][0][0]-centroid[prev_frame][1][0]), (centroid[current_frame][0][1]- centroid[prev_frame][0][1]))
# print(y)
for key in centroid:
    
#   # try:
#      for pt in key:
#       # for x in n:
#       #    y = math.hypot((centroid[key][x][0]-centroid[key-1][x][0]), (centroid[key][x][1]-centroid[key-1][x][1]))
         print(centroid[key])
  # except:
  #   print('0')


  

                

