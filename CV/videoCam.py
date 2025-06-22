import cv2
 
video_path="CV\\vid.mp4"

# For Video
caps=cv2.VideoCapture(video_path)
# For Camera
# caps=cv2.VideoCapture(0)
 
if not caps.isOpened():
    print("video not found")
    exit()
   
while True:
    status,image=caps.read()
    if not status:
        break
    cv2.imshow("windows",cv2.flip(image,1))
    if cv2.waitKey(25) & 0xFF==ord('q'): 
        caps.release()
        break
