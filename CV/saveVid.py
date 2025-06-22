import cv2
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
output_path = 'webcam_output.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter(output_path, fourcc, 30.0, (frame_width, frame_height))
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    out.write(frame)  # Write the frame to the video file
    cv2.imshow('Webcam Feed', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()