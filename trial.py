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

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

# ['roll over']
# >>> e.tricks
# ['play dead']

class Tracker:
  def __init__(self, id, centroid):
    self.personID = id
    self.centroid = centroid

trackers = {1: [],
2: [Tracker(0, (981, 733)), Tracker(1, (1091, 734))],
3: [Tracker(1, (1090, 731))],
4: [],
5: [Tracker(1, (979, 735))],
6: [Tracker(1, (976, 736)), Tracker(2, (1113, 731))]}

trackers_in_current_frame = trackers[6]
trackers_in_previous_frame = trackers[5]

# for pt in current_centroids:
#   for pt_prev in prev_centroids:
#       p = math.hypot((pt[0] - pt_prev[0]), (pt[1] - pt_prev[1]))
#       # if p < 100:
        

#compare current coordinates to previous coordinates

for tracker in trackers_in_current_frame:
  least_distance = 101

  for prev_tracker in trackers_in_previous_frame:
    p = math.hypot((tracker.centroid[0] - prev_tracker.centroid[0]), (tracker.centroid[1] - prev_tracker.centroid[1]))

#if the distance between current and previous is less than 100 
    if p < 100:

#then whichever is the minimum would retain ID, others will be incremented
      least_distance = min(p,least_distance) 
      if p == least_distance:
        min_distance_tracker = prev_tracker
      tracker.personID = prev_tracker.personID

  print(tracker.personID)

#elif > 100 then increment 


























       
  


# p1 = Person("John", 36)
# p1.myfunc()
# centroid = {1: [], 2: [(981, 733), (1091, 734)], 3: [(1090, 731)], 4: [], 5: [(979, 735)], 6: [(976, 736), (1113, 731)], 7: [(911, 728), (973, 738)], 8: [(974, 741)], 9: [(971, 741)]}
# current_frame = 3
# prev_frame = current_frame- 1

# print(centroid[2][0])
# y = math.hypot((centroid[current_frame][0][0]-centroid[prev_frame][1][0]), (centroid[current_frame][0][1]- centroid[prev_frame][0][1]))
# print(y)
# for key in centroid:
    
# #   # try:
# #      for pt in key:
# #       # for x in n:
# #       #    y = math.hypot((centroid[key][x][0]-centroid[key-1][x][0]), (centroid[key][x][1]-centroid[key-1][x][1]))
#          print(centroid[key])
#   # except:
#   #   print('0')


  

                

