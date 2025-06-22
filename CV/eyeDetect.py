import cv2
# Step 1: Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
 
# Step 2: Start the webcam
cap = cv2.VideoCapture(0)
# Step 3: Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
# Step 4: Read frames from webcam
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convert frame to grayscale (Haar cascade needs grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
 
        # Region of interest for eyes inside face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
 
        # Detect eyes within face
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Face Detection - Webcam', frame)
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Step 5: Release resources
cap.release()
cv2.destroyAllWindows()