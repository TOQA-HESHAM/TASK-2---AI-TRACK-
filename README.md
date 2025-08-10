# TASK-2---AI-TRACK-



Color Tracking using OpenCV
Task Name
Task 1 - Color Detection & Tracking (Video-based)


Objective
The main goal of this task is to detect and track a specific color within a video using computer vision techniques. The project processes each video frame, applies color filtering, and displays the tracking results in real time.


Technologies Used
Python – Main programming language

OpenCV – For video processing and color detection

NumPy – For numerical operations and color range handling



Steps Taken
Prepare the Environment

Installed Python environment via Anaconda.

Installed OpenCV (cv2) and NumPy libraries.

Set Up the Project

Created the project folder and added:

The Python script file color_tracking.py

The video file sample.mp4 for testing.

Write the Code

Loaded the video using cv2.VideoCapture().

Converted each frame from BGR to HSV color space.

Defined the HSV lower and upper bounds for the target color (blue).

Created a mask to filter only the target color.

Applied the mask to the original frame to highlight the detected areas.

Run the Program

Executed the script to process the video.



Displayed:

Original video frame

Mask showing only the target color as white

Tracked Color showing the detected color in the original image



Result
When running the code, three windows appear:

Original – The original video.

Mask – White pixels indicate the detected target color.

Tracked Color – The original video with only the target color visible, all other colors removed.

