import cv2
import os

# Step 1: Load the video file
video_path = 'webcam_output.avi'  # Replace with your video file
cap = cv2.VideoCapture(video_path)

# Step 2: Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get FPS
fps = cap.get(cv2.CAP_PROP_FPS)

# Step 3: Create a directory to save frames
os.makedirs('extracted_frames', exist_ok=True)

# Step 4: Read and save frames with timestamp in filename
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video
    
    # Calculate timestamp
    timestamp_sec = frame_count / fps
    timestamp_str = f"{int(timestamp_sec // 3600):02d}-{int((timestamp_sec % 3600) // 60):02d}-{int(timestamp_sec % 60):02d}.{int((timestamp_sec * 1000) % 1000):03d}"

    frame_filename = f'extracted_frames/frame_{frame_count:04d}_{timestamp_str}.jpg'
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

# Step 5: Clean up
cap.release()
print(f"Extracted {frame_count} frames to the 'extracted_frames' folder.")
