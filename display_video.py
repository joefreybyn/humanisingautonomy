from math import floor
from typing import NoReturn

import cv2
import json
from collections import OrderedDict
import numpy as np
import math
from cv2 import FONT_HERSHEY_COMPLEX
from cv2 import FONT_HERSHEY_SCRIPT_COMPLEX
from cv2 import FONT_HERSHEY_PLAIN


colour = {
    "car"      :(225,225,225) ,        #white for cars
    "person"   :(255,225,0)   ,        #sky blue for people
    "truck"    :(255,0,0)     ,        #blue for trucks  
    "bicycle"  :(0,225,0)     ,        #green for bikes
    "bus"      :(0,225,225)   ,        #yellow for buses 
    "motorbike":(255,0,225)            #pink for motorbike 
 }


def open_video(path: str) -> cv2.VideoCapture:
    """Opens a video file.

    Args:
        path: the location of the video file to be opened

    Returns:
        An opencv video capture file.
    """
    video_capture = cv2.VideoCapture(path)
    if not video_capture.isOpened():
        raise RuntimeError(f'Video at "{path}" cannot be opened.')
    return video_capture


def get_frame_dimensions(video_capture: cv2.VideoCapture) -> tuple[int, int]:
    """Returns the frame dimension of the given video.

    Args:
        video_capture: an opencv video capture file.

    Returns:
        A tuple containing the height and width of the video frames.

    """
    return video_capture.get(cv2.CAP_PROP_FRAME_WIDTH), video_capture.get(
        cv2.CAP_PROP_FRAME_HEIGHT
    )


def get_frame_display_time(video_capture: cv2.VideoCapture) -> int:
    """Returns the number of milliseconds each frame of a VideoCapture should be displayed.

    Args:
        video_capture: an opencv video capture file.

    Returns:
        The number of milliseconds each frame should be displayed for.
    """
    frames_per_second = video_capture.get(cv2.CAP_PROP_FPS)
    return floor(1000 / frames_per_second)


def is_window_open(title: str) -> bool:
    """Checks to see if a window with the specified title is open."""

    # all attempts to get a window property return -1 if the window is closed
    return cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) >= 1


def main(video_path: str, json_path: str, title: str) -> NoReturn:
    #converting json file to a dictionary
    with open(json_path, 'r') as detection_output:
        dict = json.load(detection_output)
    
    """Displays a video at half size until it is complete or the 'q' key is pressed.

    Args:
        video_path: the location of the video to be displayed
        title: the title to display in the video window
    """

    video_capture = open_video(video_path)
    width, height = get_frame_dimensions(video_capture)
    wait_time = get_frame_display_time(video_capture)

    #initialise frame id 
    frame_id = 0
    personID = 0
    
    #create empty dictionary for centroid to append centroid every loop
    centroid = {}
    centroid_prev = {}
    tracker = {}
    try:
        # read the first frame
        success, frame = video_capture.read()

        # create the window
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)

  
       
        # run whilst there are frames and the window is still open
        while success: # and is_window_open(title):
            #next frame
            frame_id += 1
            #retrieve bounding boxes and classes from json file
            frameid_as_string = str(frame_id)
            bounding_boxes = dict[frameid_as_string]["bounding boxes"]
            detected_class = dict[frameid_as_string]["detected classes"]
            #create empty list for the centroid per frame 
            centroid[frame_id] = []
            centroid_prev[frame_id] = []
            tracker[personID] = []
            for box, object in zip(bounding_boxes, detected_class):
                """taking elements from bounding_boxes 
                 x = top left x coordinate
                 y = top left y coordinate
                 w = width 
                 h = height
                """
                x, y, w, h = box
                
                #calculate centroid for pedestrians only
                if object == "person":
                    centroid[frame_id].append((x + (w//2) , y + (h//2)))
                    if frame_id > 1 :
                        centroid_prev[frame_id] = centroid[frame_id-1]


                    for coord in centroid[frame_id]:
                        for coord_prev in centroid_prev[frame_id]:
                            #calcualate Euclidian distance between current frame and previous frame
                            #if the distance is less than 100 then ID will stay the same
                            #otherwise, increment
                            # try:
                                p = math.hypot((coord[0] - coord_prev[0]), (coord[1] - coord_prev[1]))
                                if p < 100:
                                    personID == personID
                                else:
                                    personID += 1   
                                # plot name and centroid
                                cv2.circle(frame, coord, 4, (0, 255, 0), -1)
                                cv2.putText(frame, "ID: " + str(personID), (x, y), FONT_HERSHEY_PLAIN , 2, (255,225,0), 2)                
                            # except:
                            #     #if the previous frame doesnt detect a person, then ignore that frame
                            #     continue
                      




                        
                #plot rectangles
                cv2.rectangle(frame, (x, y), ((x + w) , (y + h)), colour[object], 2)

            # shrink it
            smaller_image = cv2.resize(frame, (floor(width // 2), floor(height // 2)))

            # display it
            cv2.imshow(title, smaller_image)

            # test for quit key
            if cv2.waitKey(wait_time) == ord("q"):
                break

            # read the next frame
            success, frame = video_capture.read()
    finally:
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    VIDEO_PATH = "resources/video_1.mp4"
    JSON_PATH = "resources/video_1_detections.json"
    main(VIDEO_PATH, JSON_PATH, "My Video")
