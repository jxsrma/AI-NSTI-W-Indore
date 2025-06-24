import cv2

# 1️⃣ Open webcam or video file
cap = cv2.VideoCapture('CV\\vid.mp4')  # 0 for webcam, or use 'video.mp4'

# 2️⃣ Read first frame
ret, frame = cap.read()
if not ret:
    print("Cannot read video source")
    exit()

# 3️⃣ Let user select ROI (Region Of Interest) with mouse
roi = cv2.selectROI("Select Object to Track", frame, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
track_window = (x, y, w, h)

# 4️⃣ Set up ROI for tracking: get histogram of the selected area
roi_frame = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 5️⃣ Define termination criteria: either 10 iterations or move by at least 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# 6️⃣ Start tracking in video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV for backprojection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Backproject the histogram to get the probability image
    back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply Mean Shift to get the new location
    ret, track_window = cv2.meanShift(back_proj, track_window, term_crit)

    # Draw rectangle on the tracked object
    x, y, w, h = track_window
    result = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the result
    cv2.imshow('Mean Shift Tracking', result)

    # Press 'q' to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# 7️⃣ Clean up
cap.release()
cv2.destroyAllWindows()
