from math import floor
from typing import NoReturn

import cv2
import json

#converting json file to a dictionary
with open('/Users/joefreybayan/Desktop/ha_challenge/resources/video_1_detections.json', 'r') as detection_output:
  dict1 = json.load(detection_output)

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


def main(video_path: str, title: str) -> NoReturn:
    """Displays a video at half size until it is complete or the 'q' key is pressed.

    Args:
        video_path: the location of the video to be displayed
        title: the title to display in the video window
    """

    video_capture = open_video(video_path)
    width, height = get_frame_dimensions(video_capture)
    wait_time = get_frame_display_time(video_capture)

    #initialise frame id 
    y = 1


    try:
        # read the first frame
        success, frame = video_capture.read()

        # create the window
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)

        # run whilst there are frames and the window is still open
        while success: # and is_window_open(title):
            
            #overlaying bounding boxes
            frameid_as_string = str(y)
            bounding_boxes = dict1[frameid_as_string]["bounding boxes"]
            detected_class = dict1[frameid_as_string]["detected classes"]

            for box, object in zip(bounding_boxes, detected_class):
                
                if object == "car":              
                    bgr = (225,225,225)          #white for cars
                elif object == "person":
                    bgr = (255,225,0)            #sky blue for people
                elif object == "truck":
                    bgr = (255,0,0)              #blue for trucks  
                elif object == "bicycle":
                    bgr = (0,225,0)              #green for bikes
                elif object == "bus":
                    bgr = (0,225,225)            #yellow for buses 
                elif object == "motorbike":
                    bgr = (255,0,225)            #pink for motorbike          
                
                cv2.rectangle(frame, (box[0], box[1]), ((box[0] + box[2]) , box[1] + box[3]), bgr, 2)
           
            
            # shrink it
            smaller_image = cv2.resize(frame, (floor(width // 2), floor(height // 2)))

            #next frame
            y += 1


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
    main(VIDEO_PATH, "My Video")
