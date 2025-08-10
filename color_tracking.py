import cv2
import numpy as np

# Path to the video file
video_path = "sample.mp4"

# Define the color range in HSV (Example: Blue color)
lower_color = np.array([100, 150, 50])   # Lower bound
upper_color = np.array([140, 255, 255])  # Upper bound

# Open the video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error: Video file not found.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the chosen color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display results
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Tracked Color", result)

    # Press ESC to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
