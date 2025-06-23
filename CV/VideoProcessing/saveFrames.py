#  Extract Frames from a Video
import cv2
import os
# Step 1: Load the video file
video_path = "CV\\vid.mp4"  # Replace with your actual video path
cap = cv2.VideoCapture(video_path)
# Step 2: Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
# Step 3: Create a directory to save frames
os.makedirs('extracted_frames', exist_ok=True)
# Step 4: Read and save frames
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop when video ends
 
    frame_filename = f'extracted_frames/frame_NSTI_Indore_{frame_count:04d}.jpg'
    cv2.imwrite(frame_filename, frame)
    frame_count += 1
# Step 5: Clean up
cap.release()
print(f"Extracted {frame_count} frames to the 'extracted_frames' folder.")