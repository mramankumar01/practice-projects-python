import cv2

face_cap = cv2.CascadeClassifier("C:/Users/amank/AppData/Local/Programs/Python/Python314/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, frame = video_cap.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        color,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("Video", frame)
    if cv2.waitKey(5) == ord('a'):
        break
video_cap.release()
cv2.destroyAllWindows()


'''
# Capture video from the default camera and display it in a window.

video_cap = cv2.VideoCapture(0)
while True:
    ret, frame = video_cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(10) == ord('a'):
        break
video_cap.release()
'''

'''
# EXPLANATION:
----------------------
import cv2

# ============================================================================
# STEP 1: LOAD THE FACE DETECTION MODEL
# ============================================================================
# Load the pre-trained Haar Cascade classifier for face detection
# This XML file contains the trained model data for detecting frontal faces
face_cap = cv2.CascadeClassifier("C:/Users/amank/AppData/Local/Programs/Python/Python314/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# ============================================================================
# STEP 2: INITIALIZE VIDEO CAPTURE
# ============================================================================
# Create a VideoCapture object to access the webcam
# 0 = default camera (use 1, 2, etc. for additional cameras)
video_cap = cv2.VideoCapture(0)

# ============================================================================
# STEP 3: MAIN LOOP - CONTINUOUS FACE DETECTION
# ============================================================================
while True:
    # ------------------------------------------------------------------------
    # Capture a single frame from the webcam
    # ------------------------------------------------------------------------
    # ret = True if frame was successfully captured, False otherwise
    # frame = the actual image data (as a NumPy array)
    ret, frame = video_cap.read()
    
    # ------------------------------------------------------------------------
    # Convert frame to grayscale
    # ------------------------------------------------------------------------
    # Haar Cascade works better and faster on grayscale images
    # COLOR_BGR2GRAY converts from BGR (OpenCV's default) to grayscale
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # ------------------------------------------------------------------------
    # Detect faces in the grayscale frame
    # ------------------------------------------------------------------------
    # detectMultiScale() finds faces at different scales/sizes
    # Returns a list of rectangles where faces were detected
    faces = face_cap.detectMultiScale(
        color,                          # The grayscale image to scan
        scaleFactor=1.1,                # Image scale reduction (1.1 = 10% reduction per step)
        minNeighbors=5,                 # How many neighbors each candidate rectangle should have (higher = fewer false positives)
        minSize=(30, 30),               # Minimum face size in pixels (ignores smaller detections)
        flags=cv2.CASCADE_SCALE_IMAGE   # Flag to scale the image rather than the detector
    )

    # ------------------------------------------------------------------------
    # Draw rectangles around detected faces
    # ------------------------------------------------------------------------
    # faces contains (x, y, w, h) for each detected face
    # x, y = top-left corner coordinates
    # w = width of the face rectangle
    # h = height of the face rectangle
    for (x, y, w, h) in faces:
        # Draw a green rectangle on the original (color) frame
        cv2.rectangle(
            frame,              # Image to draw on
            (x, y),            # Top-left corner of rectangle
            (x+w, y+h),        # Bottom-right corner of rectangle
            (0, 255, 0),       # Color in BGR format (0, 255, 0) = green
            2                  # Thickness of rectangle border in pixels
        )
    
    # ------------------------------------------------------------------------
    # Display the frame with detected faces
    # ------------------------------------------------------------------------
    # Show the frame in a window titled "Video"
    cv2.imshow("Video", frame)
    
    # ------------------------------------------------------------------------
    # Check for exit condition
    # ------------------------------------------------------------------------
    # waitKey(5) waits 5ms for a keyboard input (allows ~200 fps max)
    # If 'a' key is pressed, break the loop and exit
    if cv2.waitKey(5) == ord('a'):
        break

# ============================================================================
# STEP 4: CLEANUP
# ============================================================================
# Release the webcam resource so other applications can use it
video_cap.release()

# Close all OpenCV windows (good practice to add this)
cv2.destroyAllWindows()
'''