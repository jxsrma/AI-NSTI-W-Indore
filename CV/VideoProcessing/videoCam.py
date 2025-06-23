import cv2
video_path="CV\\vid.mp4"

# For Video
# caps=cv2.VideoCapture(video_path)
# For Camera
caps=cv2.VideoCapture(video_path)
 
if not caps.isOpened():
    print("video not found")
    exit()
   
while True:
    status,image=caps.read()
    print(status)
    if not status:
        print('video/camera not found')
        break
    
    # For Mirror Image in Webcam
    # cv2.imshow("windows",cv2.flip(image,1))
    cv2.imshow("windows",image)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        caps.release()
        break
