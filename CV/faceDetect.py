import cv2

# Step 1: Load the Haar Cascade XML file for face detection
# This XML comes with OpenCV: usually in 'data/haarcascades' folder
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Step 2: Open the webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Step 3: Loop to read frames and detect faces
while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale (Haar cascade works on gray images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,               # input image
        scaleFactor=1.3,    # image size reduction at each scale (1.1 to 1.5 works well)
        minNeighbors=5,     # how many neighbors each candidate rectangle should have to retain it
        minSize=(30, 30)    # minimum size of detected face
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the result
    cv2.imshow('Webcam Face Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 4: Clean up
cap.release()
cv2.destroyAllWindows()
